"""
Unit tests for machine reservation system (ADR-020).
"""
import pytest

from src.simulation.machine_reservations import (
    MachineReservationManager,
    Reservation,
    ReservationType,
    MachineAvailability,
)


class TestReservationBasics:
    """Test Reservation dataclass."""

    def test_full_duration_reservation(self):
        """Full-duration reservation releases at end_time."""
        res = Reservation(
            machine_id='lathe',
            process_run_id='proc_1',
            reservation_type=ReservationType.FULL_DURATION,
            start_time=0.0,
            end_time=5.0,
            qty_reserved=1.0,
        )

        assert res.release_time == 5.0
        assert res.is_active_at(0.0)
        assert res.is_active_at(2.5)
        assert res.is_active_at(4.9)
        assert not res.is_active_at(5.0)

    def test_partial_reservation(self):
        """Partial reservation releases at start + hr_reserved."""
        res = Reservation(
            machine_id='furnace',
            process_run_id='proc_1',
            reservation_type=ReservationType.PARTIAL,
            start_time=0.0,
            end_time=10.0,  # Process runs for 10 hours
            qty_reserved=1.0,
            hr_reserved=3.0,  # But only reserved for 3 hours
        )

        assert res.release_time == 3.0  # Released at 0 + 3
        assert res.is_active_at(0.0)
        assert res.is_active_at(2.9)
        assert not res.is_active_at(3.0)
        assert not res.is_active_at(5.0)

    def test_partial_reservation_requires_hr_reserved(self):
        """Partial reservation must specify hr_reserved."""
        with pytest.raises(ValueError, match='hr_reserved'):
            Reservation(
                machine_id='furnace',
                process_run_id='proc_1',
                reservation_type=ReservationType.PARTIAL,
                start_time=0.0,
                end_time=5.0,
                qty_reserved=1.0,
            )

    def test_overlaps_with(self):
        """Test overlap detection between reservations."""
        res1 = Reservation(
            machine_id='lathe',
            process_run_id='proc_1',
            reservation_type=ReservationType.FULL_DURATION,
            start_time=0.0,
            end_time=5.0,
            qty_reserved=1.0,
        )

        res2 = Reservation(
            machine_id='lathe',
            process_run_id='proc_2',
            reservation_type=ReservationType.FULL_DURATION,
            start_time=3.0,
            end_time=8.0,
            qty_reserved=1.0,
        )

        res3 = Reservation(
            machine_id='lathe',
            process_run_id='proc_3',
            reservation_type=ReservationType.FULL_DURATION,
            start_time=5.0,
            end_time=10.0,
            qty_reserved=1.0,
        )

        assert res1.overlaps_with(res2)  # Overlap
        assert res2.overlaps_with(res1)  # Symmetric
        assert not res1.overlaps_with(res3)  # Adjacent, no overlap

    def test_overlaps_different_machines(self):
        """Reservations on different machines don't overlap."""
        res1 = Reservation(
            machine_id='lathe',
            process_run_id='proc_1',
            reservation_type=ReservationType.FULL_DURATION,
            start_time=0.0,
            end_time=5.0,
            qty_reserved=1.0,
        )

        res2 = Reservation(
            machine_id='mill',
            process_run_id='proc_2',
            reservation_type=ReservationType.FULL_DURATION,
            start_time=0.0,
            end_time=5.0,
            qty_reserved=1.0,
        )

        assert not res1.overlaps_with(res2)


class TestMachineAvailability:
    """Test MachineAvailability."""

    def test_initial_availability(self):
        """Initial availability equals total capacity."""
        avail = MachineAvailability(
            machine_id='lathe',
            total_capacity=3.0,
        )

        assert avail.available == 3.0
        assert avail.reserved == 0.0

    def test_can_reserve(self):
        """Test capacity checking."""
        avail = MachineAvailability(
            machine_id='lathe',
            total_capacity=3.0,
        )

        assert avail.can_reserve(1.0)
        assert avail.can_reserve(3.0)
        assert not avail.can_reserve(3.1)

    def test_reserve(self):
        """Test reserving capacity."""
        avail = MachineAvailability(
            machine_id='lathe',
            total_capacity=3.0,
        )

        success = avail.reserve(2.0)
        assert success
        assert avail.reserved == 2.0
        assert avail.available == 1.0

    def test_reserve_insufficient(self):
        """Test reserving more than available."""
        avail = MachineAvailability(
            machine_id='lathe',
            total_capacity=3.0,
        )

        success = avail.reserve(4.0)
        assert not success
        assert avail.reserved == 0.0
        assert avail.available == 3.0

    def test_release(self):
        """Test releasing capacity."""
        avail = MachineAvailability(
            machine_id='lathe',
            total_capacity=3.0,
        )

        avail.reserve(2.0)
        avail.release(1.0)

        assert avail.reserved == 1.0
        assert avail.available == 2.0


