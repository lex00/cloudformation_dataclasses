"""Parameters for ALB stack."""

from .. import *  # noqa: F403, F401

VpcIdParam = Parameter(
    type=ParameterType.AWS_EC2_VPC_ID,
    description="VPC ID",
)

PublicSubnetIdsParam = Parameter(
    type=ParameterType.LIST_AWS_EC2_SUBNET_ID,
    description="Public subnet IDs (comma-separated)",
)

CertificateArnParam = Parameter(
    type=STRING,
    description="ACM Certificate ARN",
)

HostedZoneIdParam = Parameter(
    type=ParameterType.AWS_ROUTE53_HOSTED_ZONE_ID,
    description="Route53 Hosted Zone ID",
)

DomainNameParam = Parameter(
    type=STRING,
    description="Domain name (e.g., example.com)",
)
