"""MyLambdaVersion - AWS::Lambda::Version resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyLambdaVersion:
    """AWS::Lambda::Version resource."""

    resource: lambda_.Version
    function_name = ref(MyLambda)
    depends_on = ["MyLambda"]
