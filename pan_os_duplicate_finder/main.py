# pan_os_duplicate_finder/main.py

"""
PAN-OS Duplicate Finder CLI Application

Provides commands to find and analyze duplicate address objects across PAN-OS device groups.

Commands:
- `find`: Find duplicate address objects
- `version`: Show version information
- `settings`: Create settings file

Usage:
    pan-os-duplicate-finder <command> [OPTIONS]
"""

import logging
import typer
from rich.console import Console

from pan_os_duplicate_finder import (
    find_duplicates,
    create_settings,
    show_version,
)

# Initialize Typer app and Rich console
app = typer.Typer(
    name="pan-os-duplicate-finder",
    help="Find duplicate address objects across PAN-OS device groups",
)
console = Console()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------------------------------------------------
# CLI Commands
# ---------------------------------------------------------------------------------------------------------------------

# Find duplicate address objects
app.command(
    name="find",
    help="Find duplicate address objects across device groups.",
)(find_duplicates)

# Create settings file
app.command(
    name="settings",
    help="Create a settings.yaml file with configuration (required for first time setup).",
)(create_settings)

# Show version information
app.command(
    name="version",
    help="Show version information.",
)(show_version)

if __name__ == "__main__":
    app()
