"""Allow running as: python -m cfn_endpoint_waitcondition_no_igw."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template deploys a VPC with a pair of private subnets spread across two Availabilty Zones. It deploys VPC Endpoints for CloudFormation and S3 so an instance in the private subnet can use cfn-signal for a WaitCondition. **WARNING** You will be billed for the AWS resources used if you create a stack from this template.\n")
