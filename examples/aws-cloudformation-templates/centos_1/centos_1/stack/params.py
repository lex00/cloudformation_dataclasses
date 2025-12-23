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
class CentOSVersion:
    """CentOS version to deploy"""

    resource: Parameter
    type = STRING
    description = 'CentOS version to deploy'
    default = 'CentOS9'
    allowed_values = ['CentOS9']


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
            'CentOS9': 'ami-0705f7887207411ca',
        },
        'us-east-2': {
            'CentOS9': 'ami-0fe2c46c1dc3889fa',
        },
        'us-west-1': {
            'CentOS9': 'ami-0f4f63d1732fd4ef5',
        },
        'us-west-2': {
            'CentOS9': 'ami-00b231246df1d28de',
        },
        'eu-west-1': {
            'CentOS9': 'ami-05a7b8270231783b2',
        },
        'eu-west-2': {
            'CentOS9': 'ami-0086646e63ce5aaf1',
        },
        'ap-northeast-1': {
            'CentOS9': 'ami-0d8ee41b4b6f8343b',
        },
        'ap-northeast-2': {
            'CentOS9': 'ami-031e0786d2134adf6',
        },
        'ap-southeast-1': {
            'CentOS9': 'ami-0a9082a6b182a840b',
        },
        'ap-southeast-2': {
            'CentOS9': 'ami-05ffc8a6cb624035b',
        },
    }
