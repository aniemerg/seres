"""
Machine Reservation System (ADR-020)

Manages time-based machine reservations with:
- Full-duration reservations (unit: count/unit)
- Partial reservations (unit: hr)
- Conflict detection and resolution
- Machine availability queries
"""
from __future__ import annotations

from typing import List, Dict, Set, Tuple, Optional, Any
from dataclasses import dataclass, field
from enum import Enum


class ReservationType(Enum):
    """Type of machine reservation."""

    FULL_DURATION = "full_duration"  # Held for entire process (unit: count/unit)
    PARTIAL = "partial"  # Released early (unit: hr)


@dataclass
class Reservation:
    """
    Represents a machine reservation.

    Full-duration reservations:
    - Hold machine from start_time to end_time
    - Quantity reserved for entire duration

    Partial reservations:
    - Book hr_reserved at start_time
    - Released at start_time + hr_reserved (not end_time)
    """

    machine_id: str
    process_run_id: str
    reservation_type: ReservationType
    start_time: float  # Hours
    end_time: float  # Hours (process completion time)
    qty_reserved: float  # Quantity of machines reserved

    # For partial reservations
    hr_reserved: Optional[float] = None  # Hours reserved (for partial only)
    release_time: Optional[float] = None  # When partial reservation releases

    def __post_init__(self):
        """Compute release time for partial reservations."""
        if self.reservation_type == ReservationType.PARTIAL:
            if self.hr_reserved is None:
                raise ValueError("Partial reservation must specify hr_reserved")
            self.release_time = self.start_time + self.hr_reserved
        else:
            self.release_time = self.end_time

    def is_active_at(self, time: float) -> bool:
        """Check if reservation is active at given time."""
        return self.start_time <= time < self.release_time

    def overlaps_with(self, other: Reservation) -> bool:
        """Check if this reservation overlaps with another."""
        if self.machine_id != other.machine_id:
            return False

        # Check for time overlap
        return not (self.release_time <= other.start_time or
                    other.release_time <= self.start_time)

    def __repr__(self) -> str:
        return (
            f"Reservation(machine={self.machine_id}, "
            f"process={self.process_run_id}, "
            f"type={self.reservation_type.value}, "
            f"time={self.start_time:.2f}-{self.release_time:.2f}h, "
            f"qty={self.qty_reserved})"
        )


@dataclass
class MachineAvailability:
    """Tracks machine availability at a specific time."""

    machine_id: str
    total_capacity: float  # Total machines available
    reserved: float = 0.0  # Currently reserved
    available: float = 0.0  # Currently available

    def __post_init__(self):
        """Initialize available capacity."""
        self.available = self.total_capacity - self.reserved

    def can_reserve(self, qty: float) -> bool:
        """Check if qty machines can be reserved."""
        return self.available >= qty

    def reserve(self, qty: float) -> bool:
        """
        Reserve qty machines.

        Returns:
            True if successful, False if insufficient capacity
        """
        if not self.can_reserve(qty):
            return False

        self.reserved += qty
        self.available -= qty
        return True

    def release(self, qty: float) -> None:
        """Release qty machines."""
        self.reserved = max(0.0, self.reserved - qty)
        self.available = min(self.total_capacity, self.available + qty)

    def __repr__(self) -> str:
        return (
            f"MachineAvailability(machine={self.machine_id}, "
            f"total={self.total_capacity}, "
            f"reserved={self.reserved:.2f}, "
            f"available={self.available:.2f})"
        )


