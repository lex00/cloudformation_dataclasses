"""Allow running as: python -m public_vpc_1."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="A stack for deploying containerized applications onto a cluster of EC2 hosts using Elastic Container Service. This stack runs containers on hosts that are in a public VPC subnet, and includes a public facing load balancer to register the services in.")
