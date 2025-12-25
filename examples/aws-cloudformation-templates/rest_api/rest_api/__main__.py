"""Allow running as: python -m rest_api."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="rest_api CloudFormation template")
