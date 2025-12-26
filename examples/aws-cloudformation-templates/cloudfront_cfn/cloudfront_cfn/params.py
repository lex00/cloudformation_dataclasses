"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class KeyName:
    """Name of an existing EC2 KeyPair to enable SSH access to the instance"""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'Name of an existing EC2 KeyPair to enable SSH access to the instance'


@cloudformation_dataclass
class InstanceType:
    """WebServer EC2 instance type"""

    resource: Parameter
    type = STRING
    description = 'WebServer EC2 instance type'
    default = 't2.small'
    allowed_values = [
    't1.micro',
    't2.nano',
    't2.micro',
    't2.small',
    't2.medium',
    't2.large',
    'm1.small',
    'm1.medium',
    'm1.large',
    'm1.xlarge',
    'm2.xlarge',
    'm2.2xlarge',
    'm2.4xlarge',
    'm3.medium',
    'm3.large',
    'm3.xlarge',
    'm3.2xlarge',
    'm4.large',
    'm4.xlarge',
    'm4.2xlarge',
    'm4.4xlarge',
    'm4.10xlarge',
    'c1.medium',
    'c1.xlarge',
    'c3.large',
    'c3.xlarge',
    'c3.2xlarge',
    'c3.4xlarge',
    'c3.8xlarge',
    'c4.large',
    'c4.xlarge',
    'c4.2xlarge',
    'c4.4xlarge',
    'c4.8xlarge',
    'r3.large',
    'r3.xlarge',
    'r3.2xlarge',
    'r3.4xlarge',
    'r3.8xlarge',
    'i2.xlarge',
    'i2.2xlarge',
    'i2.4xlarge',
    'i2.8xlarge',
    'd2.xlarge',
    'd2.2xlarge',
    'd2.4xlarge',
    'd2.8xlarge',
    'hs1.8xlarge',
    'cr1.8xlarge',
    'cc2.8xlarge',
]
    constraint_description = 'must be a valid EC2 instance type.'


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
class AWSInstanceType2ArchMapping:
    resource: Mapping
    map_data = {
        't1.micro': {
            'Arch': 'HVM64',
        },
        't2.nano': {
            'Arch': 'HVM64',
        },
        't2.micro': {
            'Arch': 'HVM64',
        },
        't2.small': {
            'Arch': 'HVM64',
        },
        't2.medium': {
            'Arch': 'HVM64',
        },
        't2.large': {
            'Arch': 'HVM64',
        },
        'm1.small': {
            'Arch': 'HVM64',
        },
        'm1.medium': {
            'Arch': 'HVM64',
        },
        'm1.large': {
            'Arch': 'HVM64',
        },
        'm1.xlarge': {
            'Arch': 'HVM64',
        },
        'm2.xlarge': {
            'Arch': 'HVM64',
        },
        'm2.2xlarge': {
            'Arch': 'HVM64',
        },
        'm2.4xlarge': {
            'Arch': 'HVM64',
        },
        'm3.medium': {
            'Arch': 'HVM64',
        },
        'm3.large': {
            'Arch': 'HVM64',
        },
        'm3.xlarge': {
            'Arch': 'HVM64',
        },
        'm3.2xlarge': {
            'Arch': 'HVM64',
        },
        'm4.large': {
            'Arch': 'HVM64',
        },
        'm4.xlarge': {
            'Arch': 'HVM64',
        },
        'm4.2xlarge': {
            'Arch': 'HVM64',
        },
        'm4.4xlarge': {
            'Arch': 'HVM64',
        },
        'm4.10xlarge': {
            'Arch': 'HVM64',
        },
        'c1.medium': {
            'Arch': 'HVM64',
        },
        'c1.xlarge': {
            'Arch': 'HVM64',
        },
        'c3.large': {
            'Arch': 'HVM64',
        },
        'c3.xlarge': {
            'Arch': 'HVM64',
        },
        'c3.2xlarge': {
            'Arch': 'HVM64',
        },
        'c3.4xlarge': {
            'Arch': 'HVM64',
        },
        'c3.8xlarge': {
            'Arch': 'HVM64',
        },
        'c4.large': {
            'Arch': 'HVM64',
        },
        'c4.xlarge': {
            'Arch': 'HVM64',
        },
        'c4.2xlarge': {
            'Arch': 'HVM64',
        },
        'c4.4xlarge': {
            'Arch': 'HVM64',
        },
        'c4.8xlarge': {
            'Arch': 'HVM64',
        },
        'r3.large': {
            'Arch': 'HVM64',
        },
        'r3.xlarge': {
            'Arch': 'HVM64',
        },
        'r3.2xlarge': {
            'Arch': 'HVM64',
        },
        'r3.4xlarge': {
            'Arch': 'HVM64',
        },
        'r3.8xlarge': {
            'Arch': 'HVM64',
        },
        'i2.xlarge': {
            'Arch': 'HVM64',
        },
        'i2.2xlarge': {
            'Arch': 'HVM64',
        },
        'i2.4xlarge': {
            'Arch': 'HVM64',
        },
        'i2.8xlarge': {
            'Arch': 'HVM64',
        },
        'd2.xlarge': {
            'Arch': 'HVM64',
        },
        'd2.2xlarge': {
            'Arch': 'HVM64',
        },
        'd2.4xlarge': {
            'Arch': 'HVM64',
        },
        'd2.8xlarge': {
            'Arch': 'HVM64',
        },
        'hi1.4xlarge': {
            'Arch': 'HVM64',
        },
        'hs1.8xlarge': {
            'Arch': 'HVM64',
        },
        'cr1.8xlarge': {
            'Arch': 'HVM64',
        },
        'cc2.8xlarge': {
            'Arch': 'HVM64',
        },
    }


@cloudformation_dataclass
class AWSRegionArch2AMIMapping:
    resource: Mapping
    map_data = {
        'us-east-1': {
            'HVM64': 'ami-0149b2da6ceec4bb0',
        },
        'us-west-2': {
            'HVM64': 'ami-0c09c7eb16d3e8e70',
        },
        'us-west-1': {
            'HVM64': 'ami-03f6d497fceb40069',
        },
        'eu-west-1': {
            'HVM64': 'ami-0fd8802f94ed1c969',
        },
        'eu-west-2': {
            'HVM64': 'ami-04842bc62789b682e',
        },
        'eu-west-3': {
            'HVM64': 'ami-064736ff8301af3ee',
        },
        'eu-central-1': {
            'HVM64': 'ami-06148e0e81e5187c8',
        },
        'ap-northeast-1': {
            'HVM64': 'ami-09b18720cb71042df',
        },
        'ap-northeast-2': {
            'HVM64': 'ami-07d16c043aa8e5153',
        },
        'ap-northeast-3': {
            'HVM64': 'ami-09d2f3a31110c6ad4',
        },
        'ap-southeast-1': {
            'HVM64': 'ami-00e912d13fbb4f225',
        },
        'ap-southeast-2': {
            'HVM64': 'ami-055166f8a8041fbf1',
        },
        'ap-south-1': {
            'HVM64': 'ami-024c319d5d14b463e',
        },
        'us-east-2': {
            'HVM64': 'ami-0d5bf08bc8017c83b',
        },
        'ca-central-1': {
            'HVM64': 'ami-043a72cf696697251',
        },
        'sa-east-1': {
            'HVM64': 'ami-00742e66d44c13cd9',
        },
    }
