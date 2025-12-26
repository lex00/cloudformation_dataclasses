"""Allow running as: python -m elb_access_logs_and_connection_draining."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template ELB_Access_Logs_And_Connection_Draining: Creates a load balanced, scalable sample website using Elastic Load Balancer attached to an Auto Scaling group. The ELB has connection draining enabled and also puts access logs into an S3 bucket. ** This template creates one or more Amazon EC2 instances. You will be billed for the AWS resources used if you create a stack from this template.")
