"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import iam, lambda_, s3
from cloudformation_dataclasses.aws.s3 import ServerSideEncryption
from cloudformation_dataclasses.intrinsics import AWS_ACCOUNT_ID, Sub
from .params import *  # noqa: F403, F401

from .compute import LambdaInvokePermission as LambdaInvokePermission
from .compute import S3TriggerLambdaFunction as S3TriggerLambdaFunction
from .compute import S3TriggerLambdaFunctionCode as S3TriggerLambdaFunctionCode
from .params import NotificationBucket as NotificationBucket
from .security import LambdaIAMRole as LambdaIAMRole
from .security import LambdaIAMRoleAllowStatement0 as LambdaIAMRoleAllowStatement0
from .security import LambdaIAMRoleAllowStatement0_1 as LambdaIAMRoleAllowStatement0_1
from .security import LambdaIAMRoleAssumeRolePolicyDocument as LambdaIAMRoleAssumeRolePolicyDocument
from .security import LambdaIAMRolePolicies0PolicyDocument as LambdaIAMRolePolicies0PolicyDocument
from .security import LambdaIAMRolePolicy as LambdaIAMRolePolicy
from .storage import S3BucketNotification as S3BucketNotification
from .storage import S3BucketNotificationBucketEncryption as S3BucketNotificationBucketEncryption
from .storage import S3BucketNotificationLambdaConfiguration as S3BucketNotificationLambdaConfiguration
from .storage import S3BucketNotificationNotificationConfiguration as S3BucketNotificationNotificationConfiguration
from .storage import S3BucketNotificationPublicAccessBlockConfiguration as S3BucketNotificationPublicAccessBlockConfiguration
from .storage import S3BucketNotificationServerSideEncryptionByDefault as S3BucketNotificationServerSideEncryptionByDefault
from .storage import S3BucketNotificationServerSideEncryptionRule as S3BucketNotificationServerSideEncryptionRule

__all__: list[str] = ['AWS_ACCOUNT_ID', 'LambdaIAMRole', 'LambdaIAMRoleAllowStatement0', 'LambdaIAMRoleAllowStatement0_1', 'LambdaIAMRoleAssumeRolePolicyDocument', 'LambdaIAMRolePolicies0PolicyDocument', 'LambdaIAMRolePolicy', 'LambdaInvokePermission', 'NotificationBucket', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'S3BucketNotification', 'S3BucketNotificationBucketEncryption', 'S3BucketNotificationLambdaConfiguration', 'S3BucketNotificationNotificationConfiguration', 'S3BucketNotificationPublicAccessBlockConfiguration', 'S3BucketNotificationServerSideEncryptionByDefault', 'S3BucketNotificationServerSideEncryptionRule', 'S3TriggerLambdaFunction', 'S3TriggerLambdaFunctionCode', 'STRING', 'ServerSideEncryption', 'Sub', 'Template', 'cloudformation_dataclass', 'get_att', 'iam', 'lambda_', 'ref', 's3', 'setup_resources']
