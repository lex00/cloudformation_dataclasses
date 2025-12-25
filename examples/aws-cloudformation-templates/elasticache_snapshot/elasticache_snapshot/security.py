"""Security resources: IamRoleLambda."""

from . import *  # noqa: F403


@cloudformation_dataclass
class IamRoleLambdaAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class IamRoleLambdaAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [IamRoleLambdaAllowStatement0]


@cloudformation_dataclass
class IamRoleLambdaAllowStatement0_1:
    resource: PolicyStatement
    action = ['elasticache:ModifyReplicationGroup']
    resource_arn = ref(RedisReplicationGroup)


@cloudformation_dataclass
class IamRoleLambdaPolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [IamRoleLambdaAllowStatement0_1]


@cloudformation_dataclass
class IamRoleLambdaPolicy:
    resource: iam.user.Policy
    policy_name = 'ElastiCacheSnapshotPolicy'
    policy_document = IamRoleLambdaPolicies0PolicyDocument


@cloudformation_dataclass
class IamRoleLambda:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = IamRoleLambdaAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']
    policies = [IamRoleLambdaPolicy]
    condition = 'EnableBackups'
