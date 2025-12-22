"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class InstanceType:
    """WebServer EC2 instance type"""

    resource: Parameter
    type = STRING
    description = 'WebServer EC2 instance type'
    default = 't4g.micro'


@cloudformation_dataclass
class OperatorEMail:
    """Email address to notify if there are any scaling operations"""

    resource: Parameter
    type = STRING
    description = 'Email address to notify if there are any scaling operations'


@cloudformation_dataclass
class KeyName:
    """The EC2 Key Pair to allow SSH access to the instances"""

    resource: Parameter
    type = ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME
    description = 'The EC2 Key Pair to allow SSH access to the instances'
    constraint_description = 'must be the name of an existing EC2 KeyPair.'


@cloudformation_dataclass
class SSHLocation:
    """The IP address range that can be used to SSH to the EC2 instances"""

    resource: Parameter
    type = STRING
    description = 'The IP address range that can be used to SSH to the EC2 instances'
    default = '192.168.1.0/24'
    allowed_pattern = '(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})'
    min_length = 9
    max_length = 18
    constraint_description = 'must be a valid IP CIDR range of the form x.x.x.x/x.'


@cloudformation_dataclass
class LatestAmiId:
    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-arm64'


@cloudformation_dataclass
class KmsKeyArn:
    """KMS Key ARN to encrypt data"""

    resource: Parameter
    type = STRING
    description = 'KMS Key ARN to encrypt data'


@cloudformation_dataclass
class CertificateArn:
    """Certificate ARN for HTTPS"""

    resource: Parameter
    type = STRING
    description = 'Certificate ARN for HTTPS'


@cloudformation_dataclass
class SecurityGroups:
    """Security Groups to be used"""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SECURITY_GROUP_ID
    description = 'Security Groups to be used'


@cloudformation_dataclass
class Subnets:
    """Subnets to be used"""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SUBNET_ID
    description = 'Subnets to be used'


@cloudformation_dataclass
class AZs:
    """Availability Zones to be used"""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_AVAILABILITY_ZONE_NAME
    description = 'Availability Zones to be used'


@cloudformation_dataclass
class VPC:
    """VPC to be used"""

    resource: Parameter
    type = ParameterType.AWS_EC2_VPC_ID
    description = 'VPC to be used'


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
