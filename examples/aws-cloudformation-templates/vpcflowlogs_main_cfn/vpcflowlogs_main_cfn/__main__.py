"""Allow running as: python -m vpcflowlogs_main_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template enables VPC Flow Logs to CloudWatch, S3, or both.")
