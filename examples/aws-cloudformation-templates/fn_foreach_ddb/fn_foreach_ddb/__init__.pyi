"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
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
from cloudformation_dataclasses.aws import (
    config,
    ec2,
    iam,
    lambda_,
    s3,
    sns,
)
from cloudformation_dataclasses.aws.config import ConfigRule, ConfigurationRecorder
from cloudformation_dataclasses.aws.s3 import ServerSideEncryption
from cloudformation_dataclasses.aws.sns import TopicPolicy
from cloudformation_dataclasses.intrinsics import (
    AWS_ACCOUNT_ID,
    Equals,
    GetAZs,
    Join,
    Select,
)

from .compute import ConfigPermissionToCallLambda as ConfigPermissionToCallLambda
from .compute import Ec2Volume as Ec2Volume
from .compute import Ec2VolumeAssociationParameter as Ec2VolumeAssociationParameter
from .compute import VolumeAutoEnableIOComplianceCheck as VolumeAutoEnableIOComplianceCheck
from .compute import VolumeAutoEnableIOComplianceCheckCode as VolumeAutoEnableIOComplianceCheckCode
from .infra import ConfigRecorder as ConfigRecorder
from .infra import ConfigRecorderExclusionByResourceTypes as ConfigRecorderExclusionByResourceTypes
from .infra import ConfigRuleForVolumeAutoEnableIO as ConfigRuleForVolumeAutoEnableIO
from .infra import ConfigRuleForVolumeAutoEnableIOScope as ConfigRuleForVolumeAutoEnableIOScope
from .infra import ConfigRuleForVolumeAutoEnableIOSource as ConfigRuleForVolumeAutoEnableIOSource
from .infra import ConfigRuleForVolumeAutoEnableIOSourceDetail as ConfigRuleForVolumeAutoEnableIOSourceDetail
from .infra import ConfigRuleForVolumeTags as ConfigRuleForVolumeTags
from .infra import ConfigRuleForVolumeTagsScope as ConfigRuleForVolumeTagsScope
from .infra import ConfigRuleForVolumeTagsSource as ConfigRuleForVolumeTagsSource
from .infra import DeliveryChannel as DeliveryChannel
from .infra import DeliveryChannelConfigSnapshotDeliveryProperties as DeliveryChannelConfigSnapshotDeliveryProperties
from .messaging import ConfigTopic as ConfigTopic
from .messaging import ConfigTopicPolicy as ConfigTopicPolicy
from .messaging import ConfigTopicPolicyAllowStatement0 as ConfigTopicPolicyAllowStatement0
from .messaging import ConfigTopicPolicyPolicyDocument as ConfigTopicPolicyPolicyDocument
from .outputs import ConfigRuleForVolumeAutoEnableIOComplianceTypeOutput as ConfigRuleForVolumeAutoEnableIOComplianceTypeOutput
from .outputs import ConfigRuleForVolumeTagsArnOutput as ConfigRuleForVolumeTagsArnOutput
from .outputs import ConfigRuleForVolumeTagsConfigRuleIdOutput as ConfigRuleForVolumeTagsConfigRuleIdOutput
from .params import CreateDeliveryChannelCondition as CreateDeliveryChannelCondition
from .params import DeliveryChannelExists as DeliveryChannelExists
from .params import Ec2VolumeAutoEnableIO as Ec2VolumeAutoEnableIO
from .params import Ec2VolumeTagKey as Ec2VolumeTagKey
from .security import ConfigRole as ConfigRole
from .security import ConfigRoleAllowStatement0 as ConfigRoleAllowStatement0
from .security import ConfigRoleAllowStatement0_1 as ConfigRoleAllowStatement0_1
from .security import ConfigRoleAllowStatement1 as ConfigRoleAllowStatement1
from .security import ConfigRoleAllowStatement2 as ConfigRoleAllowStatement2
from .security import ConfigRoleAssumeRolePolicyDocument as ConfigRoleAssumeRolePolicyDocument
from .security import ConfigRolePolicies0PolicyDocument as ConfigRolePolicies0PolicyDocument
from .security import ConfigRolePolicy as ConfigRolePolicy
from .security import LambdaExecutionRole as LambdaExecutionRole
from .security import LambdaExecutionRoleAllowStatement0 as LambdaExecutionRoleAllowStatement0
from .security import LambdaExecutionRoleAllowStatement0_1 as LambdaExecutionRoleAllowStatement0_1
from .security import LambdaExecutionRoleAssumeRolePolicyDocument as LambdaExecutionRoleAssumeRolePolicyDocument
from .security import LambdaExecutionRolePolicies0PolicyDocument as LambdaExecutionRolePolicies0PolicyDocument
from .security import LambdaExecutionRolePolicy as LambdaExecutionRolePolicy
from .storage import ConfigBucket as ConfigBucket
from .storage import ConfigBucketBucketEncryption as ConfigBucketBucketEncryption
from .storage import ConfigBucketPublicAccessBlockConfiguration as ConfigBucketPublicAccessBlockConfiguration
from .storage import ConfigBucketServerSideEncryptionByDefault as ConfigBucketServerSideEncryptionByDefault
from .storage import ConfigBucketServerSideEncryptionRule as ConfigBucketServerSideEncryptionRule

