"""Allow running as: python -m rds_piops."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template RDS_PIOPS: Sample template showing how to create an Amazon RDS Database Instance with provisioned IOPs.**WARNING** This template creates an Amazon Relational Database Service database instance. You will be billed for the AWS resources used if you create a stack from this template.")
