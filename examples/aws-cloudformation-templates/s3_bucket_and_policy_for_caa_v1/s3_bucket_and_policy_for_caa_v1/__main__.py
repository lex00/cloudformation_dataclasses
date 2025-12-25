"""Allow running as: python -m s3_bucket_and_policy_for_caa_v1."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template: Sample template which will create an s3 bucket with a bucket policy to enable cross account acccess. The template requires you to provide an AWS account ID to provide cross account access to, and a globally unique name for an s3 bucket.")
