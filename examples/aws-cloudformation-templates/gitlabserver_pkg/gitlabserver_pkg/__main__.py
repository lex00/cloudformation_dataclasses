"""Allow running as: python -m gitlabserver_pkg."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="gitlabserver_pkg CloudFormation template")
