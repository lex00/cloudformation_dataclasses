"""Allow running as: python -m findinmapazs."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template deploys a VPC, with a pair of public and private subnets spread across two Availability Zones. It uses a static AZ Mapping known as RegionMap to ensure that your resources persist in a given Availability Zone if we add or remove zones")
