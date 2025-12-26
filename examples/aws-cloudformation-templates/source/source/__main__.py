"""Allow running as: python -m source."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Example of cross-account, same-region, S3 replication (v2) using server-side encryption with a customer-managed KMS key.  Create a symmetric KMS key with an alias, and a source S3 bucket with default encryption and versioning enabled. Create an IAM role, used by a replication rule, to provide access to the source and destination buckets and KMS keys.")
