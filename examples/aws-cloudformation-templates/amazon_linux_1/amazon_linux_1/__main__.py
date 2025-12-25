"""Allow running as: python -m amazon_linux_1."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Template to install CloudWatchAgent on amazon linux. It was validated on amazon linux 2")
