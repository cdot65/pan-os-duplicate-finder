# pan_os_duplicate_finder/commands/create_settings.py

import typer
from pathlib import Path
import yaml
from rich.console import Console

console = Console()


def create_settings(
    output_file: Path = typer.Option(
        "settings.yaml", "--output", "-o", help="Output settings file path"
    )
) -> None:
    """Create a settings.yaml file with configuration."""
    settings = {
        "hostname": "",
        "username": "",
        "password": "",
        "logging": "INFO",
        "output_format": "csv",
    }

    try:
        with open(output_file, "w") as f:
            yaml.dump(settings, f, default_flow_style=False)
        console.print(f"[green]Created settings file: {output_file}[/green]")
        console.print("Please edit the file and add your connection details.")
    except Exception as e:
        console.print(f"[red]Error creating settings file: {e}[/red]")
        raise typer.Exit(code=1)
