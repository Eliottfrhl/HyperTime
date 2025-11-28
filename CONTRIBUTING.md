# Contributing to HyperTime

First off, thank you for considering contributing to HyperTime! It's people like you that make HyperTime such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our commitment to providing a welcoming and inclusive environment. Be respectful, professional, and constructive in all interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code snippets, config files)
- **Describe the behavior you observed and what you expected**
- **Include your environment details** (OS, Python version, HyperTime version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other projects** if applicable

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes
4. Make sure your code follows the existing style
5. Write a clear commit message

## Development Setup

### 1. Clone and Install

```bash
# Fork and clone the repository
git clone https://github.com/Eliottfrhl/HyperTime.git
cd HyperTime

# Install dependencies
poetry install

# Install with all extras for development
poetry install --extras all
```

### 2. Install Pre-commit Hooks (Optional but Recommended)

```bash
poetry run pre-commit install
```

This will automatically run code formatters before each commit.

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## Code Style

We use several tools to maintain code quality:

### Running Code Formatters

```bash
# Format code with black
poetry run black hypertime tests

# Sort imports with isort
poetry run isort hypertime tests

# Check style with flake8
poetry run flake8 hypertime tests

# Type check with mypy
poetry run mypy hypertime
```

### Style Guidelines

- **Line length**: 88 characters (black's default)
- **Imports**: Sorted with isort (compatible with black)
- **Type hints**: Use type hints for all function signatures
- **Docstrings**: Use Google-style docstrings

Example:

```python
def create_environment(robot: Robot, task: Task, config: Dict[str, Any]) -> Environment:
    """Create a new environment instance.

    Args:
        robot: The robot to use in the environment.
        task: The task definition.
        config: Configuration dictionary.

    Returns:
        A configured Environment instance.

    Raises:
        ValueError: If configuration is invalid.
    """
    pass
```

## Testing

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=hypertime --cov-report=html

# Run specific test file
poetry run pytest tests/unit/test_core.py -v

# Run tests matching a pattern
poetry run pytest -k "test_environment"
```

### Writing Tests

- Place unit tests in `tests/unit/`
- Place integration tests in `tests/integration/`
- Use fixtures from `tests/conftest.py`
- Aim for high test coverage (>80%)

Example test:

```python
def test_environment_reset(mock_robot, mock_simulator, mock_task):
    """Test that environment resets correctly."""
    env = Environment(mock_robot, mock_simulator, mock_task, {})
    obs = env.reset()

    assert obs is not None
    assert env._step_count == 0
```

## Documentation

### Building Documentation Locally

```bash
# Serve documentation locally with live reload
poetry run mkdocs serve

# Build documentation
poetry run mkdocs build
```

Then visit `http://127.0.0.1:8000/`

### Writing Documentation

- Place documentation in the `docs/` directory
- Use Markdown format
- Include code examples where appropriate
- Update the navigation in `mkdocs.yml` if adding new pages

## Project Structure

```
hypertime/
├── hypertime/          # Main package
│   ├── core/          # Core abstractions
│   ├── robots/        # Robot implementations
│   ├── simulators/    # Simulator backends
│   ├── tasks/         # Task definitions
│   └── ...
├── tests/             # Test suite
├── docs/              # Documentation
├── configs/           # Example configurations
└── examples/          # Usage examples
```

## Commit Messages

Write clear, descriptive commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests after the first line

Example:
```
Add PyBullet simulator implementation

- Implement PyBulletSimulator class
- Add URDF loading support
- Include basic collision detection
- Add tests for simulator initialization

Closes #42
```

## Release Process

(For maintainers)

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create a git tag: `git tag -a v0.2.0 -m "Release v0.2.0"`
4. Push tag: `git push origin v0.2.0`
5. GitHub Actions will handle the rest

## Questions?

Feel free to open an issue with the `question` label or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
