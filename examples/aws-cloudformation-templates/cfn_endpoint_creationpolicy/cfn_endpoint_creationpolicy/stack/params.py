"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EnvironmentName:
    """An environment name that will be prefixed to resource names"""

    resource: Parameter
    type = STRING
    description = 'An environment name that will be prefixed to resource names'


@cloudformation_dataclass
class VpcCIDR:
    """Please enter the IP range (CIDR notation) for this VPC"""

    resource: Parameter
    type = STRING
    description = 'Please enter the IP range (CIDR notation) for this VPC'
    default = '10.192.0.0/16'
    allowed_pattern = '((\\d{1,3})\\.){3}\\d{1,3}/\\d{1,2}'


@cloudformation_dataclass
class PublicSubnet1CIDR:
    """Please enter the IP range (CIDR notation) for the public subnet in the first Availability Zone"""

    resource: Parameter
    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the public subnet in the first Availability Zone'
    default = '10.192.10.0/24'
    allowed_pattern = '((\\d{1,3})\\.){3}\\d{1,3}/\\d{1,2}'


@cloudformation_dataclass
class PublicSubnet2CIDR:
    """Please enter the IP range (CIDR notation) for the public subnet in the second Availability Zone"""

    resource: Parameter
    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the public subnet in the second Availability Zone'
    default = '10.192.11.0/24'
    allowed_pattern = '((\\d{1,3})\\.){3}\\d{1,3}/\\d{1,2}'


@cloudformation_dataclass
class PrivateSubnet1CIDR:
    """Please enter the IP range (CIDR notation) for the private subnet in the first Availability Zone"""

    resource: Parameter
    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the private subnet in the first Availability Zone'
    default = '10.192.20.0/24'
    allowed_pattern = '((\\d{1,3})\\.){3}\\d{1,3}/\\d{1,2}'


@cloudformation_dataclass
class PrivateSubnet2CIDR:
    """Please enter the IP range (CIDR notation) for the private subnet in the second Availability Zone"""

    resource: Parameter
    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the private subnet in the second Availability Zone'
    default = '10.192.21.0/24'
    allowed_pattern = '((\\d{1,3})\\.){3}\\d{1,3}/\\d{1,2}'


@cloudformation_dataclass
class KeyName:
    """Key pair for EC2 access"""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'Key pair for EC2 access'


@cloudformation_dataclass
class LinuxAMI:
    """Managed AMI ID for Amazon Linux"""

    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    description = 'Managed AMI ID for Amazon Linux'
    default = '/aws/service/ami-amazon-linux-latest/amzn-ami-hvm-x86_64-gp2'
