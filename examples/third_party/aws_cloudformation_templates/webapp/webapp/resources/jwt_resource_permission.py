from __future__ import annotations

"""JwtResourcePermission - AWS::Lambda::Permission resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class JwtResourcePermission:
    """AWS::Lambda::Permission resource."""

    resource: Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(JwtResourceHandler, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*')
