"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KeyName:
    """Name of an existing EC2 KeyPair to enable SSH access to the instance"""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'Name of an existing EC2 KeyPair to enable SSH access to the instance'
    constraint_description = 'must be the name of an existing EC2 KeyPair.'


@cloudformation_dataclass
class InstanceType:
    """EC2 instance type"""

    resource: Parameter
    type = STRING
    description = 'EC2 instance type'
    default = 't3.medium'
    constraint_description = 'must be a valid EC2 instance type.'


@cloudformation_dataclass
class RHELVersion:
    """RHEL version to deploy"""

    resource: Parameter
    type = STRING
    description = 'RHEL version to deploy'
    default = 'RHEL9'
    allowed_values = ['RHEL9']


@cloudformation_dataclass
class IAMRole:
    """EC2 attached IAM role"""

    resource: Parameter
    type = STRING
    description = 'EC2 attached IAM role'
    default = 'CloudWatchAgentAdminRole'
    constraint_description = 'must be an existing IAM role which will be attached to EC2 instance.'


@cloudformation_dataclass
class SSHLocation:
    """The IP address range that can be used to SSH to the EC2 instances"""

    resource: Parameter
    type = STRING
    description = 'The IP address range that can be used to SSH to the EC2 instances'
    default = '0.0.0.0/0'
    allowed_pattern = '(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})'
    min_length = 9
    max_length = 18
    constraint_description = 'must be a valid IP CIDR range of the form x.x.x.x/x.'


@cloudformation_dataclass
class SubnetId:
    resource: Parameter
    type = ParameterType.AWS_EC2_SUBNET_ID


@cloudformation_dataclass
class RegionMapMapping:
    resource: Mapping
    map_data = {
        'us-east-1': {
            'RHEL9': 'ami-0fb13bb53494158e9',
        },
        'us-east-2': {
            'RHEL9': 'ami-0aeea2f24f6d3ba32',
        },
        'us-west-1': {
            'RHEL9': 'ami-068c2af1200ef7356',
        },
        'us-west-2': {
            'RHEL9': 'ami-0367f2b5c3d1ef960',
        },
        'eu-west-1': {
            'RHEL9': 'ami-0e28d6c0c65e7f82f',
        },
        'eu-west-2': {
            'RHEL9': 'ami-02b1e3a99e36afd1a',
        },
        'ap-northeast-1': {
            'RHEL9': 'ami-0eade93757ef7bb6c',
        },
        'ap-northeast-2': {
            'RHEL9': 'ami-097698b6cd8164ea2',
        },
        'ap-southeast-1': {
            'RHEL9': 'ami-0b9521fddc9871128',
        },
        'ap-southeast-2': {
            'RHEL9': 'ami-0eea634029e7b983c',
        },
    }
