"""Compute resources: DirectorySettingsLambdaFunction."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.lambda_ import Runtime


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'LOG_LEVEL': ref(LambdaLogLevel),
    }


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionContent:
    resource: lambda_.layer_version.Content
    s3_bucket = ref(LambdaS3BucketName)
    s3_key = ref(LambdaZipFileName)


@cloudformation_dataclass
class DirectorySettingsLambdaFunctionCapacityProviderVpcConfig:
    resource: lambda_.capacity_provider.CapacityProviderVpcConfig
    subnet_ids = ref(Subnets)
    security_group_ids = ref(SecurityGroups)


@cloudformation_dataclass
class DirectorySettingsLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    function_name = ref(LambdaFunctionName)
    handler = 'directory_settings_custom_resource.lambda_handler'
    role = get_att(DirectorySettingsLambdaRole, "Arn")
    runtime = Runtime.PYTHON3_12
    memory_size = 128
    timeout = 120
    environment = DirectorySettingsLambdaFunctionEnvironment
    code = DirectorySettingsLambdaFunctionContent
    vpc_config = DirectorySettingsLambdaFunctionCapacityProviderVpcConfig
