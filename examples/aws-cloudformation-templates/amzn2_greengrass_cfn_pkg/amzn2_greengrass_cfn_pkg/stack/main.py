"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'lambda.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class LambdaExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0]


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:*:*:*')


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement1:
    resource: PolicyStatement
    action = ['iot:*']
    resource_arn = '*'


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement2:
    resource: PolicyStatement
    action = ['greengrass:*']
    resource_arn = '*'


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement3:
    resource: PolicyStatement
    action = ['ec2:DescribeReservedInstancesOfferings']
    resource_arn = '*'


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement4:
    resource: PolicyStatement
    action = [
        'iam:CreateRole',
        'iam:AttachRolePolicy',
        'iam:GetRole',
        'iam:DeleteRole',
        'iam:PassRole',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:role/greengrass_cfn_${AWS::StackName}_ServiceRole')


@cloudformation_dataclass
class LambdaExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0_1, LambdaExecutionRoleAllowStatement1, LambdaExecutionRoleAllowStatement2, LambdaExecutionRoleAllowStatement3, LambdaExecutionRoleAllowStatement4]


@cloudformation_dataclass
class LambdaExecutionRolePolicy:
    resource: iam.user.Policy
    policy_document = LambdaExecutionRolePolicies0PolicyDocument
    policy_name = 'root'


@cloudformation_dataclass
class LambdaExecutionRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = LambdaExecutionRoleAssumeRolePolicyDocument
    policies = [LambdaExecutionRolePolicy]


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
    code = CreateThingFunctionCode
    description = 'Create thing, certificate, and policy, return cert and private key'
    handler = 'index.handler'
    role = get_att(LambdaExecutionRole, "Arn")
    runtime = 'python3.12'
    timeout = 60


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
    code = GGSampleFunctionCode
    description = 'Long running lambda that provides telemetry and pub/sub echo'
    function_name = Join('_', [
    ref(CoreName),
    'sample',
])
    handler = 'index.function_handler'
    role = get_att(LambdaExecutionRole, "Arn")
    runtime = 'python3.12'
    timeout = 60


@cloudformation_dataclass
class GGSampleFunctionVersion:
    """AWS::Lambda::Version resource."""

    resource: lambda_.Version
    function_name = get_att(GGSampleFunction, "Arn")


@cloudformation_dataclass
class FunctionDefinition:
    """AWS::Greengrass::FunctionDefinition resource."""

    resource: greengrass.FunctionDefinition
    initial_version = {
        'DefaultConfig': {
            'Execution': {
                LambdaLinuxProcessParams.isolation_mode: 'GreengrassContainer',
            },
        },
        'Functions': [{
            'FunctionArn': ref(GGSampleFunctionVersion),
            'FunctionConfiguration': {
                'EncodingType': 'binary',
                'Environment': {
                    'AccessSysfs': 'false',
                    'Execution': {
                        'IsolationMode': 'GreengrassContainer',
                        'RunAs': {
                            'Gid': '10',
                            'Uid': '1',
                        },
                    },
                    'Variables': {
                        'CORE_NAME': ref(CoreName),
                    },
                },
                'Executable': 'index.py',
                'MemorySize': '65536',
                'Pinned': 'true',
                'Timeout': '300',
            },
            'Id': Join('_', [
    ref(CoreName),
    'sample',
]),
        }],
    }
    name = 'FunctionDefinition'


@cloudformation_dataclass
class GreengrassCoreDefinition:
    """AWS::Greengrass::CoreDefinition resource."""

    resource: greengrass.CoreDefinition
    name = Join('_', [
    ref(CoreName),
    'Core',
])


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
class GreengrassCoreDefinitionVersion:
    """AWS::Greengrass::CoreDefinitionVersion resource."""

    resource: greengrass.CoreDefinitionVersion
    core_definition_id = ref(GreengrassCoreDefinition)
    cores = [{
        'CertificateArn': Join(':', [
    'arn:',
    AWS_PARTITION,
    ':iot',
    AWS_REGION,
    AWS_ACCOUNT_ID,
    Join('/', [
    'cert',
    get_att(IoTThing, "certificateId"),
]),
]),
        'Id': Join('_', [
    ref(CoreName),
    'Core',
]),
        'SyncShadow': 'false',
        'ThingArn': Join(':', [
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
]),
    }]


