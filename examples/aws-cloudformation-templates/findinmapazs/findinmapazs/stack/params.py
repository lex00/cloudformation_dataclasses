"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VpcCIDR:
    """Please enter the IP range (CIDR notation) for this VPC"""

    resource: Parameter
    type = STRING
    description = 'Please enter the IP range (CIDR notation) for this VPC'
    default = '10.192.0.0/16'


@cloudformation_dataclass
class PublicSubnet1CIDR:
    """Please enter the IP range (CIDR notation) for the public subnet in the first Availability Zone"""

    resource: Parameter
    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the public subnet in the first Availability Zone'
    default = '10.192.10.0/24'


@cloudformation_dataclass
class PublicSubnet2CIDR:
    """Please enter the IP range (CIDR notation) for the public subnet in the second Availability Zone"""

    resource: Parameter
    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the public subnet in the second Availability Zone'
    default = '10.192.11.0/24'


@cloudformation_dataclass
class PrivateSubnet1CIDR:
    """Please enter the IP range (CIDR notation) for the private subnet in the first Availability Zone"""

    resource: Parameter
    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the private subnet in the first Availability Zone'
    default = '10.192.20.0/24'


@cloudformation_dataclass
class PrivateSubnet2CIDR:
    """Please enter the IP range (CIDR notation) for the private subnet in the second Availability Zone"""

    resource: Parameter
    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the private subnet in the second Availability Zone'
    default = '10.192.21.0/24'


@cloudformation_dataclass
class RegionMapMapping:
    resource: Mapping
    map_data = {
        'us-east-1': {
            'AZs': [
                'us-east-1a',
                'us-east-1b',
                'us-east-1c',
            ],
        },
        'us-west-2': {
            'AZs': [
                'us-west-2a',
                'us-west-2b',
                'us-west-2c',
            ],
        },
    }
