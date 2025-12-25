"""Allow running as: python -m cognito_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This module creates a simple Cognito User Pool, Domain, and App Client.")
