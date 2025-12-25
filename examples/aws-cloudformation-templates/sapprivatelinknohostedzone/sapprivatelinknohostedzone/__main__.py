"""Allow running as: python -m sapprivatelinknohostedzone."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="CloudFormation template to create PrivateLink infrastructure")
