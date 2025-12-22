"""MyLambdaPermission - AWS::Lambda::Permission resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyLambdaPermission:
    """AWS::Lambda::Permission resource."""

    resource: Permission
    action = 'lambda:InvokeFunction'
    function_name = ref(MyLambda)
    principal = 'iot.amazonaws.com'
    source_account = Sub('${AWS::AccountId}')
    source_arn = get_att(IoTTopicRule, "Arn")
