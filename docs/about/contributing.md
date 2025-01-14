# Contributing to `pan-os-duplicate-finder`

We're excited that you're interested in contributing to the `pan-os-duplicate-finder` project! This tool helps network administrators identify and manage duplicate address objects across PAN-OS device groups, and your contributions can make it even better.

---

## Getting Started

Before you begin, please ensure you have a GitHub account and are familiar with Git and GitHub workflows. If you're new to these tools, check out [GitHub's Help pages](https://help.github.com).

### Setting Up Your Environment

1. **Fork the Repository:**
   Start by forking the [pan-os-duplicate-finder repository](https://github.com/cdot65/pan-os-duplicate-finder) on GitHub.

2. **Clone Your Fork:**
   Clone your fork to your local machine:

   <div class="termy">
   ```bash
   $ git clone https://github.com/cdot65/pan-os-duplicate-finder.git
   $ cd pan-os-duplicate-finder
   ```
   </div>

3. **Create a Branch:**
   Create a new branch for your feature or fix:

   <div class="termy">
   ```bash
   $ git checkout -b feature/YourFeatureName
   ```
   </div>

4. **Set Up the Development Environment:**
   ```bash
   # Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install development dependencies
   poetry install
   ```

---

## Making Changes

1. **Code Style:**
   - We use Black for code formatting
   - Follow PEP 8 guidelines
   - Use type hints where possible
   - Add docstrings to functions and classes

2. **Testing:**
   - Add tests for new functionality
   - Ensure existing tests pass
   - Run tests using pytest:
     ```bash
     poetry run pytest
     ```

3. **Documentation:**
   - Update documentation for any changed functionality
   - Add docstrings to new functions and classes
   - Update the README.md if needed

4. **Commit Your Changes:**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

---

## Submitting a Pull Request

1. **Push Changes:**
   ```bash
   git push origin feature/YourFeatureName
   ```

2. **Create Pull Request:**
   - Go to GitHub and create a new pull request
   - Provide a clear description of your changes
   - Reference any related issues
   - Wait for review from maintainers

3. **Code Review:**
   - Be responsive to feedback
   - Make requested changes if needed
   - Keep the discussion constructive

---

## Development Guidelines

### Code Organization

```bash
pan_os_duplicate_finder/
├── commands/          # CLI commands
├── utilities/         # Shared utilities
└── tests/            # Test files
```

### Testing
- Write unit tests for new functionality
- Use pytest for testing
- Maintain test coverage

### Documentation
- Keep docs up-to-date
- Use clear, concise language
- Include examples where helpful

---

## Questions or Need Help?

- Open an issue on GitHub
- Provide detailed information about your problem
- Be patient and respectful

Thank you for contributing to make `pan-os-duplicate-finder` better!