"""Allow running as: python -m date."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Template for date macro for Cloudformation. Provides functions for date manipulation in your CloudFormation templates including getting the current date, and doing date math. Written in Python.")