@cloudformation_dataclass
class SubscriptionDefinition:
    """AWS::Greengrass::SubscriptionDefinition resource."""

    resource: greengrass.SubscriptionDefinition
    initial_version = {
        'Subscriptions': [
            {
                'Id': 'Subscription1',
                'Source': 'cloud',
                'Subject': Join('/', [
    ref(CoreName),
    'in',
]),
                'Target': ref(GGSampleFunctionVersion),
            },
            {
                'Id': 'Subscription2',
                'Source': ref(GGSampleFunctionVersion),
                'Subject': Join('/', [
    ref(CoreName),
    'out',
]),
                'Target': 'cloud',
            },
            {
                'Id': 'Subscription3',
                'Source': ref(GGSampleFunctionVersion),
                'Subject': Join('/', [
    ref(CoreName),
    'telem',
]),
                'Target': 'cloud',
            },
        ],
    }
    name = 'SubscriptionDefinition'


@cloudformation_dataclass
class GreengrassResourceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'greengrass.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class GreengrassResourceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [GreengrassResourceRoleAllowStatement0]


@cloudformation_dataclass
class GreengrassResourceRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:*:*:*')


@cloudformation_dataclass
class GreengrassResourceRoleAllowStatement1:
    resource: PolicyStatement
    action = ['iot:*']
    resource_arn = '*'


@cloudformation_dataclass
class GreengrassResourceRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [GreengrassResourceRoleAllowStatement0_1, GreengrassResourceRoleAllowStatement1]


@cloudformation_dataclass
class GreengrassResourceRolePolicy:
    resource: iam.user.Policy
    policy_document = GreengrassResourceRolePolicies0PolicyDocument
    policy_name = 'root'


@cloudformation_dataclass
class GreengrassResourceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = GreengrassResourceRoleAssumeRolePolicyDocument
    policies = [GreengrassResourceRolePolicy]


@cloudformation_dataclass
class GreengrassGroup:
    """AWS::Greengrass::Group resource."""

    resource: greengrass.Group
    initial_version = {
        'CoreDefinitionVersionArn': ref(GreengrassCoreDefinitionVersion),
        'FunctionDefinitionVersionArn': get_att(FunctionDefinition, "LatestVersionArn"),
        'SubscriptionDefinitionVersionArn': get_att(SubscriptionDefinition, "LatestVersionArn"),
    }
    name = ref(CoreName)
    role_arn = get_att(GreengrassResourceRole, "Arn")


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = '172.31.0.0/24'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Allow inbound SSH access'
    security_group_ingress = [{
        'CidrIp': ref(SecurityAccessCIDR),
        'FromPort': 22,
        'IpProtocol': 'tcp',
        'ToPort': 22,
    }]
    vpc_id = ref(VPC)


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
    code = InstanceAZFunctionCode
    description = 'Queries account and region for supported AZ'
    handler = 'index.handler'
    role = get_att(LambdaExecutionRole, "Arn")
    runtime = 'python3.12'
    timeout = 60


@cloudformation_dataclass
class InstanceAZ:
    """Custom::InstanceAZ resource."""

    # Unknown resource type: Custom::InstanceAZ
    resource: CloudFormationResource
    region = AWS_REGION
    service_token = get_att(InstanceAZFunction, "Arn")


@cloudformation_dataclass
class SubnetAPublic:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = get_att(InstanceAZ, "AvailabilityZone")
    cidr_block = '172.31.0.0/24'
    map_public_ip_on_launch = True
    vpc_id = ref(VPC)


