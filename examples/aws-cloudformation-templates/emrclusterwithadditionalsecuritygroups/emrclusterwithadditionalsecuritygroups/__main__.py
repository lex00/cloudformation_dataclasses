"""Allow running as: python -m emrclusterwithadditionalsecuritygroups."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Best Practice EMR Cluster for Spark or S3 backed Hbase")
