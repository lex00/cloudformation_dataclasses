"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaLogsLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    log_group_name = Sub('/aws/lambda/${LambdaFunctionName}')
    retention_in_days = ref(LambdaLogsLogGroupRetention)
    kms_key_id = If("LambdaLogsCloudWatchKMSKeyCondition", ref(LambdaLogsCloudWatchKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [TagVpcPeeringConnectionsLambdaRoleAllowStatement0]


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    sid = 'CreateLogGroup'
    action = 'logs:CreateLogGroup'
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${TagVpcPeeringConnectionsLambdaLogsLogGroup}')


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRoleAllowStatement1:
    resource: PolicyStatement
    sid = 'CreateLogStreamAndEvents'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${TagVpcPeeringConnectionsLambdaLogsLogGroup}:log-stream:*')


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [TagVpcPeeringConnectionsLambdaRoleAllowStatement0_1, TagVpcPeeringConnectionsLambdaRoleAllowStatement1]


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRolePolicy:
    resource: iam.user.Policy
    policy_name = 'CloudWatchLogGroup'
    policy_document = TagVpcPeeringConnectionsLambdaRolePolicies0PolicyDocument


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRoleAllowStatement0_2:
    resource: PolicyStatement
    sid = 'Tagging'
    action = [
        'ec2:CreateTags',
        'ec2:DeleteTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:ec2:${AWS::Region}:${AWS::AccountId}:vpc-peering-connection/*')


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRolePolicies1PolicyDocument:
    resource: PolicyDocument
    statement = [TagVpcPeeringConnectionsLambdaRoleAllowStatement0_2]


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRolePolicy1:
    resource: iam.user.Policy
    policy_name = 'TagVpcPeeringConnections'
    policy_document = TagVpcPeeringConnectionsLambdaRolePolicies1PolicyDocument


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${LambdaFunctionName}-LambdaRole')
    description = 'Rights to Tag VPC Peering Connection'
    assume_role_policy_document = TagVpcPeeringConnectionsLambdaRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [TagVpcPeeringConnectionsLambdaRolePolicy, TagVpcPeeringConnectionsLambdaRolePolicy1]


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaFunctionEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'LOG_LEVEL': ref(LambdaLogLevel),
    }


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaFunctionCode:
    resource: lambda_.function.Code
    zip_file = """import cfnresponse, json, os, logging, boto3

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

try:
  logging.getLogger("boto3").setLevel(logging.CRITICAL)

  # Process Environment Variables
  LOGGER.setLevel(os.environ.get("LOG_LEVEL", logging.ERROR))

  ec2_client = boto3.client("ec2")
except Exception as error:
  LOGGER.error(error)
  cfnresponse.send(event, context, cfnresponse.FAILED, {})
  raise


def apply_name_tag(resource, name):
  return ec2_client.create_tags(Resources=[resource], Tags=[{"Key": "Name", "Value": name}])


def delete_name_tag(resource):
  return ec2_client.delete_tags(Resources=[resource], Tags=[{"Key": "Name"}])


def handler(event, context):
  try:
    LOGGER.info(f"REQUEST RECEIVED: {json.dumps(event, default=str)}")
    response_data = {}
    physical_resource_id = event.get("PhysicalResourceId")
    resource = event["ResourceProperties"].get("Resource")
    name = event["ResourceProperties"].get("Name")

    if event.get("RequestType") in ["Create", "Update"]:
      response = apply_name_tag(resource, name)
      LOGGER.info(f"response = {json.dumps(response, default=str)}")
    if event.get("RequestType") == "Delete":
      response = delete_name_tag(resource)
      LOGGER.info(f"response = {json.dumps(response, default=str)}")

    LOGGER.info("Sending Custom Resource Response")
    cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data, physical_resource_id)
    return
  except Exception as error:
    LOGGER.error(error)
    cfnresponse.send(event, context, cfnresponse.FAILED, {})
    return
"""


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    function_name = ref(LambdaFunctionName)
    handler = 'index.handler'
    role = get_att(TagVpcPeeringConnectionsLambdaRole, "Arn")
    runtime = 'python3.12'
    memory_size = 128
    timeout = 120
    environment = TagVpcPeeringConnectionsLambdaFunctionEnvironment
    code = TagVpcPeeringConnectionsLambdaFunctionCode


@cloudformation_dataclass
class TagVpcPeeringConnectionsResource:
    """Custom::TagVpcPeeringConnection resource."""

    # Unknown resource type: Custom::TagVpcPeeringConnection
    resource: CloudFormationResource
    service_token = get_att(TagVpcPeeringConnectionsLambdaFunction, "Arn")
    resource = ref(VPCPeeringConnectionId)
    name = ref(PeerName)
