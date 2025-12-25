"""Allow running as: python -m vpcflowlogss3_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template enables VPC Flow Logs to S3. An option is provided to create an Amazon S3 bucket with encryption to host the flow logs.")
