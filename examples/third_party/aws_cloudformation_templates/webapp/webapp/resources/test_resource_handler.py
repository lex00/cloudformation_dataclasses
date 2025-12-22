"""TestResourceHandler - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceHandlerContent:
    resource: lambda_.layer_version.Content
    s3_bucket = ref(LambdaCodeS3Bucket)
    s3_key = ref(LambdaCodeS3Key)


@cloudformation_dataclass
class TestResourceHandlerEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'TABLE_NAME': ref(TestTable),
    }


@cloudformation_dataclass
class TestResourceHandler:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    handler = 'bootstrap'
    function_name = Sub('${AppName}-test-handler')
    runtime = 'provided.al2023'
    code = TestResourceHandlerContent
    role = get_att(TestResourceHandlerRole, "Arn")
    environment = TestResourceHandlerEnvironment
