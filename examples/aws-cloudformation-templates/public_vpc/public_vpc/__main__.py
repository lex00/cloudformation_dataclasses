"""Allow running as: python -m public_vpc."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="A stack for deploying containerized applications in AWS Fargate. This stack runs containers in a public VPC subnet, and includes a public facing load balancer to register the services in.")
