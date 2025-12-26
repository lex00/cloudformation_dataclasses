"""Allow running as: python -m public_service_1."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Deploy a service into an ECS cluster behind a public load balancer.")
