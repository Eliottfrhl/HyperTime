# Installation

This guide will help you install HyperTime on your system.

## Prerequisites

Before installing HyperTime, ensure you have:

- **Python 3.9 or higher**
- **pip** (Python package installer)
- **Git** (for installing from source)

### Check Your Python Version

```bash
python --version
# or
python3 --version
```

If you need to install Python, visit [python.org](https://www.python.org/downloads/).

## Installation Methods

### Option 1: Install from PyPI (Recommended)

!!! warning "Not Yet Available"
    HyperTime is not yet published on PyPI. Currently, install from source (Option 2).

Once released, you'll be able to install via pip:

```bash
pip install hypertime
```

### Option 2: Install from Source

This is the current recommended method:

```bash
# Clone the repository
git clone https://github.com/yourusername/HyperTime.git
cd HyperTime

# Install with pip
pip install -e .

# Or with Poetry (recommended for development)
poetry install
```

## Installation Options

HyperTime has optional dependencies for different use cases:

### Basic Installation

Minimal installation with only core dependencies:

```bash
pip install hypertime
# or
poetry install
```

**Includes**: NumPy, PyYAML

### With Simulator Support

Install with physics simulator backends:

```bash
pip install hypertime[simulators]
# or
poetry install --extras simulators
```

**Adds**: PyBullet

### With RL Support

Install with reinforcement learning libraries:

```bash
pip install hypertime[rl]
# or
poetry install --extras rl
```

**Adds**: PyTorch, Gymnasium

### Full Installation

Install everything:

```bash
pip install hypertime[all]
# or
poetry install --extras all
```

**Includes**: All optional dependencies

## Verify Installation

After installation, verify that HyperTime is installed correctly:

```python
import hypertime as ht

print(ht.__version__)  # Should print: 0.1.0
```

Or run the test suite:

```bash
# If installed with Poetry
poetry run pytest

# If installed with pip
pytest
```

## Development Installation

If you want to contribute to HyperTime, follow these additional steps:

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/HyperTime.git
cd HyperTime
```

### 2. Install with Development Dependencies

```bash
poetry install --with dev,docs
```

This installs:
- Testing tools (pytest, pytest-cov)
- Code quality tools (black, isort, flake8, mypy)
- Documentation tools (mkdocs, mkdocs-material)

### 3. Install Pre-commit Hooks

```bash
poetry run pre-commit install
```

This ensures code is formatted automatically before each commit.

## Platform-Specific Notes

### Linux

Should work out of the box. If you encounter issues with PyBullet:

```bash
# Install OpenGL dependencies
sudo apt-get install python3-opengl
```

### macOS

Should work out of the box with Homebrew Python:

```bash
brew install python@3.11
```

### Windows

Install from the official Python installer. If you encounter issues:

1. Ensure you have Microsoft Visual C++ 14.0 or greater
2. Install from [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/)

## Troubleshooting

### Import Error: No module named 'hypertime'

Make sure you're in the correct virtual environment:

```bash
# With Poetry
poetry shell

# With venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### PyBullet Installation Issues

If PyBullet fails to install:

```bash
# Try installing separately
pip install pybullet --no-cache-dir
```

### Poetry Lock File Issues

If you encounter lock file conflicts:

```bash
poetry lock --no-update
poetry install
```

## Updating HyperTime

### From PyPI

```bash
pip install --upgrade hypertime
```

### From Source

```bash
cd HyperTime
git pull origin main
poetry install
```

## Uninstalling

To uninstall HyperTime:

```bash
pip uninstall hypertime
```

## Next Steps

Now that HyperTime is installed, continue to:

- [Quick Start Guide](quickstart.md) - Learn the basics
- [Core Concepts](concepts.md) - Understand the architecture
- [Examples](../examples/navigation.md) - See it in action

## Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section above
2. Search [existing issues](https://github.com/yourusername/HyperTime/issues)
3. Open a [new issue](https://github.com/yourusername/HyperTime/issues/new) with details about your problem
