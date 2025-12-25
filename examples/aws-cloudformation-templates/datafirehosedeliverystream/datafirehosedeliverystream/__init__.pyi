"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    PolicyDocument,
    PolicyStatement,
    STRING,
    STRING_EQUALS,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import iam, kinesisfirehose, logs
from cloudformation_dataclasses.intrinsics import (
    AWS_ACCOUNT_ID,
    AWS_NO_VALUE,
    Equals,
    If,
    Join,
    Not,
    Sub,
)
from .params import *  # noqa: F403, F401

from .main import DeliveryStream as DeliveryStream
from .main import DeliveryStreamCloudWatchLoggingOptions as DeliveryStreamCloudWatchLoggingOptions
from .main import DeliveryStreamDeliveryStreamEncryptionConfigurationInput as DeliveryStreamDeliveryStreamEncryptionConfigurationInput
from .main import DeliveryStreamExtendedS3DestinationConfiguration as DeliveryStreamExtendedS3DestinationConfiguration
from .main import DeliveryStreamProcessingConfiguration as DeliveryStreamProcessingConfiguration
from .main import DeliveryStreamProcessor as DeliveryStreamProcessor
from .main import DeliveryStreamProcessorParameter as DeliveryStreamProcessorParameter
from .monitoring import FirehoseLogGroup as FirehoseLogGroup
from .monitoring import FirehoseLogStream as FirehoseLogStream
from .params import CloudWatchLogGroupRetention as CloudWatchLogGroupRetention
from .params import CloudWatchLogsKMSKey as CloudWatchLogsKMSKey
from .params import CloudWatchLogsKMSKeyConditionCondition as CloudWatchLogsKMSKeyConditionCondition
from .params import DeliveryStreamName as DeliveryStreamName
from .params import DestinationBucketName as DestinationBucketName
from .params import LogGroupName as LogGroupName
from .params import LogStreamName as LogStreamName
from .security import DeliveryRole as DeliveryRole
from .security import DeliveryRoleAllowStatement0 as DeliveryRoleAllowStatement0
from .security import DeliveryRoleAllowStatement0_1 as DeliveryRoleAllowStatement0_1
from .security import DeliveryRoleAllowStatement1 as DeliveryRoleAllowStatement1
from .security import DeliveryRoleAssumeRolePolicyDocument as DeliveryRoleAssumeRolePolicyDocument
from .security import DeliveryRolePolicies0PolicyDocument as DeliveryRolePolicies0PolicyDocument
from .security import DeliveryRolePolicy as DeliveryRolePolicy

__all__: list[str] = ['AWS_ACCOUNT_ID', 'AWS_NO_VALUE', 'CloudWatchLogGroupRetention', 'CloudWatchLogsKMSKey', 'CloudWatchLogsKMSKeyConditionCondition', 'DeliveryRole', 'DeliveryRoleAllowStatement0', 'DeliveryRoleAllowStatement0_1', 'DeliveryRoleAllowStatement1', 'DeliveryRoleAssumeRolePolicyDocument', 'DeliveryRolePolicies0PolicyDocument', 'DeliveryRolePolicy', 'DeliveryStream', 'DeliveryStreamCloudWatchLoggingOptions', 'DeliveryStreamDeliveryStreamEncryptionConfigurationInput', 'DeliveryStreamExtendedS3DestinationConfiguration', 'DeliveryStreamName', 'DeliveryStreamProcessingConfiguration', 'DeliveryStreamProcessor', 'DeliveryStreamProcessorParameter', 'DestinationBucketName', 'Equals', 'FirehoseLogGroup', 'FirehoseLogStream', 'If', 'Join', 'LogGroupName', 'LogStreamName', 'Not', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'STRING', 'STRING_EQUALS', 'Sub', 'Template', 'TemplateCondition', 'cloudformation_dataclass', 'get_att', 'iam', 'kinesisfirehose', 'logs', 'ref', 'setup_resources']
