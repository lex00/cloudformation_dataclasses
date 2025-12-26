"""Allow running as: python -m vpcpeering_requester_setup_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This templates creates a VPC Peering connection. (Requester Account)")
