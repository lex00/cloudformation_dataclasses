"""Allow running as: python -m elbwithlockeddownautoscaledinstances."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template ELBWithLockedDownAutoScaledInstances: Create a load balanced, Auto Scaled sample website where the instances are locked down to only accept traffic from the load balancer. This example creates an Auto Scaling group behind a load balancer with a simple health check. The web site is available on port 80, however, the instances can be configured to listen on any port (8888 by default). **WARNING** This template creates one or more Amazon EC2 instances and an Elastic Load Balancer. You will be billed for the AWS resources used if you create a stack from this template.")
