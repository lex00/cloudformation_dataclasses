"""Allow running as: python -m common_resources_stackset_pkg."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template contains a stack set that deploys common-resource.yaml to target accounts")
