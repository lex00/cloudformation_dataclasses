from __future__ import annotations

"""ADConnectorLambdaFunction - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorLambdaFunctionEnvironment:
    resource: Environment
    variables = {
        'LOG_LEVEL': ref(LambdaLogLevel),
    }


@cloudformation_dataclass
class ADConnectorLambdaFunctionCode:
    resource: Code
    s3_bucket = ref(LambdaS3BucketName)
    s3_key = ref(LambdaZipFileName)


@cloudformation_dataclass
class ADConnectorLambdaFunctionVpcConfig:
    resource: VpcConfig
    subnet_ids = ['PrivateSubnet1ID', 'PrivateSubnet2ID']
    security_group_ids = [ref(ADConnectorDomainMembersSG)]


@cloudformation_dataclass
class ADConnectorLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: Function
    function_name = ref(LambdaFunctionName)
    handler = 'adconnector_custom_resource.lambda_handler'
    role = get_att(ADConnectorLambdaRole, "Arn")
    runtime = 'python3.8'
    memory_size = 128
    timeout = 120
    environment = ADConnectorLambdaFunctionEnvironment
    code = ADConnectorLambdaFunctionCode
    vpc_config = ADConnectorLambdaFunctionVpcConfig
