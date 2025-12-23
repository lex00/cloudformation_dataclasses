"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceType:
    """EC2 instance type"""

    resource: Parameter
    type = STRING
    description = 'EC2 instance type'
    default = 't2.micro'
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
    """The EC2 Key Pair to allow SSH access to the instances"""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'The EC2 Key Pair to allow SSH access to the instances'
    constraint_description = 'must be the name of an existing EC2 KeyPair.'


@cloudformation_dataclass
class Subnets:
    """The list of SubnetIds, for at least two Availability Zones in the region in your Virtual Private Cloud (VPC) Defaults: """

    resource: Parameter
    type = ParameterType.COMMA_DELIMITED_LIST
    description = 'The list of SubnetIds, for at least two Availability Zones in the region in your Virtual Private Cloud (VPC) Defaults: '


@cloudformation_dataclass
class VPC:
    """VPC ID for EC2 and Elastic Load Balancer"""

    resource: Parameter
    type = ParameterType.AWS_EC2_VPC_ID
    description = 'VPC ID for EC2 and Elastic Load Balancer'


@cloudformation_dataclass
class EC2RegionMapMapping:
    resource: Mapping
    map_data = {
        'ap-northeast-1': {
            '64': 'ami-d85e7fbf',
        },
        'ap-northeast-2': {
            '64': 'ami-15d5077b',
        },
        'ap-south-1': {
            '64': 'ami-83a8dbec',
        },
        'ap-southeast-1': {
            '64': 'ami-0a19a669',
        },
        'ap-southeast-2': {
            '64': 'ami-807876e3',
        },
        'ca-central-1': {
            '64': 'ami-beea56da',
        },
        'eu-central-1': {
            '64': 'ami-25a97a4a',
        },
        'eu-west-1': {
            '64': 'ami-09447c6f',
        },
        'eu-west-2': {
            '64': 'ami-63342007',
        },
        'sa-east-1': {
            '64': 'ami-8df695e1',
        },
        'us-east-1': {
            '64': 'ami-772aa961',
        },
        'us-east-2': {
            '64': 'ami-8fab8fea',
        },
        'us-west-1': {
            '64': 'ami-1da8f27d',
        },
        'us-west-2': {
            '64': 'ami-7c22b41c',
        },
    }
