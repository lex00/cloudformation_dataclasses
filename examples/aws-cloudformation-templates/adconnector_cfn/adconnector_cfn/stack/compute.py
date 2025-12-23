"""Compute resources: ADConnectorLambdaFunction, DHCPOptions, DHCPOptionsVPCAssociation."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorLambdaFunctionEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'LOG_LEVEL': ref(LambdaLogLevel),
    }


@cloudformation_dataclass
class ADConnectorLambdaFunctionContent:
    resource: lambda_.layer_version.Content
    s3_bucket = ref(LambdaS3BucketName)
    s3_key = ref(LambdaZipFileName)


@cloudformation_dataclass
class ADConnectorLambdaFunctionCapacityProviderVpcConfig:
    resource: lambda_.capacity_provider.CapacityProviderVpcConfig
    subnet_ids = ['PrivateSubnet1ID', 'PrivateSubnet2ID']
    security_group_ids = [ref(ADConnectorDomainMembersSG)]


@cloudformation_dataclass
class ADConnectorLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    function_name = ref(LambdaFunctionName)
    handler = 'adconnector_custom_resource.lambda_handler'
    role = get_att(ADConnectorLambdaRole, "Arn")
    runtime = 'python3.8'
    memory_size = 128
    timeout = 120
    environment = ADConnectorLambdaFunctionEnvironment
    code = ADConnectorLambdaFunctionContent
    vpc_config = ADConnectorLambdaFunctionCapacityProviderVpcConfig


@cloudformation_dataclass
class DHCPOptions:
    """AWS::EC2::DHCPOptions resource."""

    resource: ec2.DHCPOptions
    domain_name = ref(DomainDNSName)
    domain_name_servers = [ref(DomainDNSServers)]
    tags = [{
        'Key': 'Name',
        'Value': ref(DomainDNSName),
    }]
    condition = 'DHCPOptionSetCondition'


@cloudformation_dataclass
class DHCPOptionsVPCAssociation:
    """AWS::EC2::VPCDHCPOptionsAssociation resource."""

    resource: ec2.VPCDHCPOptionsAssociation
    vpc_id = ref(VPCID)
    dhcp_options_id = ref(DHCPOptions)
    condition = 'DHCPOptionSetCondition'
