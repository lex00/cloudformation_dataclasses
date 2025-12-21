from __future__ import annotations

"""DirectorySettingsLambdaFunction - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionEnvironment:
    resource: Environment
    variables = {
        'LOG_LEVEL': ref(LambdaLogLevel),
    }


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionCode:
    resource: Code
    s3_bucket = ref(LambdaS3BucketName)
    s3_key = ref(LambdaZipFileName)


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionVpcConfig:
    resource: VpcConfig
    subnet_ids = ref(Subnets)
    security_group_ids = ref(SecurityGroups)


@cloudformation_dataclass
class DirectorySettingsLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: Function
    function_name = ref(LambdaFunctionName)
    handler = 'directory_settings_custom_resource.lambda_handler'
    role: GetAtt[DirectorySettingsLambdaRole] = get_att("Arn")
    runtime = 'python3.12'
    memory_size = 128
    timeout = 120
    environment = DirectorySettingsLambdaFunctionEnvironment
    code = DirectorySettingsLambdaFunctionCode
    vpc_config = DirectorySettingsLambdaFunctionVpcConfig
