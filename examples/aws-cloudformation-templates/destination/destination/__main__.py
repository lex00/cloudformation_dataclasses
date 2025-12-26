"""Allow running as: python -m destination."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Example of cross-account, same-region, S3 replication (v2) using server-side encryption with a customer-managed KMS key.  Create a symmetric KMS key with an alias, and a destination S3 bucket with default encryption and versioning enabled. Allow the source account access to the destination S3 bucket and KMS key for replication.")
