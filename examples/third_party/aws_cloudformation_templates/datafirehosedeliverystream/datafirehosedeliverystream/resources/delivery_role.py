"""DeliveryRole - AWS::IAM::Role resource."""

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
class DeliveryRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        's3:AbortMultipartUpload',
        's3:GetBucketLocation',
        's3:GetObject',
        's3:ListBucket',
        's3:ListBucketMultipartUploads',
        's3:PutObject',
    ]
    resource_arn = [
        Join('', [
    'arn:aws:s3:::',
    ref(DestinationBucketName),
]),
        Join('', [
    'arn:aws:s3:::',
    ref(DestinationBucketName),
    '/*',
]),
    ]


@cloudformation_dataclass
class DeliveryRoleAllowStatement1:
    resource: PolicyStatement
    action = ['logs:PutLogEvents']
    resource_arn = Join('', [
    Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/kinesisfirehose/'),
    ref(LogGroupName),
    ':*',
])


@cloudformation_dataclass
class DeliveryRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [DeliveryRoleAllowStatement0_1, DeliveryRoleAllowStatement1]


@cloudformation_dataclass
class DeliveryRolePolicy:
    resource: iam.Policy
    policy_name = 'firehose_delivery_policy'
    policy_document = DeliveryRolePolicies0PolicyDocument


@cloudformation_dataclass
class DeliveryRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = DeliveryRoleAssumeRolePolicyDocument
    path = '/'
    policies = [DeliveryRolePolicy]
