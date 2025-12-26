"""Allow running as: python -m elbguidedautoscalingrollingupgrade."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template ELBGuidedAutoScalingRollingUpdates: This example creates an auto scaling group behind a load balancer with a simple health check. The Auto Scaling launch configuration includes an update policy that will keep 2 instances running while doing an autoscaling rolling update. The update will roll forward only when the ELB health check detects an updated instance in-service. **WARNING** This template creates one or more Amazon EC2  instances and an Elastic Load Balancer. You will be billed for the AWS resources used if you create a stack from this template.")
