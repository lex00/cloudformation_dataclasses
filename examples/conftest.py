"""Pytest configuration for examples tests.

Clears the registry and reloads the example module before each test to ensure
proper isolation when using Template.from_registry().
"""

import importlib
import sys

import pytest

from cloudformation_dataclasses.core import registry


@pytest.fixture(autouse=True)
def isolate_registry(request):
    """Clear registry and reload example module before each test.

    When using Template.from_registry(), the registry must contain the
    resources from the example being tested. This fixture:
    1. Clears the registry
    2. Reloads the example module to re-register its resources
    """
    registry.clear()

    # Find the example module being tested (parent of tests/ directory)
    test_module = request.module.__name__
    # e.g., "examples.generated.aws_cloudformation_templates.S3.compliant_bucket.tests.test_compliant_bucket"
    # -> "examples.generated.aws_cloudformation_templates.S3.compliant_bucket"
    parts = test_module.split(".")
    if "tests" in parts:
        tests_idx = parts.index("tests")
        example_package = ".".join(parts[:tests_idx])

        # Find and reload all modules in that example package
        modules_to_reload = [
            name for name in list(sys.modules.keys())
            if name.startswith(example_package) and "tests" not in name
        ]

        for mod_name in modules_to_reload:
            if mod_name in sys.modules:
                importlib.reload(sys.modules[mod_name])

    yield
