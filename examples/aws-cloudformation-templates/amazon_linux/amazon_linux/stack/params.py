"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SSMKey:
    """Name of parameter store which contains the json configuration of CWAgent."""

    resource: Parameter
    type = STRING
    description = 'Name of parameter store which contains the json configuration of CWAgent.'
    default = 'AmazonCloudWatch-DefaultLinuxConfigCloudFormation'


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
class InstanceAMI:
    """Managed AMI ID for EC2 Instance"""

    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    description = 'Managed AMI ID for EC2 Instance'
    default = '/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64'


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
