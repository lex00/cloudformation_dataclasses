"""Allow running as: python -m efs_with_automount_to_ec2."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Multi-AZ EFS with automount EFS.")
