"""Allow running as: python -m example_2."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="example_2 CloudFormation template")
