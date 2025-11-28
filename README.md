# HyperTime

[![CI](https://github.com/Eliottfrhl/HyperTime/actions/workflows/ci.yml/badge.svg)](https://github.com/Eliottfrhl/HyperTime/actions/workflows/ci.yml)
[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue)](https://Eliottfrhl.github.io/HyperTime/)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A flexible and modular robotics and reinforcement learning simulation framework.

## 🎯 Overview

HyperTime provides a unified interface for creating, running, and training intelligent agents in simulated robotic environments. It allows you to:

- 🤖 Mix and match different robots (mobile robots, robotic arms, grippers)
- 🌍 Use multiple simulator backends (PyBullet, MuJoCo, or simple custom simulators)
- 🎯 Define custom tasks (navigation, manipulation, reaching, etc.)
- 🧠 Train agents using reinforcement learning
- ⚡ Run parallel simulations for faster training
- ⚙️ Configure everything through simple YAML files

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/HyperTime.git
cd HyperTime

# Install with Poetry (basic installation)
poetry install

# Install with simulator support
poetry install --extras simulators

# Install with RL support
poetry install --extras rl

# Install everything
poetry install --extras all
```

### Basic Usage

```python
import hypertime as ht

# Create an environment (coming soon in Phase 2!)
# env = ht.make('mobile-nav-v0')

# Or from a config file
# env = ht.make_from_config('configs/scenarios/navigation.yaml')

# Run the environment
# obs = env.reset()
# for _ in range(1000):
#     action = env.action_space.sample()
#     obs, reward, done, info = env.step(action)
#     if done:
#         break
```

## 📚 Documentation

Full documentation is available at [https://yourusername.github.io/HyperTime/](https://yourusername.github.io/HyperTime/)

## 🏗️ Project Status

HyperTime is currently in **early development** (Phase 1: Project Setup).

### Roadmap

- [x] Phase 1: Project setup and infrastructure
- [ ] Phase 2: Core abstractions and basic components
- [ ] Phase 3: Simulator integration (PyBullet, MuJoCo)
- [ ] Phase 4: Reinforcement learning integration
- [ ] Phase 5: Parallel training support
- [ ] Phase 6: Configuration system and usability improvements

## 🛠️ Development

### Setup Development Environment

```bash
# Install all dependencies including dev tools
poetry install

# Install pre-commit hooks (optional)
poetry run pre-commit install

# Run tests
poetry run pytest

# Run linting
poetry run black hypertime tests
poetry run isort hypertime tests
poetry run flake8 hypertime tests
poetry run mypy hypertime
```

### Running Tests

```bash
# Run all tests
poetry run pytest -v

# Run with coverage
poetry run pytest --cov=hypertime --cov-report=html

# Run specific test file
poetry run pytest tests/unit/test_placeholder.py -v
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by OpenAI Gym/Gymnasium
- Built with PyBullet and MuJoCo for physics simulation
- Uses Stable-Baselines3 for RL algorithms

## 📧 Contact

- GitHub: [@yourusername](https://github.com/yourusername)
- Issues: [GitHub Issues](https://github.com/yourusername/HyperTime/issues)

---

**Note**: This project is under active development. APIs may change as we iterate towards v1.0.
