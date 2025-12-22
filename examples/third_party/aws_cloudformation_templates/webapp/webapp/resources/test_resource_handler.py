from __future__ import annotations

"""TestResourceHandler - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceHandlerCode:
    resource: Code
    s3_bucket = ref(LambdaCodeS3Bucket)
    s3_key = ref(LambdaCodeS3Key)


@cloudformation_dataclass
class TestResourceHandlerEnvironment:
    resource: Environment
    variables = {
        'TABLE_NAME': ref(TestTable),
    }


@cloudformation_dataclass
class TestResourceHandler:
    """AWS::Lambda::Function resource."""

    resource: Function
    handler = 'bootstrap'
    function_name = Sub('${AppName}-test-handler')
    runtime = 'provided.al2023'
    code = TestResourceHandlerCode
    role = get_att(TestResourceHandlerRole, "Arn")
    environment = TestResourceHandlerEnvironment
