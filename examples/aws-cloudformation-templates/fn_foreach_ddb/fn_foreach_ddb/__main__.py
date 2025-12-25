"""Allow running as: python -m fn_foreach_ddb."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This CloudFormation sample template DMSAuroraToS3FullLoadAndOngoingReplication creates an Aurora RDS instance and DMS instance in a VPC, and an S3 bucket. The Aurora RDS instance is configured as the DMS Source Endpoint and the S3 bucket is configured as the DMS Target Endpoint. A DMS task is created and configured to migrate existing data and replicate ongoing changes from the source endpoint to the target endpoint. You will be billed for the AWS resources used if you create a stack from this template.")
