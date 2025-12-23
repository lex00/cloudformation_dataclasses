"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


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
    'g2.2xlarge',
    'g2.8xlarge',
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
class KeyName:
    """Name of an existing EC2 KeyPair to enable SSH access to the instances"""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'Name of an existing EC2 KeyPair to enable SSH access to the instances'
    constraint_description = 'must be the name of an existing EC2 KeyPair.'


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
class LatestAmiId:
    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'


@cloudformation_dataclass
class Region2ExamplesMapping:
    resource: Mapping
    map_data = {
        'us-east-1': {
            'Examples': 'https://s3.amazonaws.com/cloudformation-examples-us-east-1',
        },
        'us-west-2': {
            'Examples': 'https://s3-us-west-2.amazonaws.com/cloudformation-examples-us-west-2',
        },
        'us-west-1': {
            'Examples': 'https://s3-us-west-1.amazonaws.com/cloudformation-examples-us-west-1',
        },
        'eu-west-1': {
            'Examples': 'https://s3-eu-west-1.amazonaws.com/cloudformation-examples-eu-west-1',
        },
        'eu-central-1': {
            'Examples': 'https://s3-eu-central-1.amazonaws.com/cloudformation-examples-eu-central-1',
        },
        'ap-southeast-1': {
            'Examples': 'https://s3-ap-southeast-1.amazonaws.com/cloudformation-examples-ap-southeast-1',
        },
        'ap-northeast-1': {
            'Examples': 'https://s3-ap-northeast-1.amazonaws.com/cloudformation-examples-ap-northeast-1',
        },
        'ap-northeast-2': {
            'Examples': 'https://s3-ap-northeast-2.amazonaws.com/cloudformation-examples-ap-northeast-2',
        },
        'ap-southeast-2': {
            'Examples': 'https://s3-ap-southeast-2.amazonaws.com/cloudformation-examples-ap-southeast-2',
        },
        'ap-south-1': {
            'Examples': 'https://s3-ap-south-1.amazonaws.com/cloudformation-examples-ap-south-1',
        },
        'us-east-2': {
            'Examples': 'https://s3-us-east-2.amazonaws.com/cloudformation-examples-us-east-2',
        },
        'sa-east-1': {
            'Examples': 'https://s3-sa-east-1.amazonaws.com/cloudformation-examples-sa-east-1',
        },
        'cn-north-1': {
            'Examples': 'https://s3.cn-north-1.amazonaws.com.cn/cloudformation-examples-cn-north-1',
        },
    }
