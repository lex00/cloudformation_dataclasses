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
class InstanceAMI:
    """Managed AMI ID for EC2 Instance"""

    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    description = 'Managed AMI ID for EC2 Instance'
    default = '/aws/service/canonical/ubuntu/eks-pro/22.04/1.29/stable/current/amd64/hvm/ebs-gp2/ami-id'
