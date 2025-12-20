"""Shared constant mappings for code generation and linting.

These maps are used by both the importer (for code generation) and the linter
(for detecting and fixing common issues).
"""

# =============================================================================
# Condition Operator Mappings
# =============================================================================

# Map IAM condition operator strings to their Python constant names
CONDITION_OPERATOR_MAP: dict[str, str] = {
    # String conditions
    "StringEquals": "STRING_EQUALS",
    "StringNotEquals": "STRING_NOT_EQUALS",
    "StringEqualsIgnoreCase": "ConditionOperator.STRING_EQUALS_IGNORE_CASE",
    "StringNotEqualsIgnoreCase": "ConditionOperator.STRING_NOT_EQUALS_IGNORE_CASE",
    "StringLike": "STRING_LIKE",
    "StringNotLike": "STRING_NOT_LIKE",
    # Numeric conditions
    "NumericEquals": "ConditionOperator.NUMERIC_EQUALS",
    "NumericNotEquals": "ConditionOperator.NUMERIC_NOT_EQUALS",
    "NumericLessThan": "ConditionOperator.NUMERIC_LESS_THAN",
    "NumericLessThanEquals": "ConditionOperator.NUMERIC_LESS_THAN_EQUALS",
    "NumericGreaterThan": "ConditionOperator.NUMERIC_GREATER_THAN",
    "NumericGreaterThanEquals": "ConditionOperator.NUMERIC_GREATER_THAN_EQUALS",
    # Date conditions
    "DateEquals": "ConditionOperator.DATE_EQUALS",
    "DateNotEquals": "ConditionOperator.DATE_NOT_EQUALS",
    "DateLessThan": "ConditionOperator.DATE_LESS_THAN",
    "DateLessThanEquals": "ConditionOperator.DATE_LESS_THAN_EQUALS",
    "DateGreaterThan": "ConditionOperator.DATE_GREATER_THAN",
    "DateGreaterThanEquals": "ConditionOperator.DATE_GREATER_THAN_EQUALS",
    # Boolean
    "Bool": "BOOL",
    # Binary
    "BinaryEquals": "ConditionOperator.BINARY_EQUALS",
    # IP Address
    "IpAddress": "IP_ADDRESS",
    "NotIpAddress": "ConditionOperator.NOT_IP_ADDRESS",
    # ARN conditions
    "ArnEquals": "ARN_EQUALS",
    "ArnNotEquals": "ConditionOperator.ARN_NOT_EQUALS",
    "ArnLike": "ARN_LIKE",
    "ArnNotLike": "ConditionOperator.ARN_NOT_LIKE",
    # Null check
    "Null": "ConditionOperator.NULL",
    # IfExists variants
    "StringEqualsIfExists": "ConditionOperator.STRING_EQUALS_IF_EXISTS",
    "StringNotEqualsIfExists": "ConditionOperator.STRING_NOT_EQUALS_IF_EXISTS",
    "StringLikeIfExists": "ConditionOperator.STRING_LIKE_IF_EXISTS",
    "StringNotLikeIfExists": "ConditionOperator.STRING_NOT_LIKE_IF_EXISTS",
    "NumericEqualsIfExists": "ConditionOperator.NUMERIC_EQUALS_IF_EXISTS",
    "BoolIfExists": "ConditionOperator.BOOL_IF_EXISTS",
    "IpAddressIfExists": "ConditionOperator.IP_ADDRESS_IF_EXISTS",
    "ArnEqualsIfExists": "ConditionOperator.ARN_EQUALS_IF_EXISTS",
    "ArnLikeIfExists": "ConditionOperator.ARN_LIKE_IF_EXISTS",
    # ForAllValues and ForAnyValue set operators
    "ForAllValues:StringEquals": "ConditionOperator.FOR_ALL_VALUES_STRING_EQUALS",
    "ForAllValues:StringLike": "ConditionOperator.FOR_ALL_VALUES_STRING_LIKE",
    "ForAnyValue:StringEquals": "ConditionOperator.FOR_ANY_VALUE_STRING_EQUALS",
    "ForAnyValue:StringLike": "ConditionOperator.FOR_ANY_VALUE_STRING_LIKE",
    "ForAllValues:ArnLike": "ConditionOperator.FOR_ALL_VALUES_ARN_LIKE",
    "ForAnyValue:ArnLike": "ConditionOperator.FOR_ANY_VALUE_ARN_LIKE",
}

# Reverse map: constant name -> string value (for linting)
CONDITION_OPERATOR_REVERSE_MAP: dict[str, str] = {v: k for k, v in CONDITION_OPERATOR_MAP.items()}


