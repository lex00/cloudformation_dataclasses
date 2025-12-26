"""Allow running as: python -m networkloadbalancerwitheips."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Template creates a Network Load Balancer in 2 AZs with EIPs listening on TCP port 80. There are no registered targets these would either be EC2 instance IDs added to the targets property of the target group  or defined under the autoscaling group resources  ")
