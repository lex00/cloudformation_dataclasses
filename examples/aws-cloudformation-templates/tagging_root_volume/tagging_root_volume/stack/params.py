"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KeyName:
    """Name of an existing EC2 KeyPair to enable SSH access to the ECS instances."""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'Name of an existing EC2 KeyPair to enable SSH access to the ECS instances.'


@cloudformation_dataclass
class InstanceType:
    """EC2 instance type"""

    resource: Parameter
    type = STRING
    description = 'EC2 instance type'
    default = 't2.micro'
    allowed_values = [
    't2.micro',
    't2.small',
    't2.medium',
    't2.large',
    'm3.medium',
    'm3.large',
    'm3.xlarge',
    'm3.2xlarge',
    'm4.large',
    'm4.xlarge',
    'm4.2xlarge',
    'm4.4xlarge',
    'm4.10xlarge',
    'c4.large',
    'c4.xlarge',
    'c4.2xlarge',
    'c4.4xlarge',
    'c4.8xlarge',
    'c3.large',
    'c3.xlarge',
    'c3.2xlarge',
    'c3.4xlarge',
    'c3.8xlarge',
    'r3.large',
    'r3.xlarge',
    'r3.2xlarge',
    'r3.4xlarge',
    'r3.8xlarge',
    'i2.xlarge',
    'i2.2xlarge',
    'i2.4xlarge',
    'i2.8xlarge',
]
    constraint_description = 'Please choose a valid instance type.'


@cloudformation_dataclass
class InstanceAZ:
    """EC2 AZ."""

    resource: Parameter
    type = ParameterType.AWS_EC2_AVAILABILITY_ZONE_NAME
    description = 'EC2 AZ.'
    constraint_description = 'Must be the name of an availabity zone.'


@cloudformation_dataclass
class WindowsAMIID:
    """The Latest Windows 2016 AMI taken from the public Systems Manager Parameter Store"""

    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    description = 'The Latest Windows 2016 AMI taken from the public Systems Manager Parameter Store'
    default = '/aws/service/ami-windows-latest/Windows_Server-2016-English-Full-Base'


@cloudformation_dataclass
class LinuxAMIID:
    """The Latest Amazon Linux 2 AMI taken from the public Systems Manager Parameter Store"""

    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    description = 'The Latest Amazon Linux 2 AMI taken from the public Systems Manager Parameter Store'
    default = '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'


@cloudformation_dataclass
class SubnetId:
    resource: Parameter
    type = ParameterType.AWS_EC2_SUBNET_ID
