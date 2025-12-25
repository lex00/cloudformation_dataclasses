"""Allow running as: python -m windows_2."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Template to install CloudWatchAgent on windows. It was validated on windows 2016")
