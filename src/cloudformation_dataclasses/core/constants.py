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
# IAM Condition Operators
# https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html
# =============================================================================


class ConditionOperator:
    """IAM policy condition operators for type-safe condition definitions."""

    # String conditions
    STRING_EQUALS = "StringEquals"
    STRING_NOT_EQUALS = "StringNotEquals"
    STRING_EQUALS_IGNORE_CASE = "StringEqualsIgnoreCase"
    STRING_NOT_EQUALS_IGNORE_CASE = "StringNotEqualsIgnoreCase"
    STRING_LIKE = "StringLike"
    STRING_NOT_LIKE = "StringNotLike"

    # Numeric conditions
    NUMERIC_EQUALS = "NumericEquals"
    NUMERIC_NOT_EQUALS = "NumericNotEquals"
    NUMERIC_LESS_THAN = "NumericLessThan"
    NUMERIC_LESS_THAN_EQUALS = "NumericLessThanEquals"
    NUMERIC_GREATER_THAN = "NumericGreaterThan"
    NUMERIC_GREATER_THAN_EQUALS = "NumericGreaterThanEquals"

    # Date conditions
    DATE_EQUALS = "DateEquals"
    DATE_NOT_EQUALS = "DateNotEquals"
    DATE_LESS_THAN = "DateLessThan"
    DATE_LESS_THAN_EQUALS = "DateLessThanEquals"
    DATE_GREATER_THAN = "DateGreaterThan"
    DATE_GREATER_THAN_EQUALS = "DateGreaterThanEquals"

    # Boolean conditions
    BOOL = "Bool"

    # Binary conditions
    BINARY_EQUALS = "BinaryEquals"

    # IP address conditions
    IP_ADDRESS = "IpAddress"
    NOT_IP_ADDRESS = "NotIpAddress"

    # ARN conditions
    ARN_EQUALS = "ArnEquals"
    ARN_NOT_EQUALS = "ArnNotEquals"
    ARN_LIKE = "ArnLike"
    ARN_NOT_LIKE = "ArnNotLike"

    # Null check
    NULL = "Null"

    # IfExists variants (append to any operator)
    STRING_EQUALS_IF_EXISTS = "StringEqualsIfExists"
    STRING_NOT_EQUALS_IF_EXISTS = "StringNotEqualsIfExists"
    STRING_LIKE_IF_EXISTS = "StringLikeIfExists"
    STRING_NOT_LIKE_IF_EXISTS = "StringNotLikeIfExists"
    NUMERIC_EQUALS_IF_EXISTS = "NumericEqualsIfExists"
    NUMERIC_NOT_EQUALS_IF_EXISTS = "NumericNotEqualsIfExists"
    NUMERIC_LESS_THAN_IF_EXISTS = "NumericLessThanIfExists"
    NUMERIC_GREATER_THAN_IF_EXISTS = "NumericGreaterThanIfExists"
    DATE_EQUALS_IF_EXISTS = "DateEqualsIfExists"
    DATE_NOT_EQUALS_IF_EXISTS = "DateNotEqualsIfExists"
    BOOL_IF_EXISTS = "BoolIfExists"
    IP_ADDRESS_IF_EXISTS = "IpAddressIfExists"
    NOT_IP_ADDRESS_IF_EXISTS = "NotIpAddressIfExists"
    ARN_EQUALS_IF_EXISTS = "ArnEqualsIfExists"
    ARN_LIKE_IF_EXISTS = "ArnLikeIfExists"

    # ForAllValues and ForAnyValue set operators (used as prefixes)
    FOR_ALL_VALUES_STRING_EQUALS = "ForAllValues:StringEquals"
    FOR_ALL_VALUES_STRING_LIKE = "ForAllValues:StringLike"
    FOR_ANY_VALUE_STRING_EQUALS = "ForAnyValue:StringEquals"
    FOR_ANY_VALUE_STRING_LIKE = "ForAnyValue:StringLike"
    FOR_ALL_VALUES_ARN_LIKE = "ForAllValues:ArnLike"
    FOR_ANY_VALUE_ARN_LIKE = "ForAnyValue:ArnLike"


# =============================================================================
# Convenient Aliases
# =============================================================================

# Parameter types
STRING = ParameterType.STRING
NUMBER = ParameterType.NUMBER

# Condition operators (commonly used)
STRING_EQUALS = ConditionOperator.STRING_EQUALS
STRING_NOT_EQUALS = ConditionOperator.STRING_NOT_EQUALS
STRING_LIKE = ConditionOperator.STRING_LIKE
STRING_NOT_LIKE = ConditionOperator.STRING_NOT_LIKE
BOOL = ConditionOperator.BOOL
IP_ADDRESS = ConditionOperator.IP_ADDRESS
ARN_LIKE = ConditionOperator.ARN_LIKE
ARN_EQUALS = ConditionOperator.ARN_EQUALS


# =============================================================================
# IP Protocol Constants
# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html
# =============================================================================


class IpProtocol:
    """IP protocol values for security group rules.

    These are the standard values accepted by AWS for the IpProtocol property
    in security group ingress and egress rules.
    """

    TCP = "tcp"
    UDP = "udp"
    ICMP = "icmp"
    ICMPV6 = "icmpv6"
    ALL = "-1"  # All protocols
