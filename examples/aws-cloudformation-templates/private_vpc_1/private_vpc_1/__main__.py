"""Allow running as: python -m private_vpc_1."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="A stack for deploying containerized applications onto a cluster of EC2 hosts using Elastic Container Service. This stack runs containers on hosts that are in a private VPC subnet. Outbound network traffic from the hosts must go out through a NAT gateway. There are two load balancers, one inside the public subnet, which can be used to send traffic to the containers in the private subnet, and one in the private subnet, which can be used for private internal traffic between internal services.")
