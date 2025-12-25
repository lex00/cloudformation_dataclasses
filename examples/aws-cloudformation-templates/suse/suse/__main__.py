"""Allow running as: python -m suse."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Template to install CloudWatchAgent on suse. It was validated on suse 12")
