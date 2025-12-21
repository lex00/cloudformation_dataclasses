"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class SubnetConfigMapping:
    resource: Mapping
    map_data = {
        'VPC': {
            'CIDR': '10.0.0.0/16',
        },
        'PublicOne': {
            'CIDR': '10.0.0.0/24',
        },
        'PublicTwo': {
            'CIDR': '10.0.1.0/24',
        },
        'PrivateOne': {
            'CIDR': '10.0.2.0/24',
        },
        'PrivateTwo': {
            'CIDR': '10.0.3.0/24',
        },
    }
