"""NeptuneRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': [
            'monitoring.rds.amazonaws.com',
            'rds.amazonaws.com',
        ],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class NeptuneRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneRoleAllowStatement0]


@cloudformation_dataclass
class NeptuneRole:
    """AWS::IAM::Role resource."""

    resource: Role
    role_name = Sub('${Env}-${AppName}-neptune-iam-role-${AWS::Region}')
    assume_role_policy_document = NeptuneRoleAssumeRolePolicyDocument
    managed_policy_arns = [ref(NeptuneCloudWatchPolicy), ref(NeptuneS3Policy)]
    condition = 'EnableAuditLogUpload'
