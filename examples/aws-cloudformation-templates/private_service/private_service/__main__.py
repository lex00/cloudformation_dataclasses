"""Allow running as: python -m private_service."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Deploy a service into an ECS cluster behind a private load balancer.")
