"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    BOOL,
    DenyStatement,
    Output,
    Parameter,
    ParameterType,
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
from cloudformation_dataclasses.aws import ec2, s3
from cloudformation_dataclasses.aws.s3.bucket import LoggingConfiguration
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    Equals,
    If,
    Not,
    Sub,
)

from .compute import VPCFlowLogstoS3 as VPCFlowLogstoS3
from .compute import VPCFlowLogstoS3AssociationParameter as VPCFlowLogstoS3AssociationParameter
from .outputs import VPCFlowLogsBucketOutput as VPCFlowLogsBucketOutput
from .params import S3AccessLogsBucketName as S3AccessLogsBucketName
from .params import S3AccessLogsConditionCondition as S3AccessLogsConditionCondition
from .params import VPCFlowLogsBucketKMSKey as VPCFlowLogsBucketKMSKey
from .params import VPCFlowLogsBucketKMSKeyConditionCondition as VPCFlowLogsBucketKMSKeyConditionCondition
from .params import VPCFlowLogsBucketKeyEnabled as VPCFlowLogsBucketKeyEnabled
from .params import VPCFlowLogsBucketName as VPCFlowLogsBucketName
from .params import VPCFlowLogsLogFormat as VPCFlowLogsLogFormat
from .params import VPCFlowLogsMaxAggregationInterval as VPCFlowLogsMaxAggregationInterval
from .params import VPCFlowLogsNewBucketConditionCondition as VPCFlowLogsNewBucketConditionCondition
from .params import VPCFlowLogsTrafficType as VPCFlowLogsTrafficType
from .params import VPCID as VPCID
from .storage import VPCFlowLogsBucket as VPCFlowLogsBucket
from .storage import VPCFlowLogsBucketBucketEncryption as VPCFlowLogsBucketBucketEncryption
from .storage import VPCFlowLogsBucketDeleteMarkerReplication as VPCFlowLogsBucketDeleteMarkerReplication
from .storage import VPCFlowLogsBucketPolicy as VPCFlowLogsBucketPolicy
from .storage import VPCFlowLogsBucketPolicyAllowStatement0 as VPCFlowLogsBucketPolicyAllowStatement0
from .storage import VPCFlowLogsBucketPolicyAllowStatement1 as VPCFlowLogsBucketPolicyAllowStatement1
from .storage import VPCFlowLogsBucketPolicyDenyStatement2 as VPCFlowLogsBucketPolicyDenyStatement2
from .storage import VPCFlowLogsBucketPolicyPolicyDocument as VPCFlowLogsBucketPolicyPolicyDocument
from .storage import VPCFlowLogsBucketPublicAccessBlockConfiguration as VPCFlowLogsBucketPublicAccessBlockConfiguration
from .storage import VPCFlowLogsBucketServerSideEncryptionByDefault as VPCFlowLogsBucketServerSideEncryptionByDefault
from .storage import VPCFlowLogsBucketServerSideEncryptionRule as VPCFlowLogsBucketServerSideEncryptionRule

__all__: list[str] = ['AWS_NO_VALUE', 'BOOL', 'DenyStatement', 'Equals', 'If', 'LoggingConfiguration', 'Not', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'S3AccessLogsBucketName', 'S3AccessLogsConditionCondition', 'STRING', 'STRING_EQUALS', 'Sub', 'Template', 'TemplateCondition', 'VPCFlowLogsBucket', 'VPCFlowLogsBucketBucketEncryption', 'VPCFlowLogsBucketDeleteMarkerReplication', 'VPCFlowLogsBucketKMSKey', 'VPCFlowLogsBucketKMSKeyConditionCondition', 'VPCFlowLogsBucketKeyEnabled', 'VPCFlowLogsBucketName', 'VPCFlowLogsBucketOutput', 'VPCFlowLogsBucketPolicy', 'VPCFlowLogsBucketPolicyAllowStatement0', 'VPCFlowLogsBucketPolicyAllowStatement1', 'VPCFlowLogsBucketPolicyDenyStatement2', 'VPCFlowLogsBucketPolicyPolicyDocument', 'VPCFlowLogsBucketPublicAccessBlockConfiguration', 'VPCFlowLogsBucketServerSideEncryptionByDefault', 'VPCFlowLogsBucketServerSideEncryptionRule', 'VPCFlowLogsLogFormat', 'VPCFlowLogsMaxAggregationInterval', 'VPCFlowLogsNewBucketConditionCondition', 'VPCFlowLogsTrafficType', 'VPCFlowLogstoS3', 'VPCFlowLogstoS3AssociationParameter', 'VPCID', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 's3', 'setup_resources']
