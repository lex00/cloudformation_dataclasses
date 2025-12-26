"""Allow running as: python -m rhel9_cfn_hup."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Installing Cloudformation helper scripts in RHEL 9")
