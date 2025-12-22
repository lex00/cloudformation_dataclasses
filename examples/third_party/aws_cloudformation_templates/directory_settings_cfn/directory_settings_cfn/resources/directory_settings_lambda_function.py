"""DirectorySettingsLambdaFunction - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionEnvironment:
    resource: lambda_.Environment
    variables = {
        'LOG_LEVEL': ref(LambdaLogLevel),
    }


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionCode:
    resource: lambda_.Code
    s3_bucket = ref(LambdaS3BucketName)
    s3_key = ref(LambdaZipFileName)


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionVpcConfig:
    resource: lambda_.VpcConfig
    subnet_ids = ref(Subnets)
    security_group_ids = ref(SecurityGroups)


@cloudformation_dataclass
class DirectorySettingsLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    function_name = ref(LambdaFunctionName)
    handler = 'directory_settings_custom_resource.lambda_handler'
    role = get_att(DirectorySettingsLambdaRole, "Arn")
    runtime = 'python3.12'
    memory_size = 128
    timeout = 120
    environment = DirectorySettingsLambdaFunctionEnvironment
    code = DirectorySettingsLambdaFunctionCode
    vpc_config = DirectorySettingsLambdaFunctionVpcConfig
