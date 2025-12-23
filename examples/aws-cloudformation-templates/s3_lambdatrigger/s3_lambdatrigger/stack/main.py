"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaIAMRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class LambdaIAMRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIAMRoleAllowStatement0]


@cloudformation_dataclass
class LambdaIAMRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = 'arn:aws:logs:*:*:*'


@cloudformation_dataclass
class LambdaIAMRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIAMRoleAllowStatement0_1]


@cloudformation_dataclass
class LambdaIAMRolePolicy:
    resource: iam.user.Policy
    policy_name = 'root'
    policy_document = LambdaIAMRolePolicies0PolicyDocument


@cloudformation_dataclass
class LambdaIAMRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = LambdaIAMRoleAssumeRolePolicyDocument
    path = '/'
    policies = [LambdaIAMRolePolicy]


@cloudformation_dataclass
class S3TriggerLambdaFunctionCode:
    resource: lambda_.function.Code
    zip_file = """import json
def lambda_handler(event,context):
    print(event)
    return "Hello... This is a test S3 trigger Lambda Function"
"""


@cloudformation_dataclass
class S3TriggerLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    code = S3TriggerLambdaFunctionCode
    handler = 'index.lambda_handler'
    role = get_att(LambdaIAMRole, "Arn")
    runtime = 'python3.9'
    timeout = 30


@cloudformation_dataclass
class LambdaInvokePermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    function_name = get_att(S3TriggerLambdaFunction, "Arn")
    action = 'lambda:InvokeFunction'
    principal = 's3.amazonaws.com'
    source_account = AWS_ACCOUNT_ID
    source_arn = Sub('arn:${AWS::Partition}:s3:::${NotificationBucket}')


@cloudformation_dataclass
class S3BucketNotificationServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class S3BucketNotificationServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = S3BucketNotificationServerSideEncryptionByDefault


@cloudformation_dataclass
class S3BucketNotificationBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [S3BucketNotificationServerSideEncryptionRule]


@cloudformation_dataclass
class S3BucketNotificationPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class S3BucketNotificationLambdaConfiguration:
    resource: s3.bucket.LambdaConfiguration
    event = 's3:ObjectCreated:Put'
    function = get_att(S3TriggerLambdaFunction, "Arn")


@cloudformation_dataclass
class S3BucketNotificationNotificationConfiguration:
    resource: s3.bucket.NotificationConfiguration
    lambda_configurations = [S3BucketNotificationLambdaConfiguration]


@cloudformation_dataclass
class S3BucketNotification:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = Sub('${NotificationBucket}')
    bucket_encryption = S3BucketNotificationBucketEncryption
    public_access_block_configuration = S3BucketNotificationPublicAccessBlockConfiguration
    notification_configuration = S3BucketNotificationNotificationConfiguration
    depends_on = ["LambdaInvokePermission"]
