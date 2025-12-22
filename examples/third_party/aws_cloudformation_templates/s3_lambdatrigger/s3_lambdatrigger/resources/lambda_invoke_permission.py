"""LambdaInvokePermission - AWS::Lambda::Permission resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaInvokePermission:
    """AWS::Lambda::Permission resource."""

    resource: Permission
    function_name = get_att(S3TriggerLambdaFunction, "Arn")
    action = 'lambda:InvokeFunction'
    principal = 's3.amazonaws.com'
    source_account = AWS_ACCOUNT_ID
    source_arn = Sub('arn:${AWS::Partition}:s3:::${NotificationBucket}')
