from __future__ import annotations

"""JwtResourceRootPermission - AWS::Lambda::Permission resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class JwtResourceRootPermission:
    """AWS::Lambda::Permission resource."""

    resource: Permission
    action = 'lambda:InvokeFunction'
    function_name: GetAtt[JwtResourceHandler] = get_att("Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/')
