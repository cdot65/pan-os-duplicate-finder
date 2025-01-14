# pan_os_duplicate_finder/commands/show_version.py

"""Version command implementation."""

from rich.console import Console
from ..version import __version__

console = Console()


def show_version() -> None:
    """Show version information."""
    console.print(f"PAN-OS Duplicate Address Finder v{__version__}")
