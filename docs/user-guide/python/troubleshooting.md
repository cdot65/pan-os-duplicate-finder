# Troubleshooting Guide

If you encounter issues while using `pan-os-duplicate-finder`, this guide provides solutions to common problems.

## Common Issues and Solutions

### 1. Authentication Failures

**Problem:** Error authenticating with Panorama or firewall.

**Solution:**
- Verify your credentials in `settings.yaml` are correct
- Ensure you have API access enabled on the device
- Check for any typos in hostname/IP address
- Verify the user account has sufficient privileges

Example debug command:

```bash
pan-os-duplicate-finder find --debug --log-file auth-debug.log
```

### 2. Network Connectivity Issues

**Problem:** Unable to connect to PAN-OS device.

**Solution:**
- Verify network connectivity to the device
  ```bash
  ping <device-ip>
  ```
- Check for firewalls blocking HTTPS (TCP/443)
- Ensure SSL/TLS verification isn't causing issues
- Verify DNS resolution if using hostnames

### 3. Device Group Access

**Problem:** Unable to retrieve address objects from certain device groups.

**Solution:**
- Verify the user has access to all device groups
- Check device group names for any special characters
- Enable debug logging to see which groups are accessible:
  ```bash
  pan-os-duplicate-finder find --debug --log-file dg-debug.log
  ```

### 4. Performance Issues

**Problem:** Script runs slowly or times out.

**Solution:**
- Large configurations may take longer to process
- Consider running during maintenance windows
- Check network latency to the device
- Monitor device CPU usage during execution

### 5. CSV Output Issues

**Problem:** CSV file is incomplete or malformed.

**Solution:**
- Ensure write permissions in output directory
- Check for disk space
- Verify file isn't locked by another process
- Try specifying a different output location:
  ```bash
  pan-os-duplicate-finder find --output /different/path/output.csv
  ```

## Logging and Debugging

### Enable Debug Logging

For detailed troubleshooting:

```bash
pan-os-duplicate-finder find --debug --log-file debug.log
```

### Log Levels
- INFO: Normal operation messages
- DEBUG: Detailed information for troubleshooting
- WARNING: Issues that don't stop execution
- ERROR: Critical problems that halt execution

### Common Log Messages

1. "Unable to connect to device":
   - Check network connectivity
   - Verify hostname/IP is correct
   - Confirm port 443 is accessible

2. "API authentication failed":
   - Verify credentials
   - Check API access is enabled
   - Confirm user permissions

3. "Error processing device group":
   - Check user access to device group
   - Verify device group exists
   - Look for configuration issues

## Best Practices

1. **Always Start with Debug Mode During Setup**:
   ```bash
   pan-os-duplicate-finder find --debug --log-file setup.log
   ```

2. **Test Connectivity First**:
   ```bash
   pan-os-duplicate-finder version
   ```

3. **Verify Settings File**:
   ```bash
   pan-os-duplicate-finder settings
   ```

4. **Regular Testing**:
   - Run with smaller scope first
   - Gradually include more device groups
   - Monitor performance patterns

## Getting Help

If you're unable to resolve an issue:

1. Enable debug logging
2. Capture the full error message
3. Note your environment details:
   - Python version
   - PAN-OS version
   - Network configuration
4. Open an issue on our [GitHub repository](https://github.com/cdot65/pan-os-duplicate-finder/issues) with these details

For urgent issues or sensitive information, consider reaching out to support directly.

## Common Error Messages

| Error Message            | Likely Cause                           | Solution                            |
|--------------------------|----------------------------------------|-------------------------------------|
| "Connection refused"     | Network connectivity or firewall rules | Check network access and firewalls  |
| "Invalid credentials"    | Authentication failure                 | Verify username/password or API key |
| "Permission denied"      | Insufficient privileges                | Check user permissions              |
| "Device group not found" | Invalid device group                   | Verify device group exists          |
| "XML parsing error"      | Malformed configuration                | Check device configuration          |

Remember to always check the logs for detailed error messages and stack traces when troubleshooting.