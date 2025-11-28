"""
Shared pytest fixtures and configuration for all tests.
"""

from typing import Any, Dict

import numpy as np
import pytest


@pytest.fixture
def sample_config() -> Dict[str, Any]:
    """Sample configuration for testing."""
    return {
        "dt": 0.01,
        "max_steps": 1000,
        "render": False,
    }


@pytest.fixture
def random_seed() -> int:
    """Fixed random seed for reproducible tests."""
    return 42


@pytest.fixture
def sample_observation() -> np.ndarray:
    """Sample observation array for testing."""
    np.random.seed(42)
    return np.random.randn(10)


@pytest.fixture
def sample_action() -> np.ndarray:
    """Sample action array for testing."""
    np.random.seed(42)
    return np.random.randn(2)


# Additional fixtures will be added as we implement more features
# For example:
# - mock_robot
# - mock_simulator
# - mock_task
# - mock_environment
