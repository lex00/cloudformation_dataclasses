"""Stack resources."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.lambda_ import Runtime
from cloudformation_dataclasses.core.constants import IpProtocol


@cloudformation_dataclass
class GreengrassCoreDefinition:
    """AWS::Greengrass::CoreDefinition resource."""

    resource: greengrass.CoreDefinition
    name = Join('_', [
    ref(CoreName),
    'Core',
])


@cloudformation_dataclass
class CreateThingFunctionCode:
    resource: lambda_.function.Code
    zip_file = """import sys
import cfnresponse
import boto3
from botocore.exceptions import ClientError
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

policyDocument = {
    'Version': '2012-10-17',
    'Statement': [
        {
            'Effect': 'Allow',
            'Action': 'iot:*',
            'Resource': '*'
        },
        {
            'Effect': 'Allow',
            'Action': 'greengrass:*',
            'Resource': '*'
        }
    ]
}


def handler(event, context):
    responseData = {}
    try:
        logger.info('Received event: {}'.format(json.dumps(event)))
        result = cfnresponse.FAILED
        client = boto3.client('iot')
        thingName=event['ResourceProperties']['ThingName']
        if event['RequestType'] == 'Create':
            thing = client.create_thing(
                thingName=thingName
            )
            response = client.create_keys_and_certificate(
                setAsActive=True
            )
            certId = response['certificateId']
            certArn = response['certificateArn']
            certPem = response['certificatePem']
            privateKey = response['keyPair']['PrivateKey']
            client.create_policy(
                policyName='{}-full-access'.format(thingName),
                policyDocument=json.dumps(policyDocument)
            )
            response = client.attach_policy(
                policyName='{}-full-access'.format(thingName),
                target=certArn
            )
            response = client.attach_thing_principal(
                thingName=thingName,
                principal=certArn,
            )
            logger.info('Created thing: %s, cert: %s and policy: %s' % 
                (thingName, certId, '{}-full-access'.format(thingName)))
            result = cfnresponse.SUCCESS
            responseData['certificateId'] = certId
            responseData['certificatePem'] = certPem
            responseData['privateKey'] = privateKey
            responseData['iotEndpoint'] = client.describe_endpoint(endpointType='iot:Data-ATS')['endpointAddress']
        elif event['RequestType'] == 'Update':
            logger.info('Updating thing: %s' % thingName)
            result = cfnresponse.SUCCESS
        elif event['RequestType'] == 'Delete':
            logger.info('Deleting thing: %s and cert/policy' % thingName)
            response = client.list_thing_principals(
                thingName=thingName
            )
            for i in response['principals']:
                response = client.detach_thing_principal(
                    thingName=thingName,
                    principal=i
                )
                response = client.detach_policy(
                    policyName='{}-full-access'.format(thingName),
                    target=i
                )
                response = client.update_certificate(
                    certificateId=i.split('/')[-1],
                    newStatus='INACTIVE'
                )
                response = client.delete_certificate(
                    certificateId=i.split('/')[-1],
                    forceDelete=True
                )
                response = client.delete_policy(
                    policyName='{}-full-access'.format(thingName),
                )
                response = client.delete_thing(
                    thingName=thingName
                )
            result = cfnresponse.SUCCESS
    except ClientError as e:
        logger.error('Error: {}'.format(e))
        result = cfnresponse.FAILED
    logger.info('Returning response of: {}, with result of: {}'.format(result, responseData))
    sys.stdout.flush()
    cfnresponse.send(event, context, result, responseData)
"""


@cloudformation_dataclass
class CreateThingFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    description = 'Create thing, certificate, and policy, return cert and private key'
    handler = 'index.handler'
    runtime = Runtime.PYTHON3_12
    role = get_att(LambdaExecutionRole, "Arn")
    timeout = 60
    code = CreateThingFunctionCode


@cloudformation_dataclass
class IoTThing:
    """Custom::IoTThing resource."""

    # Unknown resource type: Custom::IoTThing
    resource: CloudFormationResource
    service_token = get_att(CreateThingFunction, "Arn")
    thing_name = Join('_', [
    ref(CoreName),
    'Core',
])


@cloudformation_dataclass
class GreengrassCoreDefinitionVersionDevice:
    resource: greengrass.device_definition.Device
    id = Join('_', [
    ref(CoreName),
    'Core',
])
    thing_arn = Join(':', [
    'arn:',
    AWS_PARTITION,
    ':iot',
    AWS_REGION,
    AWS_ACCOUNT_ID,
    Join('/', [
    'thing',
    Join('_', [
    ref(CoreName),
    'Core',
]),
]),
])
    certificate_arn = Join(':', [
    'arn:',
    AWS_PARTITION,
    ':iot',
    AWS_REGION,
    AWS_ACCOUNT_ID,
    Join('/', [
    'cert',
    get_att(IoTThing, "certificateId"),
]),
])
    sync_shadow = 'false'


@cloudformation_dataclass
class GreengrassCoreDefinitionVersion:
    """AWS::Greengrass::CoreDefinitionVersion resource."""

    resource: greengrass.CoreDefinitionVersion
    core_definition_id = ref(GreengrassCoreDefinition)
    cores = [GreengrassCoreDefinitionVersionDevice]


@cloudformation_dataclass
class GGSampleFunctionCode:
    resource: lambda_.function.Code
    zip_file = """import os
