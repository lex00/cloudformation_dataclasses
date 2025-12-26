"""Allow running as: python -m fn_foreach_ddb."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Provision AWS Managed Active Directory\n")
