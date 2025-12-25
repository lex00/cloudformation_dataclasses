"""Allow running as: python -m ubuntu20_04_cfn_hup."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Installing Cloudformation helper scripts in Ubuntu 20.04 LTS")
