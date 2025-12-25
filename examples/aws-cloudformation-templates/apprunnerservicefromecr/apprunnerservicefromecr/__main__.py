"""Allow running as: python -m apprunnerservicefromecr."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template AppRunnerService: This template demonstrates the creation of a App Runner Service from existing ECR Repository.  **WARNING** This template creates an AWS App Runner Service. You will be billed for the AWS resources used if you create a stack from this template.")
