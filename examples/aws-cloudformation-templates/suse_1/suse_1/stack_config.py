"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


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
class SUSEVersion:
    """SUSE Linux Enterprise Server version to deploy"""

    resource: Parameter
    type = STRING
    description = 'SUSE Linux Enterprise Server version to deploy'
    default = 'SLES15SP5'
    allowed_values = ['SLES15SP5']


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


@cloudformation_dataclass
class RegionMapMapping:
    resource: Mapping
    map_data = {
        'us-east-1': {
            'SLES15SP5': 'ami-0d62a8e6541a2d491',
        },
        'us-east-2': {
            'SLES15SP5': 'ami-05d1f1c3db2b2eb0c',
        },
        'us-west-1': {
            'SLES15SP5': 'ami-060034d187be82d31',
        },
        'us-west-2': {
            'SLES15SP5': 'ami-066c85d277ae33d38',
        },
        'eu-west-1': {
            'SLES15SP5': 'ami-028867095499bce4b',
        },
        'eu-west-2': {
            'SLES15SP5': 'ami-03d783398e1e54eb1',
        },
        'ap-northeast-1': {
            'SLES15SP5': 'ami-05ef8ea5a07946994',
        },
        'ap-northeast-2': {
            'SLES15SP5': 'ami-0f8bf550807d8d01a',
        },
        'ap-southeast-1': {
            'SLES15SP5': 'ami-0db03992e79210b9f',
        },
        'ap-southeast-2': {
            'SLES15SP5': 'ami-084fd76702fabcf2c',
        },
    }