class MachineReservationManager:
    """
    Manages machine reservations across time.

    Features:
    - Time-based reservation tracking
    - Conflict detection
    - Capacity queries
    - Automatic release of partial reservations
    """

    def __init__(self, machine_capacities: Dict[str, float]):
        """
        Initialize reservation manager.

        Args:
            machine_capacities: Dict of machine_id -> total capacity (count)
        """
        self.machine_capacities = machine_capacities.copy()
        self.reservations: List[Reservation] = []
        self.current_time: float = 0.0

    def add_reservation(
        self,
        machine_id: str,
        process_run_id: str,
        start_time: float,
        end_time: float,
        qty: float,
        unit: str,
        hr_reserved: Optional[float] = None,
    ) -> bool:
        """
        Add a machine reservation.

        Args:
            machine_id: Machine to reserve
            process_run_id: Process instance ID
            start_time: When reservation starts (hours)
            end_time: When process completes (hours)
            qty: Quantity to reserve
            unit: Reservation unit (count/unit/hr)
            hr_reserved: Hours to reserve (for unit='hr')

        Returns:
            True if reservation successful, False if conflict

        Raises:
            ValueError: If machine doesn't exist or invalid parameters
        """
        if machine_id not in self.machine_capacities:
            raise ValueError(f"Machine '{machine_id}' not found in capacity registry")

        # Determine reservation type
        if unit in ('count', 'unit'):
            res_type = ReservationType.FULL_DURATION
            hr_res = None
        elif unit == 'hr':
            res_type = ReservationType.PARTIAL
            if hr_reserved is None:
                hr_res = qty  # Default: qty is the hours
            else:
                hr_res = hr_reserved
        else:
            raise ValueError(f"Invalid reservation unit: {unit}")

        # Create reservation
        reservation = Reservation(
            machine_id=machine_id,
            process_run_id=process_run_id,
            reservation_type=res_type,
            start_time=start_time,
            end_time=end_time,
            qty_reserved=qty if unit in ('count', 'unit') else 1.0,
            hr_reserved=hr_res,
        )

        # Check for conflicts
        if not self._can_reserve(reservation):
            return False

        # Add reservation
        self.reservations.append(reservation)
        return True

    def _can_reserve(self, new_reservation: Reservation) -> bool:
        """
        Check if a reservation can be made without conflicts.

        Returns:
            True if reservation is possible
        """
        machine_id = new_reservation.machine_id
        total_capacity = self.machine_capacities[machine_id]

        # Get all existing reservations for this machine
        existing = [r for r in self.reservations if r.machine_id == machine_id]

        # Check capacity at all relevant time points
        # Time points: start of new reservation, start/release of existing reservations
        time_points = {new_reservation.start_time}

        for res in existing:
            time_points.add(res.start_time)
            time_points.add(res.release_time)

        # Check capacity at each time point
        for time in sorted(time_points):
            # Count reserved capacity at this time
            reserved = 0.0

            # Add existing reservations active at this time
            for res in existing:
                if res.is_active_at(time):
                    reserved += res.qty_reserved

            # Add new reservation if active at this time
            if new_reservation.is_active_at(time):
                reserved += new_reservation.qty_reserved

            # Check capacity
            if reserved > total_capacity:
                return False

        return True

    def remove_reservation(self, process_run_id: str) -> List[Reservation]:
        """
        Remove all reservations for a process.

        Args:
            process_run_id: Process instance to remove

        Returns:
            List of removed reservations
        """
        removed = [r for r in self.reservations if r.process_run_id == process_run_id]
        self.reservations = [r for r in self.reservations if r.process_run_id != process_run_id]
        return removed

    def get_availability_at(self, machine_id: str, time: float) -> MachineAvailability:
        """
        Get machine availability at a specific time.

        Args:
            machine_id: Machine to query
            time: Time to check (hours)

        Returns:
            MachineAvailability object
        """
        if machine_id not in self.machine_capacities:
            raise ValueError(f"Machine '{machine_id}' not found in capacity registry")

        total = self.machine_capacities[machine_id]

        # Count reserved at this time
        reserved = sum(
            r.qty_reserved
            for r in self.reservations
            if r.machine_id == machine_id and r.is_active_at(time)
        )

        return MachineAvailability(
            machine_id=machine_id,
            total_capacity=total,
            reserved=reserved,
        )

    def get_reserved_qty(
        self,
        machine_id: str,
        start_time: float,
        end_time: float
    ) -> float:
        """
        Get the maximum reserved quantity for a machine over a time range.

        Args:
            machine_id: Machine to query
            start_time: Range start (hours)
            end_time: Range end (hours)

        Returns:
            Maximum reserved quantity over the range
        """
        if machine_id not in self.machine_capacities:
            raise ValueError(f"Machine '{machine_id}' not found in capacity registry")

        reservations = [r for r in self.reservations if r.machine_id == machine_id]
        if not reservations:
            return 0.0

        time_points = {start_time, end_time}
        for res in reservations:
            if res.start_time <= end_time and res.release_time >= start_time:
                time_points.add(res.start_time)
                time_points.add(res.release_time)

        max_reserved = 0.0
        for time in sorted(time_points):
            if time < start_time or time > end_time:
                continue
            reserved = sum(
                r.qty_reserved
                for r in reservations
                if r.is_active_at(time)
            )
            if reserved > max_reserved:
                max_reserved = reserved

        return max_reserved

    def get_reservations_for_machine(
        self,
        machine_id: str,
        time_range: Optional[Tuple[float, float]] = None
    ) -> List[Reservation]:
        """
        Get all reservations for a machine.

        Args:
            machine_id: Machine to query
            time_range: Optional (start, end) time range filter

        Returns:
            List of reservations
        """
        reservations = [r for r in self.reservations if r.machine_id == machine_id]

        if time_range:
            start, end = time_range
            reservations = [
                r for r in reservations
                if r.start_time < end and r.release_time > start
            ]

        return sorted(reservations, key=lambda r: r.start_time)

    def get_reservations_for_process(self, process_run_id: str) -> List[Reservation]:
        """Get all reservations for a process."""
        return [r for r in self.reservations if r.process_run_id == process_run_id]

    def advance_time(self, new_time: float) -> List[Reservation]:
        """
        Advance current time and return expired reservations.

        Args:
            new_time: New current time (hours)

        Returns:
            List of reservations that expired in this time window
        """
        expired = [
            r for r in self.reservations
            if self.current_time <= r.release_time < new_time
        ]

        self.current_time = new_time
        return expired

    def find_conflicts(self) -> List[Tuple[Reservation, Reservation]]:
        """
        Find all overlapping reservations.

        Returns:
            List of (reservation1, reservation2) conflict pairs
        """
        conflicts = []

        for i, res1 in enumerate(self.reservations):
            for res2 in self.reservations[i + 1:]:
                if res1.overlaps_with(res2):
                    # Check if they exceed capacity
                    machine_id = res1.machine_id
                    capacity = self.machine_capacities[machine_id]

                    # Find overlap time range
                    overlap_start = max(res1.start_time, res2.start_time)
                    overlap_end = min(res1.release_time, res2.release_time)

                    # Check capacity during overlap
                    reserved = res1.qty_reserved + res2.qty_reserved
                    if reserved > capacity:
                        conflicts.append((res1, res2))

        return conflicts

    def get_utilization(
        self,
        machine_id: str,
        time_range: Tuple[float, float]
    ) -> float:
        """
        Calculate machine utilization over a time range.

        Args:
            machine_id: Machine to analyze
            time_range: (start, end) time range

        Returns:
            Utilization ratio (0.0 to 1.0)
        """
        if machine_id not in self.machine_capacities:
            raise ValueError(f"Machine '{machine_id}' not found")

        start, end = time_range
        if end <= start:
            return 0.0

        total_capacity = self.machine_capacities[machine_id]
        if total_capacity == 0:
            return 0.0

        # Get reservations in range
        reservations = self.get_reservations_for_machine(machine_id, time_range)

        if not reservations:
            return 0.0

        # Calculate total machine-hours reserved
        total_machine_hours = 0.0

        for res in reservations:
            # Clip reservation to time range
            res_start = max(res.start_time, start)
            res_end = min(res.release_time, end)

            if res_start < res_end:
                duration = res_end - res_start
                total_machine_hours += duration * res.qty_reserved

        # Calculate utilization
        total_possible_hours = (end - start) * total_capacity
        return total_machine_hours / total_possible_hours if total_possible_hours > 0 else 0.0

    def __repr__(self) -> str:
        return (
            f"MachineReservationManager("
            f"machines={len(self.machine_capacities)}, "
            f"reservations={len(self.reservations)})"
        )
