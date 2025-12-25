"""Allow running as: python -m dynamodb_secondary_indexes."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template DynamoDB_Secondary_Indexes: Create a DynamoDB table with local and global secondary indexes. **WARNING** This template creates an Amazon DynamoDB table. You will be billed for the AWS resources used if you create a stack from this template.")
