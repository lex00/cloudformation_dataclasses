"""Allow running as: python -m directoryservicesimplead."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="directoryservicesimplead CloudFormation template")
