"""Allow running as: python -m load_balancer."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This module creates an ELBv2 load balancer\n")
