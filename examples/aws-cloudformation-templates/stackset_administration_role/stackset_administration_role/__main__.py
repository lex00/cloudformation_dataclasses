"""Allow running as: python -m stackset_administration_role."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="StackSet administration role for management account")
