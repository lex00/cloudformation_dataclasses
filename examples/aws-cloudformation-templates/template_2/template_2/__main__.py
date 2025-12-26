"""Allow running as: python -m template_2."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template EKS Cluster on EC2")