__all__: list[str] = ['AWS_ACCOUNT_ID', 'ConfigBucket', 'ConfigBucketBucketEncryption', 'ConfigBucketPublicAccessBlockConfiguration', 'ConfigBucketServerSideEncryptionByDefault', 'ConfigBucketServerSideEncryptionRule', 'ConfigPermissionToCallLambda', 'ConfigRecorder', 'ConfigRecorderExclusionByResourceTypes', 'ConfigRole', 'ConfigRoleAllowStatement0', 'ConfigRoleAllowStatement0_1', 'ConfigRoleAllowStatement1', 'ConfigRoleAllowStatement2', 'ConfigRoleAssumeRolePolicyDocument', 'ConfigRolePolicies0PolicyDocument', 'ConfigRolePolicy', 'ConfigRule', 'ConfigRuleForVolumeAutoEnableIO', 'ConfigRuleForVolumeAutoEnableIOComplianceTypeOutput', 'ConfigRuleForVolumeAutoEnableIOScope', 'ConfigRuleForVolumeAutoEnableIOSource', 'ConfigRuleForVolumeAutoEnableIOSourceDetail', 'ConfigRuleForVolumeTags', 'ConfigRuleForVolumeTagsArnOutput', 'ConfigRuleForVolumeTagsConfigRuleIdOutput', 'ConfigRuleForVolumeTagsScope', 'ConfigRuleForVolumeTagsSource', 'ConfigTopic', 'ConfigTopicPolicy', 'ConfigTopicPolicyAllowStatement0', 'ConfigTopicPolicyPolicyDocument', 'ConfigurationRecorder', 'CreateDeliveryChannelCondition', 'DeliveryChannel', 'DeliveryChannelConfigSnapshotDeliveryProperties', 'DeliveryChannelExists', 'Ec2Volume', 'Ec2VolumeAssociationParameter', 'Ec2VolumeAutoEnableIO', 'Ec2VolumeTagKey', 'Equals', 'GetAZs', 'Join', 'LambdaExecutionRole', 'LambdaExecutionRoleAllowStatement0', 'LambdaExecutionRoleAllowStatement0_1', 'LambdaExecutionRoleAssumeRolePolicyDocument', 'LambdaExecutionRolePolicies0PolicyDocument', 'LambdaExecutionRolePolicy', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'STRING', 'STRING_EQUALS', 'Select', 'ServerSideEncryption', 'Template', 'TemplateCondition', 'TopicPolicy', 'VolumeAutoEnableIOComplianceCheck', 'VolumeAutoEnableIOComplianceCheckCode', 'cloudformation_dataclass', 'config', 'ec2', 'get_att', 'iam', 'lambda_', 'ref', 's3', 'setup_resources', 'sns']
