"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class OUID:
    resource: Parameter
    type = STRING
    default = 'ou-qxtx-vv0thlla'


@cloudformation_dataclass
class KmsKeyId:
    """The ID of an AWS Key Management Service (KMS) for Amazon SQS, or a custom KMS. To use the AWS managed KMS for Amazon SQS, specify a (default) alias ARN, alias name (for example alias/aws/sqs), key ARN, or key ID"""

    resource: Parameter
    type = STRING
    description = 'The ID of an AWS Key Management Service (KMS) for Amazon SQS, or a custom KMS. To use the AWS managed KMS for Amazon SQS, specify a (default) alias ARN, alias name (for example alias/aws/sqs), key ARN, or key ID'
    default = 'alias/aws/sqs'


@cloudformation_dataclass
class StackSetRegions:
    """AWS Regions where stack instances should be deployed in target accounts"""

    resource: Parameter
    type = ParameterType.COMMA_DELIMITED_LIST
    description = 'AWS Regions where stack instances should be deployed in target accounts'
    default = 'us-east-1,eu-west-1'
