"""Allow running as: python -m vpcpeering_accepter_role_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template creates an assumable role to be used by the requester account to accept the VPC peering connection. (Accepter Account)")
