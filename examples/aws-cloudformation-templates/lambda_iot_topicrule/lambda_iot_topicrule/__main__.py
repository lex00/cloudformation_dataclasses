"""Allow running as: python -m lambda_iot_topicrule."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template RDS_Snapshot_On_Delete: Sample template showing how to create an RDS DBInstance that is snapshotted on stack deletion. **WARNING** This template creates an Amazon RDS database instance. When the stack is deleted a database snapshot will be left in your account. You will be billed for the AWS resources used if you create a stack from this template.")
