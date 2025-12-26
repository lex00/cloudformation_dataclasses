"""Allow running as: python -m vpc_ec2_instance_with_multiple_static_ipaddresses."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Sample template showing how to create an instance with a single network\ninterface and multiple static IP addresses in an existing VPC. It assumes you\nhave already created a VPC.  **WARNING** This template creates an Amazon EC2\ninstance. You will be billed for the AWS resources used if you create a stack\nfrom this template.\n")
