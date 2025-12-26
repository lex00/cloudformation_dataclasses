"""Compute resources: TagVpcPeeringConnectionsLambdaFunction."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.lambda_ import Runtime


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
    runtime = Runtime.PYTHON3_12
    memory_size = 128
    timeout = 120
    environment = TagVpcPeeringConnectionsLambdaFunctionEnvironment
    code = TagVpcPeeringConnectionsLambdaFunctionCode
