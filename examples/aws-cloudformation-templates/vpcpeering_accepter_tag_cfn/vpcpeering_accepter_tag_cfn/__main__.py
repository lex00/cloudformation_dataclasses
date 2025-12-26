"""Allow running as: python -m vpcpeering_accepter_tag_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template uses a custom resource Lambda to apply a Name tag to the VPC peering connection on the Accepter Account.")