@cloudformation_dataclass
class GreengrassInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(LatestAmiId)
    instance_type = ref(InstanceType)
    key_name = ref(myKeyPair)
    security_group_ids = Split(',', get_att(InstanceSecurityGroup, "GroupId"))
    subnet_id = ref(SubnetAPublic)
    tags = [{
        'Key': 'Name',
        'Value': Join('-', [
    'Greengrass Core Blog ',
    ref(CoreName),
]),
    }]
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
class GroupDeploymentResetFunctionCode:
    resource: lambda_.function.Code
    zip_file = """"Group Deployment Reset Function"

# pylint: disable=line-too-long,logging-fstring-interpolation

import os
import sys
import json
import logging
import cfnresponse
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

session = boto3.session.Session()
region = os.env["AWS_REGION"]
partition = session.get_partition_for_region(region)
c = session.client("greengrass")
iam = session.client("iam")
role_name = f"greengrass_cfn_{os.environ['STACK_NAME']}_ServiceRole"


def find_group(thingName):
    "Find the group based on the name"

    response_auth = ""

    response = c.list_groups()
    for group in response["Groups"]:
        thingfound = False
        group_version = c.get_group_version(
            GroupId=group["Id"], GroupVersionId=group["LatestVersion"]
        )

        core_arn = group_version["Definition"].get("CoreDefinitionVersionArn", "")
        if core_arn:
            core_id = core_arn[
                core_arn.index("/cores/") + 7 : core_arn.index("/versions/")
            ]
            core_version_id = core_arn[
                core_arn.index("/versions/") + 10 : len(core_arn)
            ]
            thingfound = False
            response_core_version = c.get_core_definition_version(
                CoreDefinitionId=core_id, CoreDefinitionVersionId=core_version_id
            )
            if "Cores" in response_core_version["Definition"]:
                for thing_arn in response_core_version["Definition"]["Cores"]:
                    if thingName == thing_arn["ThingArn"].split("/")[1]:
                        thingfound = True
                        break
        if thingfound:
            logger.info(f"found thing: {thingName}, group id is: {group['Id']}")
            response_auth = group["Id"]
            return response_auth

    return ""


def manage_greengrass_role(cmd):
    "Greengrass role"

    if cmd == "CREATE":
        r = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument='{"Version": "2012-10-17","Statement": [{"Effect": "Allow","Principal": {"Service": "greengrass.amazonaws.com"},"Action": "sts:AssumeRole"}]}',
            Description="Role for CloudFormation blog post",
        )
        role_arn = r["Role"]["Arn"]
        iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn=f"arn:{partition}:iam::policy/service-role/AWSGreengrassResourceAccessRolePolicy",
        )
        c.associate_service_role_to_account(RoleArn=role_arn)
        logger.info(f"Created and associated role {role_name}")
    else:
        try:
            r = iam.get_role(RoleName=role_name)
            role_arn = r["Role"]["Arn"]
            c.disassociate_service_role_from_account()
            iam.delete_role(RoleName=role_name)
            logger.info(f"Disassociated and deleted role {role_name}")
        except ClientError:
            return


def handler(event, context):
    "Lambda handler"

    responseData = {}
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        result = cfnresponse.FAILED
        thingName = event["ResourceProperties"]["ThingName"]
        if event["RequestType"] == "Create":
            try:
                c.get_service_role_for_account()
                result = cfnresponse.SUCCESS
            except ClientError:
                manage_greengrass_role("CREATE")
                logger.info("Greengrass service role created")
                result = cfnresponse.SUCCESS
        elif event["RequestType"] == "Delete":
            group_id = find_group(thingName)
            logger.info(f"Group id to delete: {group_id}")
            if group_id:
                c.reset_deployments(Force=True, GroupId=group_id)
                result = cfnresponse.SUCCESS
                logger.info("Forced reset of Greengrass deployment")
                manage_greengrass_role("DELETE")
            else:
                logger.error(f"No group Id for thing: {thingName} found")
    except ClientError as e:
        logger.error(f"Error: {e}")
        result = cfnresponse.FAILED
    logger.info(f"Returning response of: {result}, with result of: {responseData}")
    sys.stdout.flush()
    cfnresponse.send(event, context, result, responseData)"""


@cloudformation_dataclass
class GroupDeploymentResetFunctionEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'STACK_NAME': AWS_STACK_NAME,
    }


@cloudformation_dataclass
class GroupDeploymentResetFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    code = GroupDeploymentResetFunctionCode
    description = 'Resets any deployments during stack delete and manages Greengrass service role needs'
    environment = GroupDeploymentResetFunctionEnvironment
    handler = 'index.handler'
    role = get_att(LambdaExecutionRole, "Arn")
    runtime = 'python3.12'
    timeout = 60


@cloudformation_dataclass
class GroupDeploymentReset:
    """Custom::GroupDeploymentReset resource."""

    # Unknown resource type: Custom::GroupDeploymentReset
    resource: CloudFormationResource
    region = AWS_REGION
    service_token = get_att(GroupDeploymentResetFunction, "Arn")
    thing_name = Join('_', [
    ref(CoreName),
    'Core',
])
    depends_on = ["GreengrassGroup"]


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway


@cloudformation_dataclass
class RouteTablePublic:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class RouteTableAssociationAPublic:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(RouteTablePublic)
    subnet_id = ref(SubnetAPublic)


@cloudformation_dataclass
class RouteTablePublicInternetRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    route_table_id = ref(RouteTablePublic)
    depends_on = ["VPCGatewayAttachment"]


@cloudformation_dataclass
class VPCGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = ref(InternetGateway)
    vpc_id = ref(VPC)
