---
hide:
  - navigation
---

<style>
.md-content .md-typeset h1 { display: none; }
</style>

<p align="center">
    <a href="https://paloaltonetworks.com"><img src="https://github.com/cdot65/pan-os-duplicate-finder/blob/main/docs/images/logo.svg?raw=true" alt="PaloAltoNetworks"></a>
</p>
<p align="center">
    <em><code>pan-os-duplicate-finder</code>: Find duplicate address objects across PAN-OS device groups</em>
</p>
<p align="center">
<a href="https://github.com/cdot65/pan-os-duplicate-finder/graphs/contributors" target="_blank">
    <img src="https://img.shields.io/github/contributors/cdot65/pan-os-duplicate-finder.svg?style=for-the-badge" alt="Contributors">
</a>
<a href="https://github.com/cdot65/pan-os-duplicate-finder/network/members" target="_blank">
    <img src="https://img.shields.io/github/forks/cdot65/pan-os-duplicate-finder.svg?style=for-the-badge" alt="Forks">
</a>
<a href="https://github.com/cdot65/pan-os-duplicate-finder/stargazers" target="_blank">
    <img src="https://img.shields.io/github/stars/cdot65/pan-os-duplicate-finder.svg?style=for-the-badge" alt="Stars">
</a>
<a href="https://github.com/cdot65/pan-os-duplicate-finder/issues" target="_blank">
    <img src="https://img.shields.io/github/issues/cdot65/pan-os-duplicate-finder.svg?style=for-the-badge" alt="Issues">
</a>
<a href="https://github.com/cdot65/pan-os-duplicate-finder/blob/main/LICENSE" target="_blank">
    <img src="https://img.shields.io/github/license/cdot65/pan-os-duplicate-finder.svg?style=for-the-badge" alt="License">
</a>
</p>

---

**Documentation**: <a href="https://cdot65.github.io/pan-os-duplicate-finder/" target="_blank">https://cdot65.github.io/pan-os-duplicate-finder/</a>

**Source Code**: <a href="https://github.com/cdot65/pan-os-duplicate-finder" target="_blank">https://github.com/cdot65/pan-os-duplicate-finder</a>

---

`pan-os-duplicate-finder` is a command-line tool designed to identify duplicate address objects across Palo Alto Networks
device groups. It helps network administrators maintain cleaner configurations by finding redundant address objects that 
could be consolidated, enhancing efficiency and reducing potential inconsistencies.

## Key Features

- **Comprehensive Scanning**: Examines both shared space and all device groups for duplicates
- **User-Friendly CLI**: Built with [Typer](https://typer.tiangolo.com/) for an intuitive command-line experience
- **Secure Authentication**: Supports both direct credential input and settings file storage
- **Detailed Reporting**: Generates CSV reports with complete duplicate information
- **Rich Console Output**: Provides clear, colorized summaries and progress indicators

## Workflow

1. **Authentication**: Connect to your PAN-OS device using your credentials
2. **Discovery**: Automatically scan shared space and all device groups
3. **Analysis**: Identify duplicate address objects across locations
4. **Reporting**: Generate detailed CSV reports and console summaries

---

## Execution

`pan-os-duplicate-finder` can be executed using Python in a virtual environment:

<div class="termy">

<!-- termynal -->

```bash
$ pip install pan-os-duplicate-finder
$ pan-os-duplicate-finder --help
                                                                                                                                                                                                                                                        
 Usage: pan-os-duplicate-finder [OPTIONS] COMMAND [ARGS]...                                                                                                                                                                                                           
                                                                                                                                                                                                                                                        
 Find duplicate address objects across PAN-OS device groups.                                                                                                                                                                                   
                                                                                                                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                                                                                                              │
│ --show-completion            Show completion for the current shell, to copy it or customize the installation.                                                                                                                                       │
│ --help                       Show this message and exit.                                                                                                                                                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ find                     Find duplicate address objects across device groups                                                                                                                                                                        │
│ settings                 Create settings file for storing credentials and preferences                                                                                                                                                               │
│ version                  Show version information                                                                                                                                                                                                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

</div>

For more detailed usage instructions and examples, refer to the [User Guide](user-guide/getting-started.md).

---

## Example Usage

Find duplicates using settings file:
```bash
pan-os-duplicate-finder find
```

Or provide credentials directly:
```bash
pan-os-duplicate-finder find --hostname panorama.example.com --username admin
```

Generate a custom-named report:
```bash
pan-os-duplicate-finder find --output my-report.csv
```

Enable debug logging:
```bash
pan-os-duplicate-finder find --debug --log-file debug.log
```

---

## Contributing

Contributions are welcome and greatly appreciated. Visit the [Contributing](about/contributing.md) page for guidelines
on how to contribute.

## License

This project is licensed under the Apache 2.0 License - see the [License](about/license.md) page for details.