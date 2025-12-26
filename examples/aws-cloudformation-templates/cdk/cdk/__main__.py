"""Allow running as: python -m cdk."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="StackSet execution role for target accounts")
