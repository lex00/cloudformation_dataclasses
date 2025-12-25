"""Stack parameters."""

from .. import *  # noqa: F403, F401

VpcIdParam = Parameter(
    type=ParameterType.AWS_EC2_VPC_ID,
    description="VPC ID for the RDS instance",
)

PrivateSubnetIdsParam = Parameter(
    type=ParameterType.LIST_AWS_EC2_SUBNET_ID,
    description="Private subnet IDs for the DB subnet group",
)

VpcCidrParam = Parameter(
    type=STRING,
    description="VPC CIDR block for security group ingress",
    default="10.0.0.0/16",
)

DatabaseNameParam = Parameter(
    type=STRING,
    description="Name of the database to create",
    default="webapp",
)
