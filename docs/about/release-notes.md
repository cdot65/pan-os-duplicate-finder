# Release Notes

Welcome to the release notes for the `pan-os-duplicate-finder` tool. This document provides a detailed record of changes, enhancements, and fixes in each version of the tool.

---

## Version 0.1.0

**Release Date:** January 14, 2025

### Initial Release
- **Core Features**:
  - Find duplicate address objects across PAN-OS device groups
  - Support for shared and device group configurations
  - CSV report generation
  - Rich console output with detailed summaries

- **Authentication**:
  - Support for direct credential input
  - Settings file for storing credentials
  - API key generation and management

- **Analysis Features**:
  - Detection of ip-netmask duplicates
  - Detection of ip-range duplicates
  - Detection of FQDN duplicates
  - Cross-device-group analysis
  - Detailed reporting of duplicate locations

- **Output Options**:
  - CSV report generation
  - Console summary tables
  - Logging with configurable levels
  - Debug mode for troubleshooting

- **CLI Improvements**:
  - Typer-based command interface
  - Interactive prompts for missing credentials
  - Rich console output with status indicators
  - Progress tracking during analysis

For detailed information about each release, visit our [GitHub repository](https://github.com/cdot65/pan-os-duplicate-finder) or check the [commit history](https://github.com/cdot65/pan-os-duplicate-finder/commits/main).