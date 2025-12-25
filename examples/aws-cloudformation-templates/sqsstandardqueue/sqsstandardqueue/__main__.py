"""Allow running as: python -m sqsstandardqueue."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Best Practice SQS Standard Queue")
