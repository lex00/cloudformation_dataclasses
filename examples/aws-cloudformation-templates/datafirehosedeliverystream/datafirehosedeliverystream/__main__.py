"""Allow running as: python -m datafirehosedeliverystream."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Create an Amazon Data Firehose stream with server-side encryption set using AWS Managed keys and destination error logging enabled to a created Amazon CloudWatch log group and log stream.")