from threading import Timer
import greengrasssdk


counter = 0
client = greengrasssdk.client('iot-data')


def telemetry():
    '''Publish incrementing value to telemetry topic every 2 seconds'''
    global counter
    counter += 1
    client.publish(
        topic='{}/telem'.format(os.environ['CORE_NAME']),
        payload='Example telemetry counter, value: {}'.format(counter)
    )
    Timer(5, telemetry).start()
# Call telemetry() to start telemetry publish
telemetry()


def function_handler(event, context):
    '''Echo message on /in topic to /out topic'''
    client.publish(
        topic='{}/out'.format(os.environ['CORE_NAME']),
        payload=event
    )
"""


@cloudformation_dataclass
class GGSampleFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    function_name = Join('_', [
    ref(CoreName),
    'sample',
])
    description = 'Long running lambda that provides telemetry and pub/sub echo'
    handler = 'index.function_handler'
    runtime = Runtime.PYTHON3_12
    role = get_att(LambdaExecutionRole, "Arn")
    timeout = 60
    code = GGSampleFunctionCode


@cloudformation_dataclass
class GGSampleFunctionVersion:
    """AWS::Lambda::Version resource."""

    resource: lambda_.Version
    function_name = get_att(GGSampleFunction, "Arn")


@cloudformation_dataclass
class FunctionDefinitionExecution:
    resource: greengrass.function_definition.Execution
    isolation_mode = 'GreengrassContainer'


@cloudformation_dataclass
class FunctionDefinitionDefaultConfig:
    resource: greengrass.function_definition.DefaultConfig
    execution = FunctionDefinitionExecution


@cloudformation_dataclass
class FunctionDefinitionRunAs:
    resource: greengrass.function_definition.RunAs
    uid = '1'
    gid = '10'


@cloudformation_dataclass
class FunctionDefinitionExecution1:
    resource: greengrass.function_definition.Execution
    isolation_mode = 'GreengrassContainer'
    run_as = FunctionDefinitionRunAs


@cloudformation_dataclass
class FunctionDefinitionEnvironment:
    resource: greengrass.function_definition.Environment
    variables = {
        'CORE_NAME': ref(CoreName),
    }
    access_sysfs = 'false'
    execution = FunctionDefinitionExecution1


@cloudformation_dataclass
class FunctionDefinitionFunctionConfiguration:
    resource: greengrass.function_definition.FunctionConfiguration
    pinned = 'true'
    executable = 'index.py'
    memory_size = '65536'
    timeout = '300'
    encoding_type = 'binary'
    environment = FunctionDefinitionEnvironment


@cloudformation_dataclass
class FunctionDefinitionFunction:
    resource: greengrass.function_definition.Function
    id = Join('_', [
    ref(CoreName),
    'sample',
])
    function_arn = ref(GGSampleFunctionVersion)
    function_configuration = FunctionDefinitionFunctionConfiguration


@cloudformation_dataclass
class FunctionDefinitionFunctionDefinitionVersion:
    resource: greengrass.function_definition.FunctionDefinitionVersion
    default_config = FunctionDefinitionDefaultConfig
    functions = [FunctionDefinitionFunction]


@cloudformation_dataclass
class FunctionDefinition:
    """AWS::Greengrass::FunctionDefinition resource."""

    resource: greengrass.FunctionDefinition
    name = 'FunctionDefinition'
    initial_version = FunctionDefinitionFunctionDefinitionVersion


@cloudformation_dataclass
class SubscriptionDefinitionSubscription:
    resource: greengrass.subscription_definition.Subscription
    id = 'Subscription1'
    source = 'cloud'
    subject = Join('/', [
    ref(CoreName),
    'in',
])
    target = ref(GGSampleFunctionVersion)


@cloudformation_dataclass
class SubscriptionDefinitionSubscription1:
    resource: greengrass.subscription_definition.Subscription
    id = 'Subscription2'
    source = ref(GGSampleFunctionVersion)
    subject = Join('/', [
    ref(CoreName),
    'out',
])
    target = 'cloud'


@cloudformation_dataclass
class SubscriptionDefinitionSubscription2:
    resource: greengrass.subscription_definition.Subscription
    id = 'Subscription3'
    source = ref(GGSampleFunctionVersion)
    subject = Join('/', [
    ref(CoreName),
    'telem',
])
    target = 'cloud'


@cloudformation_dataclass
class SubscriptionDefinitionSubscriptionDefinitionVersion:
    resource: greengrass.subscription_definition.SubscriptionDefinitionVersion
    subscriptions = [SubscriptionDefinitionSubscription, SubscriptionDefinitionSubscription1, SubscriptionDefinitionSubscription2]


@cloudformation_dataclass
class SubscriptionDefinition:
    """AWS::Greengrass::SubscriptionDefinition resource."""

    resource: greengrass.SubscriptionDefinition
    name = 'SubscriptionDefinition'
    initial_version = SubscriptionDefinitionSubscriptionDefinitionVersion


@cloudformation_dataclass
class GreengrassGroupGroupVersion:
    resource: greengrass.group.GroupVersion
    core_definition_version_arn = ref(GreengrassCoreDefinitionVersion)
    function_definition_version_arn = get_att(FunctionDefinition, "LatestVersionArn")
    subscription_definition_version_arn = get_att(SubscriptionDefinition, "LatestVersionArn")


@cloudformation_dataclass
class GreengrassGroup:
    """AWS::Greengrass::Group resource."""

    resource: greengrass.Group
    name = ref(CoreName)
    role_arn = get_att(GreengrassResourceRole, "Arn")
    initial_version = GreengrassGroupGroupVersion


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = '172.31.0.0/24'
    enable_dns_support = True
    enable_dns_hostnames = True
    instance_tenancy = 'default'


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway


@cloudformation_dataclass
class VPCGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    vpc_id = ref(VPC)
    internet_gateway_id = ref(InternetGateway)


@cloudformation_dataclass
class InstanceAZFunctionCode:
    resource: lambda_.function.Code
    zip_file = """import sys
