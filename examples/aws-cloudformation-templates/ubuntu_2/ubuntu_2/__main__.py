"""Allow running as: python -m ubuntu_2."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Template to install CloudWatchAgent on ubuntu. It was validated on ubuntu 22.04")
