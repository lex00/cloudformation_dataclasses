"""Allow running as: python -m private_subnet_public_service."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Deploy a service on AWS Fargate, hosted in a private subnet, but accessible via a public load balancer.")
