from __future__ import annotations

"""TestResourceRootPermission - AWS::Lambda::Permission resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceRootPermission:
    """AWS::Lambda::Permission resource."""

    resource: Permission
    action = 'lambda:InvokeFunction'
    function_name: GetAtt[TestResourceHandler] = get_att("Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/')
