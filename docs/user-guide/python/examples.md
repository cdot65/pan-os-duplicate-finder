# Examples

This section provides practical scenarios to help you understand how to use `pan-os-duplicate-finder` effectively. Each example demonstrates different usage patterns, from basic duplicate finding to advanced filtering and output options.

## Table of Contents

- [Overview](#overview)
- [Flags and Parameters](#flags-and-parameters)
- [Basic Usage](#basic-usage)
- [Advanced Usage](#advanced-usage)
- [Output Options](#output-options)
- [Best Practices](#best-practices)

## Overview

Before running duplicate analysis, ensure you have either:
- A `settings.yaml` file configured with your credentials
- Or be prepared to input credentials at runtime

The tool can read from `settings.yaml` first, falling back to command-line arguments and interactive prompts if needed.

## Flags and Parameters

All commands share a common set of flags that interact with the defaults defined in `settings.yaml`:

| Flag/Option           | Description                      | Default from YAML |
|-----------------------|----------------------------------|-------------------|
| `--hostname`          | Panorama/Firewall hostname or IP | From settings     |
| `--username`          | Username for authentication      | From settings     |
| `--password`          | Password for authentication      | From settings     |
| `--debug, -d`         | Enable debug logging             | False             |
| `--output, -o`        | Output CSV file path             | Auto-generated    |
| `--log-file, -l`      | Log file path                    | None              |
| `--settings-file, -s` | Path to settings file            | `settings.yaml`   |

## Basic Usage

### Finding All Duplicates

The simplest way to find duplicates is:

<div class="termy">

```bash
# Using settings file
$ pan-os-duplicate-finder find

# Or provide credentials directly
$ pan-os-duplicate-finder find --hostname panorama.example.com --username admin
```

</div>

This will:
1. Connect to your device
2. Scan all device groups
3. Generate a CSV report
4. Show a summary in the console

### Customizing Output Location

Specify where to save the CSV report:

<div class="termy">

```bash
$ pan-os-duplicate-finder find --output duplicates.csv
```

</div>

## Advanced Usage

### Enabling Debug Output

For troubleshooting or detailed analysis:

<div class="termy">

```bash
$ pan-os-duplicate-finder find --debug --log-file debug.log
```

</div>

### Using a Custom Settings File

If you manage multiple environments:

<div class="termy">

```bash
$ pan-os-duplicate-finder find --settings-file prod-settings.yaml
```

</div>

### Combining Multiple Options

For comprehensive analysis:

<div class="termy">

```bash
$ pan-os-duplicate-finder find \
    --debug \
    --log-file audit.log \
    --output detailed-report.csv
```

</div>

## Output Options

### CSV Report Format

The CSV report includes these columns:
- `address_value`: The actual IP/FQDN
- `address_type`: ip-netmask, ip-range, or fqdn
- `object_name`: Name of the address object
- `device_group`: Location (shared or device group name)
- `duplicate_group`: Identifier linking related duplicates
- `description`: Object description if available

Example CSV content:
```csv
address_value,address_type,object_name,device_group,duplicate_group,description
10.0.0.1,ip-netmask,server1,shared,Group_1,Primary Server
10.0.0.1,ip-netmask,server1-backup,DeviceGroup1,Group_1,Backup Server Config
```

### Console Output

The console displays:
1. Progress indicators during analysis
2. Summary table of duplicates found
3. Device group distribution
4. Total counts and statistics

## Best Practices

1. **Regular Scanning**:
   ```bash
   # Weekly scan with dated output
   $ pan-os-duplicate-finder find --output "duplicates_$(date +%Y%m%d).csv"
   ```

2. **Detailed Troubleshooting**:
   ```bash
   $ pan-os-duplicate-finder find --debug --log-file debug.log
   ```

3. **Production Environments**:
   ```bash
   # Use specific settings file for production
   $ pan-os-duplicate-finder find --settings-file prod.yaml --output prod-audit.csv
   ```

For more detailed reference on commands and their arguments, see the [Commands Reference](../reference/commands.md).