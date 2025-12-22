from __future__ import annotations

"""NeptuneCloudWatchPolicy - AWS::IAM::ManagedPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneCloudWatchPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'EnableLogGroups'
    action = [
        'logs:CreateLogGroup',
        'logs:PutRetentionPolicy',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:logs:*:*:log-group:/aws/neptune/*')]


@cloudformation_dataclass
class NeptuneCloudWatchPolicyAllowStatement1:
    resource: PolicyStatement
    sid = 'EnableLogStreams'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'logs:DescribeLogStreams',
        'logs:GetLogEvents',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:logs:*:*:log-group:/aws/neptune/*:log-stream:*')]


@cloudformation_dataclass
class NeptuneCloudWatchPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneCloudWatchPolicyAllowStatement0, NeptuneCloudWatchPolicyAllowStatement1]


@cloudformation_dataclass
class NeptuneCloudWatchPolicy:
    """AWS::IAM::ManagedPolicy resource."""

    resource: ManagedPolicy
    description = 'Default policy for CloudWatch logs'
    managed_policy_name = Sub('${Env}-${AppName}-neptune-cw-policy-${AWS::Region}')
    policy_document = NeptuneCloudWatchPolicyPolicyDocument