class TestReservationManager:
    """Test MachineReservationManager."""

    def test_add_full_duration_reservation(self):
        """Add full-duration reservation."""
        manager = MachineReservationManager({'lathe': 2.0})

        success = manager.add_reservation(
            machine_id='lathe',
            process_run_id='proc_1',
            start_time=0.0,
            end_time=5.0,
            qty=1.0,
            unit='count',
        )

        assert success
        assert len(manager.reservations) == 1
        assert manager.reservations[0].reservation_type == ReservationType.FULL_DURATION

    def test_add_partial_reservation(self):
        """Add partial reservation."""
        manager = MachineReservationManager({'furnace': 1.0})

        success = manager.add_reservation(
            machine_id='furnace',
            process_run_id='proc_1',
            start_time=0.0,
            end_time=10.0,
            qty=3.0,  # Reserve for 3 hours
            unit='hr',
        )

        assert success
        assert len(manager.reservations) == 1
        res = manager.reservations[0]
        assert res.reservation_type == ReservationType.PARTIAL
        assert res.release_time == 3.0

    def test_add_reservation_unknown_machine(self):
        """Adding reservation for unknown machine should fail."""
        manager = MachineReservationManager({'lathe': 1.0})

        with pytest.raises(ValueError, match='not found'):
            manager.add_reservation(
                machine_id='unknown',
                process_run_id='proc_1',
                start_time=0.0,
                end_time=5.0,
                qty=1.0,
                unit='count',
            )

    def test_capacity_conflict_detection(self):
        """Reservation exceeding capacity should fail."""
        manager = MachineReservationManager({'lathe': 1.0})

        # First reservation succeeds
        success1 = manager.add_reservation(
            machine_id='lathe',
            process_run_id='proc_1',
            start_time=0.0,
            end_time=5.0,
            qty=1.0,
            unit='count',
        )
        assert success1

        # Second overlapping reservation fails (exceeds capacity)
        success2 = manager.add_reservation(
            machine_id='lathe',
            process_run_id='proc_2',
            start_time=2.0,
            end_time=7.0,
            qty=1.0,
            unit='count',
        )
        assert not success2
        assert len(manager.reservations) == 1

    def test_non_overlapping_reservations(self):
        """Sequential reservations should succeed."""
        manager = MachineReservationManager({'lathe': 1.0})

        success1 = manager.add_reservation(
            machine_id='lathe',
            process_run_id='proc_1',
            start_time=0.0,
            end_time=5.0,
            qty=1.0,
            unit='count',
        )

        success2 = manager.add_reservation(
            machine_id='lathe',
            process_run_id='proc_2',
            start_time=5.0,  # Starts when proc_1 ends
            end_time=10.0,
            qty=1.0,
            unit='count',
        )

        assert success1 and success2
        assert len(manager.reservations) == 2

    def test_multiple_machines_capacity(self):
        """Multiple machines allow parallel reservations."""
        manager = MachineReservationManager({'lathe': 2.0})

        success1 = manager.add_reservation(
            machine_id='lathe',
            process_run_id='proc_1',
            start_time=0.0,
            end_time=5.0,
            qty=1.0,
            unit='count',
        )

        success2 = manager.add_reservation(
            machine_id='lathe',
            process_run_id='proc_2',
            start_time=0.0,
            end_time=5.0,
            qty=1.0,
            unit='count',
        )

        assert success1 and success2
        assert len(manager.reservations) == 2

    def test_partial_reservation_releases_early(self):
        """Partial reservations allow later full-duration reservations."""
        manager = MachineReservationManager({'furnace': 1.0})

        # Partial: reserves 0-3h only
        success1 = manager.add_reservation(
            machine_id='furnace',
            process_run_id='proc_1',
            start_time=0.0,
            end_time=10.0,
            qty=3.0,
            unit='hr',
        )

        # Full: reserves 3-8h (starts after partial releases)
        success2 = manager.add_reservation(
            machine_id='furnace',
            process_run_id='proc_2',
            start_time=3.0,
            end_time=8.0,
            qty=1.0,
            unit='count',
        )

        assert success1 and success2

    def test_remove_reservation(self):
        """Remove reservations by process_run_id."""
        manager = MachineReservationManager({'lathe': 1.0})

        manager.add_reservation(
            machine_id='lathe',
            process_run_id='proc_1',
            start_time=0.0,
            end_time=5.0,
            qty=1.0,
            unit='count',
        )

        removed = manager.remove_reservation('proc_1')

        assert len(removed) == 1
        assert len(manager.reservations) == 0

    def test_get_availability_at(self):
        """Query machine availability at specific time."""
        manager = MachineReservationManager({'lathe': 3.0})

        manager.add_reservation(
            machine_id='lathe',
            process_run_id='proc_1',
            start_time=0.0,
            end_time=5.0,
            qty=2.0,
            unit='count',
        )

        # At t=2.5, 2.0 reserved, 1.0 available
        avail = manager.get_availability_at('lathe', 2.5)
        assert avail.reserved == 2.0
        assert avail.available == 1.0

        # At t=5.0, reservation ended, all available
        avail = manager.get_availability_at('lathe', 5.0)
        assert avail.reserved == 0.0
        assert avail.available == 3.0

    def test_get_reservations_for_machine(self):
        """Get all reservations for a machine."""
        manager = MachineReservationManager({'lathe': 2.0, 'mill': 1.0})

        manager.add_reservation('lathe', 'proc_1', 0.0, 5.0, 1.0, 'count')
        manager.add_reservation('lathe', 'proc_2', 5.0, 10.0, 1.0, 'count')
        manager.add_reservation('mill', 'proc_3', 0.0, 5.0, 1.0, 'count')

        lathe_res = manager.get_reservations_for_machine('lathe')
        assert len(lathe_res) == 2

        mill_res = manager.get_reservations_for_machine('mill')
        assert len(mill_res) == 1

    def test_get_reservations_with_time_range(self):
        """Get reservations filtered by time range."""
        manager = MachineReservationManager({'lathe': 2.0})

        manager.add_reservation('lathe', 'proc_1', 0.0, 5.0, 1.0, 'count')
        manager.add_reservation('lathe', 'proc_2', 5.0, 10.0, 1.0, 'count')
        manager.add_reservation('lathe', 'proc_3', 10.0, 15.0, 1.0, 'count')

        # Get reservations in range 3-8
        res = manager.get_reservations_for_machine('lathe', time_range=(3.0, 8.0))
        assert len(res) == 2  # proc_1 and proc_2

    def test_get_reservations_for_process(self):
        """Get all reservations for a process."""
        manager = MachineReservationManager({'lathe': 1.0, 'mill': 1.0})

        manager.add_reservation('lathe', 'proc_1', 0.0, 5.0, 1.0, 'count')
        manager.add_reservation('mill', 'proc_1', 0.0, 5.0, 1.0, 'count')

        res = manager.get_reservations_for_process('proc_1')
        assert len(res) == 2

    def test_find_conflicts(self):
        """Find conflicting reservations."""
        manager = MachineReservationManager({'lathe': 1.0})

        # Force add conflicting reservations (bypass capacity check)
        manager.reservations.append(Reservation(
            machine_id='lathe',
            process_run_id='proc_1',
            reservation_type=ReservationType.FULL_DURATION,
            start_time=0.0,
            end_time=5.0,
            qty_reserved=1.0,
        ))

        manager.reservations.append(Reservation(
            machine_id='lathe',
            process_run_id='proc_2',
            reservation_type=ReservationType.FULL_DURATION,
            start_time=2.0,
            end_time=7.0,
            qty_reserved=1.0,
        ))

        conflicts = manager.find_conflicts()
        assert len(conflicts) == 1

    def test_get_utilization(self):
        """Calculate machine utilization over time range."""
        manager = MachineReservationManager({'lathe': 2.0})

        # Reserve 1 machine for 10 hours
        manager.add_reservation('lathe', 'proc_1', 0.0, 10.0, 1.0, 'count')

        # Utilization: 10 machine-hours / (10 hours * 2 machines) = 0.5
        util = manager.get_utilization('lathe', (0.0, 10.0))
        assert util == pytest.approx(0.5)

    def test_get_utilization_multiple_reservations(self):
        """Utilization with multiple overlapping reservations."""
        manager = MachineReservationManager({'lathe': 2.0})

        # Two machines fully utilized for 5 hours
        manager.add_reservation('lathe', 'proc_1', 0.0, 5.0, 1.0, 'count')
        manager.add_reservation('lathe', 'proc_2', 0.0, 5.0, 1.0, 'count')

        # Utilization: 10 machine-hours / 10 possible = 1.0
        util = manager.get_utilization('lathe', (0.0, 5.0))
        assert util == pytest.approx(1.0)

    def test_advance_time(self):
        """Advance time and get expired reservations."""
        manager = MachineReservationManager({'lathe': 1.0})

        manager.add_reservation('lathe', 'proc_1', 0.0, 5.0, 1.0, 'count')
        manager.add_reservation('lathe', 'proc_2', 5.0, 10.0, 1.0, 'count')

        # Advance to t=6 - proc_1 should be expired
        expired = manager.advance_time(6.0)
        assert len(expired) == 1
        assert expired[0].process_run_id == 'proc_1'

        # Advance to t=11 - proc_2 should be expired
        expired = manager.advance_time(11.0)
        assert len(expired) == 1
        assert expired[0].process_run_id == 'proc_2'
