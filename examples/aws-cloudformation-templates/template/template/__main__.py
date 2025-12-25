"""Allow running as: python -m template."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Template for Lambda Sample.")
