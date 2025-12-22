from __future__ import annotations

"""TestResourcePermission - AWS::Lambda::Permission resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourcePermission:
    """AWS::Lambda::Permission resource."""

    resource: Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(TestResourceHandler, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*')
