"""Allow running as: python -m public_service_2."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Deploy a service on AWS Fargate, hosted in a public subnet, and accessible via a public load balancer.")
