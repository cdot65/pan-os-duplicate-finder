# Getting Started with pan-os-duplicate-finder

This guide will help you get started with `pan-os-duplicate-finder`, from initial setup to finding your first duplicate address objects.

## Step 1: Create a Settings File

Before scanning for duplicates, create a `settings.yaml` file containing your device credentials and preferences:

<div class="termy">

```bash
$ pan-os-duplicate-finder settings
```

</div>

You will be prompted to enter:
- Hostname/IP of your Panorama or firewall
- Username and password
- Logging level (e.g., INFO)
- Output format preferences

After completion, `settings.yaml` will be created in your current directory:

```yaml
hostname: "panorama.example.com"
username: "admin"
password: "your-password"
logging: "INFO"
output_format: "csv"
```

## Step 2: Finding Duplicate Objects

With your settings in place, you can search for duplicate address objects:

<div class="termy">

```bash
# Using settings file
$ pan-os-duplicate-finder find

# Or provide credentials directly
$ pan-os-duplicate-finder find --hostname panorama.example.com --username admin
```

</div>

The tool will:
1. Connect to your device
2. Retrieve address objects from all device groups
3. Analyze for duplicates
4. Generate a CSV report
5. Display a summary in the console

### Understanding the Output

The CSV report includes:
- Object name
- Device group location
- Address value
- Address type
- Description
- Duplicate group identifier

The console summary shows:
- Total duplicates found
- Summary by device group
- Detailed analysis of each duplicate set

## Additional Options

### Enable Debug Logging
```bash
pan-os-duplicate-finder find --debug
```

### Specify Output File
```bash
pan-os-duplicate-finder find --output my-report.csv
```

### Save Debug Logs
```bash
pan-os-duplicate-finder find --debug --log-file debug.log
```

## Next Steps

With basic functionality understood, you can:
- Review the [Commands Reference](../reference/commands.md) for detailed command options
- Check [Examples](examples.md) for more complex scenarios
- Set up automatic scanning using the [Configuration Guide](configuration.md)

For troubleshooting help, see our [Troubleshooting Guide](../reference/troubleshooting.md).