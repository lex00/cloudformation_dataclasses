"""Allow running as: python -m vpc_with_managed_nat_and_private_subnet."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Creates a VPC with Managed NAT, similar to the VPC Wizard at https://console.aws.amazon.com/vpc/home#wizardFullpagePublicAndPrivate: (extended from VPC_with_PublicIPs_And_DNS.template sample)")
