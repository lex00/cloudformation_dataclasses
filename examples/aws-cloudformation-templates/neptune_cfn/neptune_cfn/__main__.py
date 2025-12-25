"""Allow running as: python -m neptune_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation template to automatically provision AWS Neptune Graph Database through optimized CI/CD method with AWS CloudWatch and AWS SNS.")
