"""
Run runbook with debug logging enabled.
"""
import logging
import sys

# Enable debug logging BEFORE any imports
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s [%(name)s] %(message)s',
    stream=sys.stdout
)

# Now run the CLI
if __name__ == "__main__":
    # Import after logging is configured
    from src import cli
    sys.exit(cli.main())
