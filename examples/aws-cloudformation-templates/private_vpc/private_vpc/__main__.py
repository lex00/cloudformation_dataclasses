"""Allow running as: python -m private_vpc."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This stack deploys a Fargate cluster that is in a VPC with both public and private subnets. Containers can be deployed into either the public subnets or the private subnets, and there are two load balancers. One is inside the public subnet, which can be used to send traffic to the containers in the private subnet, and one in the private subnet, which can be used for private internal traffic between internal services.")
