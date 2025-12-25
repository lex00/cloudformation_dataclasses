"""Allow running as: python -m example_3."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="example_3 CloudFormation template")
