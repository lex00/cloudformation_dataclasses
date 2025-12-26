"""Allow running as: python -m snstopic."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Best Practice SNS Topic")
