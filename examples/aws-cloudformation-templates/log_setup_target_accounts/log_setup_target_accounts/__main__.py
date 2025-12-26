"""Allow running as: python -m log_setup_target_accounts."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="EventBridge Rule to send CloudFormation events to a central EventBus")
