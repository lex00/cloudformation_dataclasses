"""Allow running as: python -m example."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="example CloudFormation template")
