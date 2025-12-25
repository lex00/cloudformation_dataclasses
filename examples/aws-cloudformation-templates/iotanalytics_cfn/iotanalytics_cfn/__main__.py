"""Allow running as: python -m iotanalytics_cfn."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="AWS CloudFormation Sample Template Config: This template creates a Channel, Datastore, Pipeline and Dataset with SQL action. **WARNING** You will be billed for the AWS resources used if you create a stack from this template. See https://aws.amazon.com/blogs/iot/introducing-aws-cloudformation-support-for-aws-iot-analytics/ for further details.")
