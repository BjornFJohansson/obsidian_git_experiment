# Contributing to Obsidian-GitHub Wiki Sync

Thanks for your interest in contributing! This project helps bridge Obsidian and GitHub Wiki, and we welcome all kinds of contributions.

## How You Can Help

### 🐛 Report Issues
Found a bug or have an idea? Just create an issue! Include:
- What you were trying to do
- What happened instead
- Your operating system (Windows/Mac/Linux)

### 💡 Suggest Improvements
Have ideas for making this better? We'd love to hear them! Some areas we're thinking about:
- Better error messages
- Support for more Obsidian features
- Performance improvements
- Documentation improvements

### 🔧 Code Contributions
Want to help with code? Great! Here's how:

1. **Fork** this repository
2. **Clone** your fork to your computer
3. **Set up development environment** (see Development Setup below)
4. **Make changes** in a new branch
5. **Test** your changes (see Testing Guide below)
6. **Submit** a pull request!

#### Development Setup
The project consists of two main components:
- `post-commit`: The main git hook script that handles the sync workflow
- `transformations.py`: A modular Python module containing the text transformation functions

For development work on transformations:
1. Set up a Python virtual environment:
   ```bash
   python -m venv test-env
   source test-env/bin/activate
   ```
2. Install testing dependencies:
   ```bash
   pip install pytest
   ```

#### Testing Guide
This project includes a comprehensive test suite using pytest. **Please run tests before submitting changes.**

**Running Tests:**
```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_transformations.py -v

# Run tests with detailed output
python -m pytest tests/ -v -s
```

**Test Structure:**
- `tests/test_transformations.py`: Tests for all transformation functions
- Tests cover page links, header links, image links, and edge cases
- Manual testing guide available for end-to-end workflow testing

**What to Test:**
- All transformation functions work correctly
- Edge cases are handled properly
- No regression in existing functionality
- New features have corresponding tests

**Writing New Tests:**
If you add new transformation logic, please include tests that cover:
- Basic functionality
- Edge cases
- Integration with existing transformations

#### End-to-End Testing Guide
For testing the complete git hook workflow:
1. Set up a test repository with a GitHub Wiki
2. Copy the `post-commit` and `transformations.py` scripts to `.git/hooks/`
3. Create the required branches (`ob_to_gh`, `obsidian`)
4. Switch to the `obsidian` branch
5. Make some changes to Obsidian markdown files and commit
6. Verify transformations work correctly on the `master` branch

#### Code Style and Structure
- Keep transformation functions focused and single-purpose
- Use clear, descriptive function names
- Add docstrings for new functions
- Maintain the existing regex pattern style
- Consider edge cases in all new code

### 📚 Documentation
Help improve the docs by:
- Clarifying unclear instructions
- Adding troubleshooting tips
- Creating simple tutorials
- Translating to other languages

### 🧪 Testing
We need help testing on:
- Different operating systems
- Various Obsidian plugins
- Large repositories
- Edge cases (special characters, complex nested links, etc.)
- Performance with large vault files
- Integration with different Git workflows

**Testing Areas:**
- **Transformation Functions**: Verify regex patterns work correctly
- **Git Hook Integration**: Test the complete sync workflow
- **Error Handling**: Test behavior with malformed markdown
- **Performance**: Test with large files and many links

## Getting Started

- Check the [README.md](README.md) for basic usage
- Look at existing issues for ideas
- Don't worry about being perfect - we're all learning :)

## Questions?

Feel free to create an issue if you have questions or need help getting started. We're here to help!

## License

By contributing, you agree that your contributions will be licensed under the same [BSD 3-Clause License](LICENSE) as the project. 