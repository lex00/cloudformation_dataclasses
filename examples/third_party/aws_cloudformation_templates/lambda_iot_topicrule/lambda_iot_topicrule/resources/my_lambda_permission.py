from __future__ import annotations

"""MyLambdaPermission - AWS::Lambda::Permission resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyLambdaPermission:
    """AWS::Lambda::Permission resource."""

    resource: Permission
    action = 'lambda:InvokeFunction'
    function_name: Ref[MyLambda] = ref()
    principal = 'iot.amazonaws.com'
    source_account = Sub('${AWS::AccountId}')
    source_arn: GetAtt[IoTTopicRule] = get_att("Arn")
