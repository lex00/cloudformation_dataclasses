"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class OUID:
    """The Id of the Organization Unit to deploy the stack set to."""

    resource: Parameter
    type = STRING
    description = 'The Id of the Organization Unit to deploy the stack set to.'
    default = 'ou-qxtx-vv0thlla'


@cloudformation_dataclass
class OrgID:
    """The Id of the Organization to verify the cross account API call. All accounts in this org will be granted permissions to put events onto the default event bus in this account. Note that this is not the OUID, it's the org itself and should start with o-"""

    resource: Parameter
    type = STRING
    description = "The Id of the Organization to verify the cross account API call. All accounts in this org will be granted permissions to put events onto the default event bus in this account. Note that this is not the OUID, it's the org itself and should start with o-"
    default = 'o-jhfo4fcm1s'


@cloudformation_dataclass
class CentralEventBusName:
    resource: Parameter
    type = STRING
    default = 'central-cloudformation'


@cloudformation_dataclass
class CentralEventLogName:
    resource: Parameter
    type = STRING
    default = 'central-cloudformation-logs'


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
