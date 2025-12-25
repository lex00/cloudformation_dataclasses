"""Allow running as: python -m redhat_1."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Template to install CloudWatchAgent on redhat. It was validated on redhat 7.5")
