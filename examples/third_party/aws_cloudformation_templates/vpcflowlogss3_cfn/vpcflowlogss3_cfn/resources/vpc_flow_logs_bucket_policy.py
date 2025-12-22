from __future__ import annotations

"""VPCFlowLogsBucketPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsBucketPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'AWSLogDeliveryWrite'
    principal = {
        'Service': 'delivery.logs.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}/*')
    condition = {
        STRING_EQUALS: {
            's3:x-amz-acl': 'bucket-owner-full-control',
        },
    }


@cloudformation_dataclass
class VPCFlowLogsBucketPolicyAllowStatement1:
    resource: PolicyStatement
    sid = 'AWSLogDeliveryAclCheck'
    principal = {
        'Service': 'delivery.logs.amazonaws.com',
    }
    action = 's3:GetBucketAcl'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}')


@cloudformation_dataclass
class VPCFlowLogsBucketPolicyDenyStatement2:
    resource: DenyStatement
    sid = 'DenyNonSSLRequests'
    principal = '*'
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}'),
        Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class VPCFlowLogsBucketPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [VPCFlowLogsBucketPolicyAllowStatement0, VPCFlowLogsBucketPolicyAllowStatement1, VPCFlowLogsBucketPolicyDenyStatement2]


@cloudformation_dataclass
class VPCFlowLogsBucketPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: BucketPolicy
    bucket: Ref[VPCFlowLogsBucket] = ref()
    policy_document = VPCFlowLogsBucketPolicyPolicyDocument
    condition = 'VPCFlowLogsNewBucketCondition'
