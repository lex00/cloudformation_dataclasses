"""Allow running as: python -m tagging_root_volume."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template Tagging Root Volumes of EC2 Instances: This template shows how to automatically tag the root volume of the EC2 instances which are created through the CloudFormation template. This is done through the UserData property of the AWS::EC2::Instance resource. **WARNING** This template creates two Amazon EC2 instances and an IAM Role. You will be billed for the AWS resources used if you create a stack from this template.")
