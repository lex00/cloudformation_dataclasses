"""Allow running as: python -m cloudformation_codebuild_template."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Deploys the prequisites for creating required code pipelines this includes \n")
