"""
Placeholder tests to ensure the test suite runs correctly.
These will be replaced with real tests as we implement features.
"""

import hypertime


def test_imports() -> None:
    """Test that the hypertime package can be imported."""
    assert hypertime is not None


def test_version() -> None:
    """Test that version is defined."""
    assert hasattr(hypertime, "__version__")
    assert isinstance(hypertime.__version__, str)
    assert hypertime.__version__ == "0.1.0"


def test_package_attributes() -> None:
    """Test that package has expected attributes."""
    assert hasattr(hypertime, "__author__")
    assert hasattr(hypertime, "__license__")
    assert hypertime.__license__ == "MIT"


def test_with_fixture(sample_config: dict) -> None:
    """Test that fixtures work correctly."""
    assert isinstance(sample_config, dict)
    assert "dt" in sample_config
    assert sample_config["dt"] == 0.01
