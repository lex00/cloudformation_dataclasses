"""Allow running as: python -m datetimenow."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="datetimenow CloudFormation template")
