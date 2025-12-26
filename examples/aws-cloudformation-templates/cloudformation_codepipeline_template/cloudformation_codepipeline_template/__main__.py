"""Allow running as: python -m cloudformation_codepipeline_template."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="CodePipeline for continuous integration build and continuous deployment")
