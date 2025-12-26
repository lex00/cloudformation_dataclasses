"""Allow running as: python -m cfn_endpoint_waitcondition."""
from cloudformation_dataclasses import run_package_cli

run_package_cli(__package__, description="This template deploys a VPC with a pair of public and private subnets spread across two Availabilty Zones. It deploys an Internet Gateway, with a default route on the public subnets and a bastion server. It deploys VPC Endpoints for CloudFormation and S3 so an instance in the private subnet can use cfn-signal for a WaitCondition. **WARNING** You will be billed for the AWS resources used if you create a stack from this template.\n")
