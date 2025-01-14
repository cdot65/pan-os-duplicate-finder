# PAN-OS Duplicate Finder CLI Commands Reference

## Table of Contents

- [Overview](#overview)
- [Basic Configuration](#basic-configuration)
- [Command Reference](#command-reference)
- [Best Practices](#best-practices)

## Overview

The `pan-os-duplicate-finder` command-line interface (CLI) helps identify duplicate address objects across PAN-OS device groups. It reads credentials from a `settings.yaml` file or accepts them as command-line arguments.

**Global Options:**
- `--help`: Display the help message and exit

**Key Features:**
- Load credentials from `settings.yaml`
- Override settings at runtime
- Generate detailed CSV reports
- Rich console output with progress indicators
- Debug logging capabilities
- Support for all address object types

## Basic Configuration

Before using the CLI, you can create a `settings.yaml` file to store credentials and preferences:

<div class="termy">

```bash
pan-os-duplicate-finder settings
```

</div>

You'll be prompted for:
- Device hostname/IP
- Username and password
- Logging preferences
- Output format preferences

**Example `settings.yaml`:**
```yaml
hostname: "panorama.example.com"
username: "admin"
password: "your-password"
logging: "INFO"
output_format: "csv"
```

## Command Reference

### Main Commands

| Command    | Description                               |
|------------|-------------------------------------------|
| `find`     | Find duplicate address objects            |
| `settings` | Create/update settings file               |
| `version`  | Display version information               |

### find

Find duplicate address objects across device groups.

**Usage:**

```bash
pan-os-duplicate-finder find [OPTIONS]
```

**Options:**
| Option                | Description                          | Default        |
|----------------------|--------------------------------------|----------------|
| `--hostname`         | Device hostname/IP                   | From settings  |
| `--username`         | Authentication username              | From settings  |
| `--password`         | Authentication password              | From settings  |
| `--debug, -d`        | Enable debug logging                 | False          |
| `--output, -o`       | CSV output file path                 | Auto-generated |
| `--log-file, -l`     | Log file path                       | None           |
| `--settings-file, -s`| Custom settings file path           | settings.yaml  |

**Example:**

```bash
pan-os-duplicate-finder find --hostname panorama.example.com --username admin
```

### settings

Create or update the settings file.

**Usage:**

```bash
pan-os-duplicate-finder settings [OPTIONS]
```

**Options:**
| Option                | Description                          | Default        |
|----------------------|--------------------------------------|----------------|
| `--output, -o`       | Settings file path                   | settings.yaml  |

**Example:**

```bash
pan-os-duplicate-finder settings --output prod-settings.yaml
```

### version

Display version information.

**Usage:**

```bash
pan-os-duplicate-finder version
```

## Output Formats

### CSV Report Fields

| Field           | Description                     |
|-----------------|---------------------------------|
| address_value   | The actual IP/FQDN value        |
| address_type    | Type (ip-netmask/ip-range/fqdn) |
| object_name     | Name of the address object      |
| device_group    | Location of the object          |
| duplicate_group | Identifier for duplicate set    |
| description     | Object description if available |

### Console Output

The tool provides rich console output including:
- Progress indicators
- Summary tables
- Device group statistics
- Error messages and warnings

## Best Practices

1. **Use Settings File**:
   - Maintain separate settings files for different environments
   - Keep credentials secure

2. **Logging**:
   - Enable debug logging for troubleshooting
   - Use log files for audit trails

3. **Output Management**:
   - Use descriptive output filenames
   - Include dates in filenames for tracking

4. **Regular Scanning**:
   - Schedule regular duplicate checks
   - Keep historical reports for tracking

For more detailed examples and scenarios, see the [Examples](../user-guide/examples.md) page.