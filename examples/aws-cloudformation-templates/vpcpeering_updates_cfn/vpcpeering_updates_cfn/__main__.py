"""Allow running as: python -m vpcpeering_updates_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template updates the specified route tables & security groups to allow communications via the VPC peering connection.")