import cfnresponse
import boto3
from botocore.exceptions import ClientError
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

c = boto3.client('ec2')


def handler(event, context):
    responseData = {}
    try:
        logger.info('Received event: {}'.format(json.dumps(event)))
        result = cfnresponse.FAILED
        if event['RequestType'] == 'Create':
            r = c.describe_reserved_instances_offerings(
                Filters=[
                    {
                        'Name': 'scope',
                        'Values': [
                            'Availability Zone',
                        ]
                    },
                ],
                IncludeMarketplace=False,
                InstanceType='t3.micro',
            )
            x = r['ReservedInstancesOfferings']
            while 'NextToken' in r:
                r = c.describe_reserved_instances_offerings(
                    Filters=[
                        {
                            'Name': 'scope',
                            'Values': [
                                'Availability Zone',
                            ]
                        },
                    ],
                    IncludeMarketplace=False,
                    InstanceType='t3.micro',
                    NextToken=r['NextToken']
                )
                x.extend(r['ReservedInstancesOfferings'])
            responseData['AvailabilityZone'] = set(d['AvailabilityZone'] for d in x).pop()
            result = cfnresponse.SUCCESS
        else:
            result = cfnresponse.SUCCESS
    except ClientError as e:
        logger.error('Error: {}'.format(e))
        result = cfnresponse.FAILED
    logger.info('Returning response of: %s, with result of: %s' % (result, responseData))
    sys.stdout.flush()
    cfnresponse.send(event, context, result, responseData)
"""


@cloudformation_dataclass
class InstanceAZFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    description = 'Queries account and region for supported AZ'
    handler = 'index.handler'
    runtime = Runtime.PYTHON3_12
    role = get_att(LambdaExecutionRole, "Arn")
    timeout = 60
    code = InstanceAZFunctionCode


@cloudformation_dataclass
class InstanceAZ:
    """Custom::InstanceAZ resource."""

    # Unknown resource type: Custom::InstanceAZ
    resource: CloudFormationResource
    service_token = get_att(InstanceAZFunction, "Arn")
    region = AWS_REGION


@cloudformation_dataclass
class SubnetAPublic:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = get_att(InstanceAZ, "AvailabilityZone")
    cidr_block = '172.31.0.0/24'
    map_public_ip_on_launch = True
    vpc_id = ref(VPC)


@cloudformation_dataclass
class RouteTablePublic:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class RouteTableAssociationAPublic:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(SubnetAPublic)
    route_table_id = ref(RouteTablePublic)


@cloudformation_dataclass
class RouteTablePublicInternetRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(RouteTablePublic)
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    depends_on = ["VPCGatewayAttachment"]


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = IpProtocol.TCP
    from_port = 22
    to_port = 22
    cidr_ip = ref(SecurityAccessCIDR)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Allow inbound SSH access'
    vpc_id = ref(VPC)
    security_group_ingress = [InstanceSecurityGroupEgress]


@cloudformation_dataclass
class GreengrassInstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('-', [
    'Greengrass Core Blog ',
    ref(CoreName),
])


@cloudformation_dataclass
class GreengrassInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(LatestAmiId)
    instance_type = ref(InstanceType)
    key_name = ref(myKeyPair)
    security_group_ids = Split(',', get_att(InstanceSecurityGroup, "GroupId"))
    tags = [GreengrassInstanceAssociationParameter]
    subnet_id = ref(SubnetAPublic)
    user_data = Base64(Sub("""#!/bin/bash
