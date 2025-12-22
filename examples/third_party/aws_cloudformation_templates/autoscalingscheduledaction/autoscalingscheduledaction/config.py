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
class Region2ExamplesMapping:
    resource: Mapping
    map_data = {
        'us-east-1': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3.amazonaws.com/cloudformation-examples-us-east-1',
        },
        'us-west-2': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-us-west-2.amazonaws.com/cloudformation-examples-us-west-2',
        },
        'us-west-1': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-us-west-1.amazonaws.com/cloudformation-examples-us-west-1',
        },
        'eu-west-1': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-eu-west-1.amazonaws.com/cloudformation-examples-eu-west-1',
        },
        'eu-central-1': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-eu-central-1.amazonaws.com/cloudformation-examples-eu-central-1',
        },
        'ap-southeast-1': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-ap-southeast-1.amazonaws.com/cloudformation-examples-ap-southeast-1',
        },
        'ap-northeast-1': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-ap-northeast-1.amazonaws.com/cloudformation-examples-ap-northeast-1',
        },
        'ap-northeast-2': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-ap-northeast-2.amazonaws.com/cloudformation-examples-ap-northeast-2',
        },
        'ap-southeast-2': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-ap-southeast-2.amazonaws.com/cloudformation-examples-ap-southeast-2',
        },
        'ap-south-1': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-ap-south-1.amazonaws.com/cloudformation-examples-ap-south-1',
        },
        'us-east-2': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-us-east-2.amazonaws.com/cloudformation-examples-us-east-2',
        },
        'sa-east-1': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3-sa-east-1.amazonaws.com/cloudformation-examples-sa-east-1',
        },
        'cn-north-1': {
            GuardrailTopicConfig.EXAMPLES: 'https://s3.cn-north-1.amazonaws.com.cn/cloudformation-examples-cn-north-1',
        },
    }


@cloudformation_dataclass
class AWSInstanceType2ArchMapping:
    resource: Mapping
    map_data = {
        't1.micro': {
            'Arch': 'PV64',
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
            'Arch': 'PV64',
        },
        'm1.medium': {
            'Arch': 'PV64',
        },
        'm1.large': {
            'Arch': 'PV64',
        },
        'm1.xlarge': {
            'Arch': 'PV64',
        },
        'm2.xlarge': {
            'Arch': 'PV64',
        },
        'm2.2xlarge': {
            'Arch': 'PV64',
        },
        'm2.4xlarge': {
            'Arch': 'PV64',
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
            'Arch': 'PV64',
        },
        'c1.xlarge': {
            'Arch': 'PV64',
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
        'g2.2xlarge': {
            'Arch': 'HVMG2',
        },
        'g2.8xlarge': {
            'Arch': 'HVMG2',
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
            'PV64': 'ami-2a69aa47',
            'HVM64': 'ami-6869aa05',
            'HVMG2': 'ami-50b4f047',
        },
        'us-west-2': {
            'PV64': 'ami-7f77b31f',
            'HVM64': 'ami-7172b611',
            'HVMG2': 'ami-002bf460',
        },
        'us-west-1': {
            'PV64': 'ami-a2490dc2',
            'HVM64': 'ami-31490d51',
            'HVMG2': 'ami-699ad409',
        },
        'eu-west-1': {
            'PV64': 'ami-4cdd453f',
            'HVM64': 'ami-f9dd458a',
            'HVMG2': 'ami-f0e0a483',
        },
        'eu-central-1': {
            'PV64': 'ami-6527cf0a',
            'HVM64': 'ami-ea26ce85',
            'HVMG2': 'ami-d9d62ab6',
        },
        'ap-northeast-1': {
            'PV64': 'ami-3e42b65f',
            'HVM64': 'ami-374db956',
            'HVMG2': 'ami-78ba6619',
        },
        'ap-northeast-2': {
            'PV64': 'NOT_SUPPORTED',
            'HVM64': 'ami-2b408b45',
            'HVMG2': 'NOT_SUPPORTED',
        },
        'ap-southeast-1': {
            'PV64': 'ami-df9e4cbc',
            'HVM64': 'ami-a59b49c6',
            'HVMG2': 'ami-56e84c35',
        },
        'ap-southeast-2': {
            'PV64': 'ami-63351d00',
            'HVM64': 'ami-dc361ebf',
            'HVMG2': 'ami-2589b946',
        },
        'ap-south-1': {
            'PV64': 'NOT_SUPPORTED',
            'HVM64': 'ami-ffbdd790',
            'HVMG2': 'ami-f7354198',
        },
        'us-east-2': {
            'PV64': 'NOT_SUPPORTED',
            'HVM64': 'ami-f6035893',
            'HVMG2': 'NOT_SUPPORTED',
        },
        'sa-east-1': {
            'PV64': 'ami-1ad34676',
            'HVM64': 'ami-6dd04501',
            'HVMG2': 'NOT_SUPPORTED',
        },
        'cn-north-1': {
            'PV64': 'ami-77559f1a',
            'HVM64': 'ami-8e6aa0e3',
            'HVMG2': 'NOT_SUPPORTED',
        },
    }
