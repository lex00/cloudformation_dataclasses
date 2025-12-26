"""Allow running as: python -m vpcpeering_accepter_main_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template accomplishes the following tasks: (1) applies a name tag to the specified VPC peering connection. (2) updates the specified route tables and security groups to allow communications via the VPC peering connection. Note, this is for the VPC Peering Accepter account.")
