"""EventRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EventRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['events.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class EventRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EventRoleAllowStatement0]


@cloudformation_dataclass
class EventRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 'codepipeline:StartPipelineExecution'
    resource_arn = Join('', [
    'arn:aws:codepipeline:',
    AWS_REGION,
    ':',
    AWS_ACCOUNT_ID,
    ':',
    ref(Pipeline),
])


@cloudformation_dataclass
class EventRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [EventRoleAllowStatement0_1]


@cloudformation_dataclass
class EventRolePolicy:
    resource: iam.user.Policy
    policy_name = 'eb-pipeline-execution'
    policy_document = EventRolePolicies0PolicyDocument


@cloudformation_dataclass
class EventRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = EventRoleAssumeRolePolicyDocument
    path = '/'
    policies = [EventRolePolicy]
