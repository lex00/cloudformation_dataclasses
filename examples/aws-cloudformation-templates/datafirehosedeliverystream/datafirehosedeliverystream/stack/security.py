"""Security resources: DeliveryRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DeliveryRoleAllowStatement0:
    resource: PolicyStatement
    sid = ''
    principal = {
        'Service': 'firehose.amazonaws.com',
    }
    action = 'sts:AssumeRole'
    condition = {
        STRING_EQUALS: {
            'sts:ExternalId': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class DeliveryRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DeliveryRoleAllowStatement0]


@cloudformation_dataclass
class DeliveryRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = DeliveryRoleAssumeRolePolicyDocument
    path = '/'
    policies = [{
        'PolicyName': 'firehose_delivery_policy',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Effect': 'Allow',
                    'Action': [
                        's3:AbortMultipartUpload',
                        's3:GetBucketLocation',
                        's3:GetObject',
                        's3:ListBucket',
                        's3:ListBucketMultipartUploads',
                        's3:PutObject',
                    ],
                    'Resource': [
                        Join('', [
    'arn:aws:s3:::',
    ref(DestinationBucketName),
]),
                        Join('', [
    'arn:aws:s3:::',
    ref(DestinationBucketName),
    '/*',
]),
                    ],
                },
                {
                    'Effect': 'Allow',
                    'Action': ['logs:PutLogEvents'],
                    'Resource': Join('', [
    Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/kinesisfirehose/'),
    ref(LogGroupName),
    ':*',
]),
                },
            ],
        },
    }]
