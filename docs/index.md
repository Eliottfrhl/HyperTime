# Welcome to HyperTime

<div align="center">
  <strong>A flexible and modular robotics and reinforcement learning simulation framework</strong>
</div>

---

## 🎯 What is HyperTime?

HyperTime is a Python framework that makes it easy to create, run, and train intelligent agents in simulated robotic environments. It provides a unified interface that lets you mix and match different robots, tasks, and simulation backends without rewriting code.

## ✨ Key Features

- **🤖 Modular Robot Support**: Use mobile robots, robotic arms, grippers, or create your own
- **🌍 Multiple Simulators**: Switch between PyBullet, MuJoCo, or simple custom simulators
- **🎯 Flexible Tasks**: Define navigation, manipulation, or custom objectives
- **🧠 RL Integration**: Train agents with popular reinforcement learning algorithms
- **⚡ Parallel Training**: Speed up training with vectorized environments
- **⚙️ Configuration-Driven**: Set up experiments with simple YAML files
- **📊 Visualization**: Built-in tools for rendering and metrics

## 🚀 Quick Start

### Installation

```bash
# Basic installation
pip install hypertime

# Or with Poetry
poetry add hypertime

# Install with extras
pip install hypertime[simulators,rl]
```

### Basic Usage

```python
import hypertime as ht

# Create an environment
env = ht.make('mobile-nav-v0')

# Run a simple loop
obs = env.reset()
for _ in range(1000):
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    if done:
        break
```

### From Configuration

```python
import hypertime as ht

# Load from YAML config
env = ht.make_from_config('configs/scenarios/navigation.yaml')

# Train an agent
agent = ht.rl.PPO(env)
agent.train(total_steps=100_000)
```

## 📚 Documentation Structure

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } __Getting Started__

    ---

    New to HyperTime? Start here to learn the basics.

    [:octicons-arrow-right-24: Installation](getting-started/installation.md)
    [:octicons-arrow-right-24: Quick Start](getting-started/quickstart.md)
    [:octicons-arrow-right-24: Core Concepts](getting-started/concepts.md)

-   :material-book-open-variant:{ .lg .middle } __User Guide__

    ---

    Learn how to use HyperTime's features in depth.

    [:octicons-arrow-right-24: Environments](user-guide/environments.md)
    [:octicons-arrow-right-24: Robots](user-guide/robots.md)
    [:octicons-arrow-right-24: Training](user-guide/training.md)

-   :material-code-braces:{ .lg .middle } __API Reference__

    ---

    Detailed documentation of all classes and functions.

    [:octicons-arrow-right-24: Core API](api/core.md)
    [:octicons-arrow-right-24: Robots API](api/robots.md)
    [:octicons-arrow-right-24: RL API](api/rl.md)

-   :material-flask:{ .lg .middle } __Examples__

    ---

    Practical examples to get you started quickly.

    [:octicons-arrow-right-24: Navigation](examples/navigation.md)
    [:octicons-arrow-right-24: Manipulation](examples/manipulation.md)
    [:octicons-arrow-right-24: Parallel Training](examples/parallel.md)

</div>

## 🏗️ Design Philosophy

HyperTime is built on several key principles:

1. **Composition over Inheritance**: Mix and match components freely
2. **Minimal Dependencies**: Core functionality requires only NumPy
3. **Extensibility**: Easy to add new robots, tasks, or simulators
4. **Type Safety**: Comprehensive type hints throughout
5. **Testing**: High test coverage ensures reliability

## 🗺️ Project Roadmap

- [x] **Phase 1**: Project setup and infrastructure *(Current)*
- [ ] **Phase 2**: Core abstractions and basic components
- [ ] **Phase 3**: Simulator integration (PyBullet, MuJoCo)
- [ ] **Phase 4**: Reinforcement learning integration
- [ ] **Phase 5**: Parallel training support
- [ ] **Phase 6**: Configuration system and usability

## 🤝 Contributing

We welcome contributions! Whether it's:

- 🐛 Reporting bugs
- 💡 Suggesting features
- 📝 Improving documentation
- 🔧 Submitting pull requests

Check out our [Contributing Guide](contributing.md) to get started.

## 📄 License

HyperTime is released under the [MIT License](https://opensource.org/licenses/MIT).

## 🙏 Acknowledgments

HyperTime is inspired by and builds upon:

- [OpenAI Gym](https://github.com/openai/gym) / [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) - Standard RL interface
- [PyBullet](https://pybullet.org/) - Fast physics simulation
- [MuJoCo](https://mujoco.org/) - Advanced physics engine
- [Stable-Baselines3](https://stable-baselines3.readthedocs.io/) - RL algorithms

## 📧 Support

- 📖 [Documentation](https://yourusername.github.io/HyperTime/)
- 🐛 [Issue Tracker](https://github.com/yourusername/HyperTime/issues)
- 💬 [Discussions](https://github.com/yourusername/HyperTime/discussions)

---

<div align="center">
  <sub>Built with ❤️ by the HyperTime community</sub>
</div>