yum -y install python3-pip
pip3 install greengrasssdk
adduser --system ggc_user
groupadd --system ggc_group

# https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html#gg-core-download-tab
curl -O https://d1onfpft10uf5o.cloudfront.net/greengrass-core/downloads/1.9.1/greengrass-linux-x86-64-1.9.1.tar.gz
tar xf greengrass-linux-x86*.gz -C /
echo -n "${IoTThing.certificatePem}" > /greengrass/certs/${IoTThing.certificateId}.pem
echo -n "${IoTThing.privateKey}" > /greengrass/certs/${IoTThing.certificateId}.key
cd /greengrass/config
# Create Greengrass config file from inputs and parameters
# Can be enhanced to manage complete installation of Greengrass and credentials
cat <<EOT > config.json          
{
  "coreThing" : {
    "caPath" : "root.ca.pem",
    "certPath" : "${IoTThing.certificateId}.pem",
    "keyPath" : "${IoTThing.certificateId}.key",
    "thingArn" : "arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:thing/${CoreName}_Core",
    "iotHost" : "${IoTThing.iotEndpoint}",
    "ggHost" : "greengrass-ats.iot.${AWS::Region}.amazonaws.com"
  },
  "runtime" : {
    "cgroup" : {
      "useSystemd" : "yes"
    }
  },
  "managedRespawn" : false,
  "crypto" : {
    "principals" : {
      "SecretsManager" : {
        "privateKeyPath" : "file:///greengrass/certs/${IoTThing.certificateId}.key"
      },
      "IoTCertificate" : {
        "privateKeyPath" : "file:///greengrass/certs/${IoTThing.certificateId}.key",
        "certificatePath" : "file:///greengrass/certs/${IoTThing.certificateId}.pem"
      }
    },
    "caPath" : "file:///greengrass/certs/root.ca.pem"
  }
}
EOT

cd /greengrass/certs/
curl -o root.ca.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem
cd /tmp
# Create Greengrass systemd file - thanks to: https://gist.github.com/matthewberryman/fa21ca796c3a2e0dfe8224934b7b055c
cat <<EOT > greengrass.service
[Unit]
Description=greengrass daemon
After=network.target

[Service]
ExecStart=/greengrass/ggc/core/greengrassd start
Type=simple
RestartSec=2
Restart=always
User=root
PIDFile=/var/run/greengrassd.pid

[Install]
WantedBy=multi-user.target
EOT
cp greengrass.service /etc/systemd/system
systemctl enable greengrass.service
reboot
"""))
    depends_on = ["GreengrassGroup"]


@cloudformation_dataclass
class GroupDeploymentResetFunctionEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'STACK_NAME': AWS_STACK_NAME,
    }


@cloudformation_dataclass
class GroupDeploymentResetFunctionCode:
    resource: lambda_.function.Code
    zip_file = {
        'Rain::Embed': 'reset_function.py',
    }


@cloudformation_dataclass
class GroupDeploymentResetFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    description = 'Resets any deployments during stack delete and manages Greengrass service role needs'
    handler = 'index.handler'
    runtime = Runtime.PYTHON3_12
    role = get_att(LambdaExecutionRole, "Arn")
    timeout = 60
    environment = GroupDeploymentResetFunctionEnvironment
    code = GroupDeploymentResetFunctionCode


@cloudformation_dataclass
class GroupDeploymentReset:
    """Custom::GroupDeploymentReset resource."""

    # Unknown resource type: Custom::GroupDeploymentReset
    resource: CloudFormationResource
    service_token = get_att(GroupDeploymentResetFunction, "Arn")
    region = AWS_REGION
    thing_name = Join('_', [
    ref(CoreName),
    'Core',
])
    depends_on = ["GreengrassGroup"]
