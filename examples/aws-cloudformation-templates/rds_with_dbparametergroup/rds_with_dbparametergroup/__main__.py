"""Allow running as: python -m rds_with_dbparametergroup."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="Sample template showing how to create an Amazon RDS Database Instance with a\nDBParameterGroup. **WARNING** This template creates an Amazon Relational\nDatabase Service database instance. You will be billed for the AWS\nresources used if you create a stack from this template.\n")
