"""Allow running as: python -m python."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Macro allowing you to run arbitrary Python code in your CloudFormation templates")
