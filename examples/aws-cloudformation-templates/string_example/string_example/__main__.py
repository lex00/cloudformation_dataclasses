"""Allow running as: python -m string_example."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="tests String macro functions")
