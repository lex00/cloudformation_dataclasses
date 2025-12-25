"""Allow running as: python -m debian_2."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Template to install CloudWatchAgent on debian. It was validated on debian 12.0")
