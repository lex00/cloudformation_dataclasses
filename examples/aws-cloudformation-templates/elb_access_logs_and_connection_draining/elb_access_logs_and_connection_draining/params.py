"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class InstanceType:
    """WebServer EC2 instance type"""

    resource: Parameter
    type = STRING
    description = 'WebServer EC2 instance type'
    default = 't3.micro'
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


@cloudformation_dataclass
class Region2ELBAccountIdMapping:
    resource: Mapping
    map_data = {
        'us-east-1': {
            'AccountId': '127311923021',
        },
        'us-west-1': {
            'AccountId': '027434742980',
        },
        'us-west-2': {
            'AccountId': '797873946194',
        },
        'eu-west-1': {
            'AccountId': '156460612806',
        },
        'ap-northeast-1': {
            'AccountId': '582318560864',
        },
        'ap-northeast-2': {
            'AccountId': '600734575887',
        },
        'ap-southeast-1': {
            'AccountId': '114774131450',
        },
        'ap-southeast-2': {
            'AccountId': '783225319266',
        },
        'ap-south-1': {
            'AccountId': '718504428378',
        },
        'us-east-2': {
            'AccountId': '033677994240',
        },
        'sa-east-1': {
            'AccountId': '507241528517',
        },
        'cn-north-1': {
            'AccountId': '638102146993',
        },
        'eu-central-1': {
            'AccountId': '054676820928',
        },
    }
