"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_VPC_ID


@cloudformation_dataclass
class Subnet1:
    """ID of the Subnet the instance should be launched in, this will link the instance to the same VPC."""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SUBNET_ID
    description = 'ID of the Subnet the instance should be launched in, this will link the instance to the same VPC.'


@cloudformation_dataclass
class Subnet2:
    """ID of the Subnet the instance should be launched in, this will link the instance to the same VPC."""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SUBNET_ID
    description = 'ID of the Subnet the instance should be launched in, this will link the instance to the same VPC.'


@cloudformation_dataclass
class ELBType:
    resource: Parameter
    type = STRING
    default = 'network'


@cloudformation_dataclass
class ELBIpAddressType:
    resource: Parameter
    type = STRING
    default = 'ipv4'
    allowed_values = [
    'ipv4',
    'dualstack',
]
