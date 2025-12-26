"""Allow running as: python -m test_2."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="test_2 CloudFormation template")
