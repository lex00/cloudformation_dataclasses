"""
CloudFormation constants for type-safe template definitions.

These constants replace magic strings in CloudFormation templates.
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

    # SSM parameter types
    AWS_SSM_PARAMETER_NAME = "AWS::SSM::Parameter::Name"
    AWS_SSM_PARAMETER_VALUE_STRING = "AWS::SSM::Parameter::Value<String>"
    AWS_SSM_PARAMETER_VALUE_LIST_STRING = "AWS::SSM::Parameter::Value<List<String>>"
    AWS_SSM_PARAMETER_VALUE_COMMA_DELIMITED_LIST = (
        "AWS::SSM::Parameter::Value<CommaDelimitedList>"
    )


# =============================================================================
# DynamoDB Key Types
# https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_KeySchemaElement.html
# =============================================================================


class KeyType:
    """DynamoDB key types for KeySchema."""

    HASH = "HASH"
    RANGE = "RANGE"


# =============================================================================
# DynamoDB Attribute Types
# https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeDefinition.html
# =============================================================================


class AttributeType:
    """DynamoDB attribute types for AttributeDefinition."""

    STRING = "S"
    NUMBER = "N"
    BINARY = "B"


# =============================================================================
# DynamoDB Projection Types
# https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Projection.html
# =============================================================================


class ProjectionType:
    """DynamoDB projection types for secondary indexes."""

    KEYS_ONLY = "KEYS_ONLY"
    INCLUDE = "INCLUDE"
    ALL = "ALL"


# Convenient aliases - Parameter types
STRING = ParameterType.STRING
NUMBER = ParameterType.NUMBER

# Convenient aliases - DynamoDB key types
HASH = KeyType.HASH
RANGE = KeyType.RANGE

# Convenient aliases - DynamoDB attribute types
S = AttributeType.STRING
N = AttributeType.NUMBER
B = AttributeType.BINARY

# Convenient aliases - DynamoDB projection types
KEYS_ONLY = ProjectionType.KEYS_ONLY
INCLUDE = ProjectionType.INCLUDE
ALL = ProjectionType.ALL
