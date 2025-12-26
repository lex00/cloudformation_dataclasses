"""Allow running as: python -m macro_3."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="macro_3 CloudFormation template")
