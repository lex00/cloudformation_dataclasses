"""Allow running as: python -m bandit."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template AutoScalingScheduledAction: Create a load balanced, Auto Scaled sample website. This example creates an Auto Scaling group with time-based scheduled actions behind a load balancer with a simple health check. **WARNING** This template creates one or more Amazon EC2 instances and an Elastic Load Balancer. You will be billed for the AWS resources used if you create a stack from this template.")
