"""Allow running as: python -m cloudfront_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Installing Cloudformation helper scripts in Ubuntu 20.04 LTS")
