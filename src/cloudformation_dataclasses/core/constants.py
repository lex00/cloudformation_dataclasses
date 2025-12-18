"""
CloudFormation constants for type-safe template definitions.

These are CloudFormation-specific constants that are not derived from AWS service APIs.
Service-specific constants (like DynamoDB KeyType, S3 storage classes, etc.) are
auto-generated from botocore and available in the respective service modules.
"""

# =============================================================================
# Parameter Types
# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html
# =============================================================================


class ParameterType:
    """CloudFormation parameter types."""

    STRING = "String"
    NUMBER = "Number"
    LIST_NUMBER = "List<Number>"
    COMMA_DELIMITED_LIST = "CommaDelimitedList"

    # AWS-specific parameter types
    AWS_EC2_AVAILABILITY_ZONE_NAME = "AWS::EC2::AvailabilityZone::Name"
    AWS_EC2_IMAGE_ID = "AWS::EC2::Image::Id"
    AWS_EC2_INSTANCE_ID = "AWS::EC2::Instance::Id"
    AWS_EC2_KEY_PAIR_KEY_NAME = "AWS::EC2::KeyPair::KeyName"
    AWS_EC2_SECURITY_GROUP_GROUP_NAME = "AWS::EC2::SecurityGroup::GroupName"
    AWS_EC2_SECURITY_GROUP_ID = "AWS::EC2::SecurityGroup::Id"
    AWS_EC2_SUBNET_ID = "AWS::EC2::Subnet::Id"
    AWS_EC2_VOLUME_ID = "AWS::EC2::Volume::Id"
    AWS_EC2_VPC_ID = "AWS::EC2::VPC::Id"
    AWS_ROUTE53_HOSTED_ZONE_ID = "AWS::Route53::HostedZone::Id"

    # List types
    LIST_AWS_EC2_AVAILABILITY_ZONE_NAME = "List<AWS::EC2::AvailabilityZone::Name>"
    LIST_AWS_EC2_IMAGE_ID = "List<AWS::EC2::Image::Id>"
    LIST_AWS_EC2_INSTANCE_ID = "List<AWS::EC2::Instance::Id>"
    LIST_AWS_EC2_SECURITY_GROUP_GROUP_NAME = "List<AWS::EC2::SecurityGroup::GroupName>"
    LIST_AWS_EC2_SECURITY_GROUP_ID = "List<AWS::EC2::SecurityGroup::Id>"
    LIST_AWS_EC2_SUBNET_ID = "List<AWS::EC2::Subnet::Id>"
    LIST_AWS_EC2_VOLUME_ID = "List<AWS::EC2::Volume::Id>"
    LIST_AWS_EC2_VPC_ID = "List<AWS::EC2::VPC::Id>"
    LIST_AWS_ROUTE53_HOSTED_ZONE_ID = "List<AWS::Route53::HostedZone::Id>"

    # SSM parameter types
    AWS_SSM_PARAMETER_NAME = "AWS::SSM::Parameter::Name"
    AWS_SSM_PARAMETER_VALUE_STRING = "AWS::SSM::Parameter::Value<String>"
    AWS_SSM_PARAMETER_VALUE_LIST_STRING = "AWS::SSM::Parameter::Value<List<String>>"
    AWS_SSM_PARAMETER_VALUE_COMMA_DELIMITED_LIST = "AWS::SSM::Parameter::Value<CommaDelimitedList>"


# =============================================================================
# Convenient Aliases
# =============================================================================

# Parameter types
STRING = ParameterType.STRING
NUMBER = ParameterType.NUMBER
