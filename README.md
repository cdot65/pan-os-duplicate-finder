# PAN-OS Duplicate Finder

[![Python versions](https://img.shields.io/pypi/pyversions/pan-os-duplicate-finder.svg)](https://pypi.org/project/pan-os-duplicate-finder/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

`pan-os-duplicate-finder` is a command-line tool designed to identify duplicate address objects across Palo Alto Networks firewalls and Panorama device groups. This tool helps network administrators maintain cleaner configurations by identifying redundant address objects that could be consolidated.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Creating the Settings File](#creating-the-settings-file)
- [Finding Duplicates](#finding-duplicates)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Easy Setup**: Store credentials and preferences in a `settings.yaml` file for reuse
- **Comprehensive Search**: Scans both shared space and all device groups
- **Flexible Output**: Generate CSV reports with detailed information about duplicates
- **Rich Console Output**: Clear, colorful display of duplicate findings
- **Device Group Awareness**: Track which device groups contain duplicate objects
- **Secure Credentials**: Support for both direct credential input and settings file

## Installation

**Requirements**:

- Python 3.10 or higher

Install directly from PyPI:

```bash
pip install pan-os-duplicate-finder
```

## Basic Usage

Once installed, the primary command is `pan-os-duplicate-finder`. Running `--help` displays available options and commands:

```bash
pan-os-duplicate-finder --help
```

Available commands include:
- `find`: Find duplicate address objects
- `settings`: Create a settings file
- `version`: Show version information

## Creating the Settings File

Before scanning for duplicates, you can create a `settings.yaml` file to store your credentials and preferences:

```bash
pan-os-duplicate-finder settings
```

This will create a template `settings.yaml` file that you can edit with your specific details:

```yaml
hostname: ""        # Your Panorama or firewall hostname/IP
username: ""        # Your username
password: ""        # Your password
logging: "INFO"     # Logging level (INFO/DEBUG)
output_format: "csv"  # Output format for results
```

## Finding Duplicates

With your settings configured, you can search for duplicate address objects:

```bash
# Using settings file
pan-os-duplicate-finder find

# Or provide credentials directly
pan-os-duplicate-finder find --hostname panorama.example.com --username admin
```

The tool will:
1. Connect to your device
2. Retrieve all address objects from shared space and device groups
3. Analyze for duplicates
4. Generate a CSV report
5. Display a summary in the console

Example CSV output includes:
- Object name
- Device group location
- Address value
- Address type
- Description
- Duplicate group identifier

Example console output shows:
- Total number of duplicates found
- Summary table of duplicates by type
- Device groups containing duplicates

### Additional Options

```bash
# Enable debug logging
pan-os-duplicate-finder find --debug

# Specify output file
pan-os-duplicate-finder find --output my-report.csv

# Save debug logs to file
pan-os-duplicate-finder find --debug --log-file debug.log
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

`pan-os-duplicate-finder` is licensed under the Apache 2.0 License. See the [LICENSE](./LICENSE) file for more details.