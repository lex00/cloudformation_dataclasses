"""Allow running as: python -m instancewithcfninit."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation sample template.  \nCreate an Amazon EC2 instance with cfn-init and cfn-signal.\n")
