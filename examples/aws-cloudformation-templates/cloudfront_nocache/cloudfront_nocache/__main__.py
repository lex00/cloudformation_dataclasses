"""Allow running as: python -m cloudfront_nocache."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="cloudfront_nocache CloudFormation template")
