"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DesiredCapacity:
    """Number of EC2 instances to launch in your ECS cluster."""

    resource: Parameter
    type = NUMBER
    description = 'Number of EC2 instances to launch in your ECS cluster.'
    default = '3'


@cloudformation_dataclass
class MaxSize:
    """Maximum number of EC2 instances that can be launched in your ECS cluster."""

    resource: Parameter
    type = NUMBER
    description = 'Maximum number of EC2 instances that can be launched in your ECS cluster.'
    default = '6'


@cloudformation_dataclass
class ECSAMI:
    """AMI ID"""

    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    description = 'AMI ID'
    default = '/aws/service/ecs/optimized-ami/amazon-linux-2/recommended/image_id'


@cloudformation_dataclass
class InstanceType:
    """EC2 instance type"""

    resource: Parameter
    type = STRING
    description = 'EC2 instance type'
    default = 'c4.xlarge'
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
