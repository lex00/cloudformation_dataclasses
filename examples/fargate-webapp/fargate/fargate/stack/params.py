"""Stack parameters."""

from .. import *  # noqa: F403, F401

VpcIdParam = Parameter(
    type=ParameterType.AWS_EC2_VPC_ID,
    description="VPC ID for the Fargate service",
)

PrivateSubnetIdsParam = Parameter(
    type=ParameterType.LIST_AWS_EC2_SUBNET_ID,
    description="Private subnet IDs for the Fargate tasks",
)

AlbSecurityGroupIdParam = Parameter(
    type=ParameterType.AWS_EC2_SECURITY_GROUP_ID,
    description="ALB Security Group ID for task ingress",
)

TargetGroupArnParam = Parameter(
    type=STRING,
    description="ALB Target Group ARN for the service",
)

DbEndpointParam = Parameter(
    type=STRING,
    description="RDS database endpoint",
)

DbSecretArnParam = Parameter(
    type=STRING,
    description="ARN of the RDS Secrets Manager secret",
)
