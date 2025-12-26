"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    BOOL,
    DenyStatement,
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
from cloudformation_dataclasses.aws import kms, s3
from cloudformation_dataclasses.aws.s3 import ServerSideEncryption
from cloudformation_dataclasses.intrinsics import Sub

from .params import AccountIdSource as AccountIdSource
from .security import KmsKey as KmsKey
from .security import KmsKeyAlias as KmsKeyAlias
from .security import KmsKeyAllowStatement0 as KmsKeyAllowStatement0
from .security import KmsKeyAllowStatement1 as KmsKeyAllowStatement1
from .security import KmsKeyKeyPolicy as KmsKeyKeyPolicy
from .storage import S3BucketDestination as S3BucketDestination
from .storage import S3BucketDestinationBucketEncryption as S3BucketDestinationBucketEncryption
from .storage import S3BucketDestinationDeleteMarkerReplication as S3BucketDestinationDeleteMarkerReplication
from .storage import S3BucketDestinationPolicy as S3BucketDestinationPolicy
from .storage import S3BucketDestinationPolicyAllowStatement0 as S3BucketDestinationPolicyAllowStatement0
from .storage import S3BucketDestinationPolicyDenyStatement1 as S3BucketDestinationPolicyDenyStatement1
from .storage import S3BucketDestinationPolicyPolicyDocument as S3BucketDestinationPolicyPolicyDocument
from .storage import S3BucketDestinationPublicAccessBlockConfiguration as S3BucketDestinationPublicAccessBlockConfiguration
from .storage import S3BucketDestinationServerSideEncryptionByDefault as S3BucketDestinationServerSideEncryptionByDefault
from .storage import S3BucketDestinationServerSideEncryptionRule as S3BucketDestinationServerSideEncryptionRule

__all__: list[str] = ['AccountIdSource', 'BOOL', 'DenyStatement', 'KmsKey', 'KmsKeyAlias', 'KmsKeyAllowStatement0', 'KmsKeyAllowStatement1', 'KmsKeyKeyPolicy', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'S3BucketDestination', 'S3BucketDestinationBucketEncryption', 'S3BucketDestinationDeleteMarkerReplication', 'S3BucketDestinationPolicy', 'S3BucketDestinationPolicyAllowStatement0', 'S3BucketDestinationPolicyDenyStatement1', 'S3BucketDestinationPolicyPolicyDocument', 'S3BucketDestinationPublicAccessBlockConfiguration', 'S3BucketDestinationServerSideEncryptionByDefault', 'S3BucketDestinationServerSideEncryptionRule', 'STRING', 'ServerSideEncryption', 'Sub', 'Template', 'cloudformation_dataclass', 'get_att', 'kms', 'ref', 's3', 'setup_resources']
