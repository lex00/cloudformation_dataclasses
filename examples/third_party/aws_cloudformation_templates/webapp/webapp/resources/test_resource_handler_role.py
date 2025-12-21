from __future__ import annotations

"""TestResourceHandlerRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceHandlerRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class TestResourceHandlerRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [TestResourceHandlerRoleAllowStatement0]


@cloudformation_dataclass
class TestResourceHandlerRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = TestResourceHandlerRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']
