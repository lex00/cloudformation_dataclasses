"""Allow running as: python -m stackset_execution_role."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="StackSet execution role for target accounts")
