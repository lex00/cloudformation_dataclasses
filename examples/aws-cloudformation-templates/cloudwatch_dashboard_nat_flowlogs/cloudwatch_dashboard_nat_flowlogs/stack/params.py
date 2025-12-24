"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGatewayPrivateIP:
    """The private IP address of the NAT Gateway"""

    resource: Parameter
    type = STRING
    description = 'The private IP address of the NAT Gateway'


@cloudformation_dataclass
class NatGatewayID:
    """The ID of the NAT Gateway"""

    resource: Parameter
    type = STRING
    description = 'The ID of the NAT Gateway'


@cloudformation_dataclass
class VpcCidr:
    """The CIDR block of the VPC"""

    resource: Parameter
    type = STRING
    description = 'The CIDR block of the VPC'


@cloudformation_dataclass
class LogGroupName:
    """The ARN of the log group to query"""

    resource: Parameter
    type = STRING
    description = 'The ARN of the log group to query'
