"""Allow running as: python -m ec2_instance_with_ephemeral_drives."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template EC2_Instance_With_Ephemeral_Drives: Example to show how to attach ephemeral drives using EC2 block device mappings. **WARNING** This template creates an Amazon EC2 instance. You will be billed for the AWS resources used if you create a stack from this template.")
