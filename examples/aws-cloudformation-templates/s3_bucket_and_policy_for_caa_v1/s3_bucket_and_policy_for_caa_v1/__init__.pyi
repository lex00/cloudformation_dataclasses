"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    BOOL,
    DenyStatement,
    Output,
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
from cloudformation_dataclasses.aws import s3
from cloudformation_dataclasses.aws.s3 import ServerSideEncryption
from cloudformation_dataclasses.intrinsics import Sub

from .outputs import BucketOutput as BucketOutput
from .outputs import BucketPolicyOutput as BucketPolicyOutput
from .params import BucketName as BucketName
from .params import PublisherAccountID as PublisherAccountID
from .storage import Bucket as Bucket
from .storage import BucketBucketEncryption as BucketBucketEncryption
from .storage import BucketDeleteMarkerReplication as BucketDeleteMarkerReplication
from .storage import BucketPolicy as BucketPolicy
from .storage import BucketPolicyAllowStatement0 as BucketPolicyAllowStatement0
from .storage import BucketPolicyAllowStatement1 as BucketPolicyAllowStatement1
from .storage import BucketPolicyDenyStatement2 as BucketPolicyDenyStatement2
from .storage import BucketPolicyPolicyDocument as BucketPolicyPolicyDocument
from .storage import BucketPublicAccessBlockConfiguration as BucketPublicAccessBlockConfiguration
from .storage import BucketServerSideEncryptionByDefault as BucketServerSideEncryptionByDefault
from .storage import BucketServerSideEncryptionRule as BucketServerSideEncryptionRule

__all__: list[str] = ['BOOL', 'Bucket', 'BucketBucketEncryption', 'BucketDeleteMarkerReplication', 'BucketName', 'BucketOutput', 'BucketPolicy', 'BucketPolicyAllowStatement0', 'BucketPolicyAllowStatement1', 'BucketPolicyDenyStatement2', 'BucketPolicyOutput', 'BucketPolicyPolicyDocument', 'BucketPublicAccessBlockConfiguration', 'BucketServerSideEncryptionByDefault', 'BucketServerSideEncryptionRule', 'DenyStatement', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PublisherAccountID', 'STRING', 'ServerSideEncryption', 'Sub', 'Template', 'cloudformation_dataclass', 'get_att', 'ref', 's3', 'setup_resources']
