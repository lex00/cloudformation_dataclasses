"""Allow running as: python -m apigateway_lambda_integration."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="apigateway_lambda_integration CloudFormation template")
