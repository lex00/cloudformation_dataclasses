"""Allow running as: python -m log_setup_management_pkg."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="A central event bus rule and log group to collect CloudFormation logs from all target accounts")
