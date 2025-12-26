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
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import iam, kms, s3
from cloudformation_dataclasses.aws.s3 import ReplicationRuleStatus, ServerSideEncryption
from cloudformation_dataclasses.intrinsics import Sub

from .params import AccountIdDestination as AccountIdDestination
from .security import KmsKey as KmsKey
from .security import KmsKeyAlias as KmsKeyAlias
from .security import KmsKeyAllowStatement0 as KmsKeyAllowStatement0
from .security import KmsKeyKeyPolicy as KmsKeyKeyPolicy
from .security import ReplicationRole as ReplicationRole
from .security import ReplicationRoleAllowStatement0 as ReplicationRoleAllowStatement0
from .security import ReplicationRoleAllowStatement0_1 as ReplicationRoleAllowStatement0_1
from .security import ReplicationRoleAllowStatement1 as ReplicationRoleAllowStatement1
from .security import ReplicationRoleAllowStatement2 as ReplicationRoleAllowStatement2
from .security import ReplicationRoleAllowStatement3 as ReplicationRoleAllowStatement3
from .security import ReplicationRoleAssumeRolePolicyDocument as ReplicationRoleAssumeRolePolicyDocument
from .security import ReplicationRolePolicies0PolicyDocument as ReplicationRolePolicies0PolicyDocument
from .security import ReplicationRolePolicy as ReplicationRolePolicy
from .storage import S3BucketSource as S3BucketSource
from .storage import S3BucketSourceAccessControlTranslation as S3BucketSourceAccessControlTranslation
from .storage import S3BucketSourceBucketEncryption as S3BucketSourceBucketEncryption
from .storage import S3BucketSourceDeleteMarkerReplication as S3BucketSourceDeleteMarkerReplication
from .storage import S3BucketSourceDeleteMarkerReplication1 as S3BucketSourceDeleteMarkerReplication1
from .storage import S3BucketSourceEncryptionConfiguration as S3BucketSourceEncryptionConfiguration
from .storage import S3BucketSourcePublicAccessBlockConfiguration as S3BucketSourcePublicAccessBlockConfiguration
from .storage import S3BucketSourceReplicationConfiguration as S3BucketSourceReplicationConfiguration
from .storage import S3BucketSourceReplicationDestination as S3BucketSourceReplicationDestination
from .storage import S3BucketSourceReplicationRule as S3BucketSourceReplicationRule
from .storage import S3BucketSourceReplicationRuleFilter as S3BucketSourceReplicationRuleFilter
from .storage import S3BucketSourceServerSideEncryptionByDefault as S3BucketSourceServerSideEncryptionByDefault
from .storage import S3BucketSourceServerSideEncryptionRule as S3BucketSourceServerSideEncryptionRule
from .storage import S3BucketSourceSourceSelectionCriteria as S3BucketSourceSourceSelectionCriteria
from .storage import S3BucketSourceSseKmsEncryptedObjects as S3BucketSourceSseKmsEncryptedObjects

__all__: list[str] = ['AccountIdDestination', 'KmsKey', 'KmsKeyAlias', 'KmsKeyAllowStatement0', 'KmsKeyKeyPolicy', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'ReplicationRole', 'ReplicationRoleAllowStatement0', 'ReplicationRoleAllowStatement0_1', 'ReplicationRoleAllowStatement1', 'ReplicationRoleAllowStatement2', 'ReplicationRoleAllowStatement3', 'ReplicationRoleAssumeRolePolicyDocument', 'ReplicationRolePolicies0PolicyDocument', 'ReplicationRolePolicy', 'ReplicationRuleStatus', 'S3BucketSource', 'S3BucketSourceAccessControlTranslation', 'S3BucketSourceBucketEncryption', 'S3BucketSourceDeleteMarkerReplication', 'S3BucketSourceDeleteMarkerReplication1', 'S3BucketSourceEncryptionConfiguration', 'S3BucketSourcePublicAccessBlockConfiguration', 'S3BucketSourceReplicationConfiguration', 'S3BucketSourceReplicationDestination', 'S3BucketSourceReplicationRule', 'S3BucketSourceReplicationRuleFilter', 'S3BucketSourceServerSideEncryptionByDefault', 'S3BucketSourceServerSideEncryptionRule', 'S3BucketSourceSourceSelectionCriteria', 'S3BucketSourceSseKmsEncryptedObjects', 'STRING', 'STRING_EQUALS', 'ServerSideEncryption', 'Sub', 'Template', 'cloudformation_dataclass', 'get_att', 'iam', 'kms', 'ref', 's3', 'setup_resources']
