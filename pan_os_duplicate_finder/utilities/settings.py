# pan_os_duplicate_finder/utilities/settings.py

import logging
from typing import Dict, Any
import typer
import yaml

logger = logging.getLogger(__name__)


def load_settings(settings_file: str) -> Dict[str, Any]:
    """
    Load configuration settings from a YAML file.

    Args:
        settings_file: Path to the YAML settings file

    Returns:
        Dictionary containing configuration settings
    """
    try:
        with open(settings_file, "r") as f:
            data = yaml.safe_load(f) or {}

        config = {
            "hostname": data.get("hostname"),
            "username": data.get("username"),
            "password": data.get("password"),
            "logging": data.get("logging", "INFO"),
            "output_format": data.get("output_format", "csv"),
        }

        return config

    except Exception as e:
        logger.error(f"Error loading settings from {settings_file}: {e}")
        typer.echo(
            f"❌ Error loading configuration. Please check that '{settings_file}' exists and is properly formatted."
        )
        raise typer.Exit(code=1)
