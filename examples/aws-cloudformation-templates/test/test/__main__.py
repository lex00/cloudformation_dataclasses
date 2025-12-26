"""Allow running as: python -m test."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="test CloudFormation template")
