"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class VPCName:
    """The name of the VPC being created."""

    resource: Parameter
    type = STRING
    description = 'The name of the VPC being created.'
    default = 'VPC Public and Private with NAT'


@cloudformation_dataclass
class SubnetConfigMapping:
    resource: Mapping
    map_data = {
        'VPC': {
            'CIDR': '10.0.0.0/16',
        },
        'Public0': {
            'CIDR': '10.0.0.0/24',
        },
        'Public1': {
            'CIDR': '10.0.1.0/24',
        },
        'Private0': {
            'CIDR': '10.0.2.0/24',
        },
        'Private1': {
            'CIDR': '10.0.3.0/24',
        },
    }