# =============================================================================
# Pseudo-Parameter Mappings
# =============================================================================

# Map AWS pseudo-parameter strings to their Python constant names
PSEUDO_PARAMETER_MAP: dict[str, str] = {
    "AWS::AccountId": "AWS_ACCOUNT_ID",
    "AWS::NotificationARNs": "AWS_NOTIFICATION_ARNS",
    "AWS::NoValue": "AWS_NO_VALUE",
    "AWS::Partition": "AWS_PARTITION",
    "AWS::Region": "AWS_REGION",
    "AWS::StackId": "AWS_STACK_ID",
    "AWS::StackName": "AWS_STACK_NAME",
    "AWS::URLSuffix": "AWS_URL_SUFFIX",
}

# Reverse map: constant name -> pseudo-parameter string
PSEUDO_PARAMETER_REVERSE_MAP: dict[str, str] = {v: k for k, v in PSEUDO_PARAMETER_MAP.items()}


# =============================================================================
# Parameter Type Mappings
# =============================================================================

# Map CloudFormation parameter type strings to their Python constant names
PARAMETER_TYPE_MAP: dict[str, str] = {
    # Basic types
    "String": "STRING",
    "Number": "NUMBER",
    "List<Number>": "ParameterType.LIST_NUMBER",
    "CommaDelimitedList": "ParameterType.COMMA_DELIMITED_LIST",
    # EC2 types
    "AWS::EC2::AvailabilityZone::Name": "ParameterType.AWS_EC2_AVAILABILITY_ZONE_NAME",
    "AWS::EC2::Image::Id": "ParameterType.AWS_EC2_IMAGE_ID",
    "AWS::EC2::Instance::Id": "ParameterType.AWS_EC2_INSTANCE_ID",
    "AWS::EC2::KeyPair::KeyName": "ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME",
    "AWS::EC2::SecurityGroup::GroupName": "ParameterType.AWS_EC2_SECURITY_GROUP_GROUP_NAME",
    "AWS::EC2::SecurityGroup::Id": "ParameterType.AWS_EC2_SECURITY_GROUP_ID",
    "AWS::EC2::Subnet::Id": "ParameterType.AWS_EC2_SUBNET_ID",
    "AWS::EC2::Volume::Id": "ParameterType.AWS_EC2_VOLUME_ID",
    "AWS::EC2::VPC::Id": "ParameterType.AWS_EC2_VPC_ID",
    # Route53
    "AWS::Route53::HostedZone::Id": "ParameterType.AWS_ROUTE53_HOSTED_ZONE_ID",
    # List types
    "List<AWS::EC2::AvailabilityZone::Name>": "ParameterType.LIST_AWS_EC2_AVAILABILITY_ZONE_NAME",
    "List<AWS::EC2::Image::Id>": "ParameterType.LIST_AWS_EC2_IMAGE_ID",
    "List<AWS::EC2::Instance::Id>": "ParameterType.LIST_AWS_EC2_INSTANCE_ID",
    "List<AWS::EC2::SecurityGroup::GroupName>": (
        "ParameterType.LIST_AWS_EC2_SECURITY_GROUP_GROUP_NAME"
    ),
    "List<AWS::EC2::SecurityGroup::Id>": "ParameterType.LIST_AWS_EC2_SECURITY_GROUP_ID",
    "List<AWS::EC2::Subnet::Id>": "ParameterType.LIST_AWS_EC2_SUBNET_ID",
    "List<AWS::EC2::Volume::Id>": "ParameterType.LIST_AWS_EC2_VOLUME_ID",
    "List<AWS::EC2::VPC::Id>": "ParameterType.LIST_AWS_EC2_VPC_ID",
    "List<AWS::Route53::HostedZone::Id>": "ParameterType.LIST_AWS_ROUTE53_HOSTED_ZONE_ID",
    # SSM types
    "AWS::SSM::Parameter::Name": "ParameterType.AWS_SSM_PARAMETER_NAME",
    "AWS::SSM::Parameter::Value<String>": "ParameterType.AWS_SSM_PARAMETER_VALUE_STRING",
    "AWS::SSM::Parameter::Value<List<String>>": (
        "ParameterType.AWS_SSM_PARAMETER_VALUE_LIST_STRING"
    ),
    "AWS::SSM::Parameter::Value<CommaDelimitedList>": (
        "ParameterType.AWS_SSM_PARAMETER_VALUE_COMMA_DELIMITED_LIST"
    ),
}

# Reverse map: constant name -> parameter type string
PARAMETER_TYPE_REVERSE_MAP: dict[str, str] = {v: k for k, v in PARAMETER_TYPE_MAP.items()}
