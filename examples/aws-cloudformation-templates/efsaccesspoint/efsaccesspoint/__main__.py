"""Allow running as: python -m efsaccesspoint."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Creates an EFS file system with three mount targets and one access point.")
