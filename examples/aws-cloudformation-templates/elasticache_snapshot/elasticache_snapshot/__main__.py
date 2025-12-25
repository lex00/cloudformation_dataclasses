"""Allow running as: python -m elasticache_snapshot."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Create a VPC containing two subnets and an auto scaling group containing instances with Internet access.")
