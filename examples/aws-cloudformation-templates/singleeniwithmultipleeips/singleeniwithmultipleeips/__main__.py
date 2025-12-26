"""Allow running as: python -m singleeniwithmultipleeips."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Template Creates a single EC2 instance with a single ENI which has multiple private and public IPs")
