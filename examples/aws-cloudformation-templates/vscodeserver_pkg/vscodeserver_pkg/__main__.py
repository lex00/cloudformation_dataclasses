"""Allow running as: python -m vscodeserver_pkg."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="vscodeserver_pkg CloudFormation template")
