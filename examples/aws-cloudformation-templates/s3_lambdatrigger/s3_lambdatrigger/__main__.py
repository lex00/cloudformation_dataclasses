"""Allow running as: python -m s3_lambdatrigger."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="s3_lambdatrigger CloudFormation template")
