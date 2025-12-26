"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class KeyName:
    """Name of an existing EC2 KeyPair to enable SSH access to the web server"""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'Name of an existing EC2 KeyPair to enable SSH access to the web server'
    constraint_description = 'must be the name of an existing EC2 KeyPair.'


@cloudformation_dataclass
class InstanceType:
    """WebServer EC2 instance type"""

    resource: Parameter
    type = STRING
    description = 'WebServer EC2 instance type'
    default = 't2.nano'
    allowed_values = [
    't2.nano',
    't2.micro',
    't2.small',
    't2.medium',
    't2.large',
    't2.xlarge',
    't2.2xlarge',
    't3.nano',
    't3.micro',
    't3.small',
    't3.medium',
    't3.large',
    't3.xlarge',
    't3.2xlarge',
    'm4.large',
    'm4.xlarge',
    'm4.2xlarge',
    'm4.4xlarge',
    'm4.10xlarge',
    'm5.large',
    'm5.xlarge',
    'm5.2xlarge',
    'm5.4xlarge',
    'c5.large',
    'c5.xlarge',
    'c5.2xlarge',
    'c5.4xlarge',
    'c5.9xlarge',
    'g3.8xlarge',
    'r5.large',
    'r5.xlarge',
    'r5.2xlarge',
    'r5.4xlarge',
    'r5.12xlarge',
    'i3.xlarge',
    'i3.2xlarge',
    'i3.4xlarge',
    'i3.8xlarge',
    'd2.xlarge',
    'd2.2xlarge',
    'd2.4xlarge',
    'd2.8xlarge',
]
    constraint_description = 'must be a valid EC2 instance type.'


@cloudformation_dataclass
class SSHLocation:
    """Lockdown SSH access to the bastion host (default can be accessed from anywhere)"""

    resource: Parameter
    type = STRING
    description = 'Lockdown SSH access to the bastion host (default can be accessed from anywhere)'
    default = '198.162.1.0/0'
    allowed_pattern = '(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})'
    min_length = 9
    max_length = 18
    constraint_description = 'must be a valid CIDR range of the form x.x.x.x/x.'


@cloudformation_dataclass
class LatestAmiId:
    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'


@cloudformation_dataclass
class Subnets:
    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SUBNET_ID
