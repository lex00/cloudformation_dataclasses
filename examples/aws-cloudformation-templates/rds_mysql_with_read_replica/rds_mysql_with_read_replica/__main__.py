"""Allow running as: python -m rds_mysql_with_read_replica."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template RDS_MySQL_With_Read_Replica: Sample template showing how to create a highly-available, RDS DBInstance with a read replica. **WARNING** This template creates an Amazon Relational Database Service database instance and Amazon CloudWatch alarms. You will be billed for the AWS resources used if you create a stack from this template.")
