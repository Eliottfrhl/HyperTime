"""
HyperTime: A flexible robotics and reinforcement learning simulation framework.

HyperTime provides a modular framework for creating, running, and training
intelligent agents in simulated robotic environments. It supports multiple
simulators, robots, and tasks with a unified interface.
"""

__version__ = "0.1.0"
__author__ = "Eliott Frohly"
__license__ = "MIT"

# Import core components for convenient access
# These will be implemented in later phases
# from hypertime.core.environment import Environment
# from hypertime.environments.registry import EnvironmentRegistry

# Convenience function that will be implemented later
# def make(env_name: str, **kwargs):
#     """Create an environment by name."""
#     return EnvironmentRegistry.make(env_name, **kwargs)

# def make_from_config(config_path: str):
#     """Create an environment from a config file."""
#     return EnvironmentRegistry.make_from_config(config_path)

__all__ = [
    "__version__",
    # "Environment",
    # "EnvironmentRegistry",
    # "make",
    # "make_from_config",
]
