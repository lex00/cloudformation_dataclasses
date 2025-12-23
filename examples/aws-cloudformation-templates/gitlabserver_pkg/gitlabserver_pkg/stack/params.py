"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LatestAMI:
    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64'


@cloudformation_dataclass
class InstanceType:
    resource: Parameter
    type = STRING
    default = 'm5.large'


@cloudformation_dataclass
class PrefixesMapping:
    resource: Mapping
    map_data = {
        'ap-northeast-1': {
            'PrefixList': 'pl-58a04531',
        },
        'ap-northeast-2': {
            'PrefixList': 'pl-22a6434b',
        },
        'ap-south-1': {
            'PrefixList': 'pl-9aa247f3',
        },
        'ap-southeast-1': {
            'PrefixList': 'pl-31a34658',
        },
        'ap-southeast-2': {
            'PrefixList': 'pl-b8a742d1',
        },
        'ca-central-1': {
            'PrefixList': 'pl-38a64351',
        },
        'eu-central-1': {
            'PrefixList': 'pl-a3a144ca',
        },
        'eu-north-1': {
            'PrefixList': 'pl-fab65393',
        },
        'eu-west-1': {
            'PrefixList': 'pl-4fa04526',
        },
        'eu-west-2': {
            'PrefixList': 'pl-93a247fa',
        },
        'eu-west-3': {
            'PrefixList': 'pl-75b1541c',
        },
        'sa-east-1': {
            'PrefixList': 'pl-5da64334',
        },
        'us-east-1': {
            'PrefixList': 'pl-3b927c52',
        },
        'us-east-2': {
            'PrefixList': 'pl-b6a144df',
        },
        'us-west-1': {
            'PrefixList': 'pl-4ea04527',
        },
        'us-west-2': {
            'PrefixList': 'pl-82a045eb',
        },
    }
