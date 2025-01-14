# pan_os_duplicate_finder/commands/find_duplicates.py

import logging
from pathlib import Path
from datetime import datetime
import csv
from typing import Optional, TextIO

import typer
from rich.console import Console
from rich.table import Table
from panos.panorama import Panorama, DeviceGroup
from panos.objects import AddressObject

from ..utilities.settings import load_settings
from ..utilities.analysis import find_duplicate_objects

logger = logging.getLogger(__name__)
console = Console()


def find_duplicates(
    hostname: Optional[str] = typer.Option(None, help="Firewall/Panorama hostname"),
    username: Optional[str] = typer.Option(None, help="Username for authentication"),
    password: Optional[str] = typer.Option(None, help="Password", hide_input=True),
    settings_file: Path = typer.Option(
        "settings.yaml", "--settings", "-s", help="Path to settings file"
    ),
    output_file: Optional[Path] = typer.Option(
        None, "--output", "-o", help="Output CSV file path"
    ),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug logging"),
) -> None:
    """Find duplicate address objects across device groups."""
    try:
        # Set up logging
        log_level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(level=log_level)

        # Load settings if needed
        if not all([hostname, username, password]):
            config = load_settings(settings_file)
            hostname = hostname or config.get("hostname")
            username = username or config.get("username")
            password = password or config.get("password")

        if not all([hostname, username, password]):
            raise typer.BadParameter("Missing required connection parameters")

        # Connect to Panorama
        with console.status("Connecting to device..."):
            pan = Panorama(
                hostname=hostname,
                api_username=username,
                api_password=password,
            )

        # Get all address objects
        all_objects = []

        with console.status("Retrieving address objects..."):
            # Get shared objects
            shared_objects = AddressObject.refreshall(pan)
            all_objects.extend([("shared", obj) for obj in shared_objects])

            # Get device groups
            device_groups = DeviceGroup.refreshall(pan)
            for dg in device_groups:
                logger.info(f"Retrieving objects from device group: {dg.name}")
                dg_objects = AddressObject.refreshall(dg)
                all_objects.extend([(dg.name, obj) for obj in dg_objects])

        # Find duplicates
        with console.status("Analyzing for duplicates..."):
            duplicates = find_duplicate_objects(all_objects)

        if not duplicates:
            console.print("\n[green]No duplicate address objects found![/green]")
            return

        # Generate output filename if not provided
        if not output_file:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            output_file = Path(f"duplicates_{timestamp}.csv")

        # Write CSV report
        fieldnames = [
            "address_value",
            "address_type",
            "object_name",
            "device_group",
            "duplicate_group",
            "description",
        ]

        with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
            csvfile: TextIO
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i, (key, objects) in enumerate(duplicates.items(), 1):
                addr_type, value = key.split(":", 1)

                for dg_name, obj in objects:
                    writer.writerow(
                        {
                            "address_value": value,
                            "address_type": addr_type,
                            "object_name": obj.name,
                            "device_group": dg_name,
                            "duplicate_group": f"Group_{i}",
                            "description": getattr(obj, "description", ""),
                        }
                    )

        console.print(
            f"\n[green]Found {len(duplicates)} sets of duplicate address objects.[/green]"
        )
        console.print(f"[green]Results written to: {output_file}[/green]")

        # Display summary table
        table = Table(title="Duplicate Address Objects Summary")
        table.add_column("Address Type", style="cyan")
        table.add_column("Value", style="green")
        table.add_column("Duplicate Count", style="magenta")
        table.add_column("Device Groups", style="yellow")

        for key, objects in duplicates.items():
            addr_type, value = key.split(":", 1)
            device_groups = {dg_name for dg_name, _ in objects}
            table.add_row(
                addr_type, value, str(len(objects)), ", ".join(sorted(device_groups))
            )

        console.print("\n", table)

    except Exception as e:
        logger.error(f"Error during execution: {e}")
        raise typer.Exit(code=1)
