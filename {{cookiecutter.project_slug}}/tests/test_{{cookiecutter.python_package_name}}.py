import pytest

def test_package_installed():
    # Test that the package is correctly installed
    try:
        import {{cookiecutter.python_package_name}}
    except ImportError:
        pytest.fail("Package not installed")
