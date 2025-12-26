"""Allow running as: python -m string."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="string CloudFormation template")
