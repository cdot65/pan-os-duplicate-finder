# Installation Guide for pan-os-duplicate-finder

This guide will help you install the `pan-os-duplicate-finder` tool in your Python environment.

## Prerequisites

Before starting, ensure you have:
- Python 3.10 or higher
- pip (Python package installer)
- Access to a PAN-OS device (Panorama or firewall)
- Network connectivity to your PAN-OS device

## Installation Steps

### 1. Create a Virtual Environment (Recommended)

It's best practice to use a virtual environment:

**On macOS and Linux:**
<div class="termy">

```bash
$ python3 -m venv panos-env
$ source panos-env/bin/activate
```

</div>

**On Windows:**
<div class="termy">

```bash
$ python3 -m venv panos-env
$ panos-env\Scripts\activate
```

</div>

### 2. Install via pip

Install the package using pip:

<div class="termy">

```bash
$ pip install pan-os-duplicate-finder
---> 100%
Successfully installed pan-os-duplicate-finder
```

</div>

### 3. Verify Installation

Verify the installation by running:

<div class="termy">

```bash
$ pan-os-duplicate-finder --version
PAN-OS Duplicate Address Finder v0.1.0
```

</div>

## Dependencies

The tool automatically installs required dependencies:
- pan-os-python
- typer[all]
- rich
- pandas
- tabulate
- pyyaml

## Upgrading

To upgrade to the latest version:

<div class="termy">

```bash
$ pip install --upgrade pan-os-duplicate-finder
```

</div>

## Development Installation

For contributing or development:

<div class="termy">

```bash
$ git clone https://github.com/cdot65/pan-os-duplicate-finder.git
$ cd pan-os-duplicate-finder
$ poetry install
```

</div>

## Next Steps

With installation complete, proceed to the [Getting Started Guide](getting-started.md) to begin finding duplicate address objects in your PAN-OS configuration.