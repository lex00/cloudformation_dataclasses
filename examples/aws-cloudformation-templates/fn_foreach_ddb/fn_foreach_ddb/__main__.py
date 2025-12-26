"""Allow running as: python -m fn_foreach_ddb."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template Config: This template demonstrates the usage of AWS Config resources. **WARNING** You will be billed for the AWS resources used if you create a stack from this template.")
