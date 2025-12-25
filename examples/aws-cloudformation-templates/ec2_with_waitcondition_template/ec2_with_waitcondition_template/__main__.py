"""Allow running as: python -m ec2_with_waitcondition_template."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Create a variable number of EC2 instance resources.")
