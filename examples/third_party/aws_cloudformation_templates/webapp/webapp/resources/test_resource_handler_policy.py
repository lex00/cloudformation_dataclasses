from __future__ import annotations

"""TestResourceHandlerPolicy - AWS::IAM::RolePolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceHandlerPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        'dynamodb:BatchGetItem',
        'dynamodb:GetItem',
        'dynamodb:Query',
        'dynamodb:Scan',
        'dynamodb:BatchWriteItem',
        'dynamodb:PutItem',
        'dynamodb:UpdateItem',
    ]
    resource_arn = [get_att("TestTable", "Arn")]


@cloudformation_dataclass
class TestResourceHandlerPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [TestResourceHandlerPolicyAllowStatement0]


@cloudformation_dataclass
class TestResourceHandlerPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: RolePolicy
    policy_document = TestResourceHandlerPolicyPolicyDocument
    policy_name = 'handler-policy'
    role_name: Ref[TestResourceHandlerRole] = ref()
