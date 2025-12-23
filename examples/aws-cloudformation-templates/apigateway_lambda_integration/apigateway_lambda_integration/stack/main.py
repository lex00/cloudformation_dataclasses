"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RestApi:
    """AWS::ApiGateway::RestApi resource."""

    resource: apigateway.RestApi
    description = 'My Rest API'
    name = 'MyApi'
    endpoint_configuration = {
        'Types': [ref(ApiType)],
    }


@cloudformation_dataclass
class ApiResource:
    """AWS::ApiGateway::Resource resource."""

    resource: apigateway.Resource
    parent_id = get_att(RestApi, "RootResourceId")
    rest_api_id = ref(RestApi)
    path_part = '{city}'


@cloudformation_dataclass
class RequestModel:
    """AWS::ApiGateway::Model resource."""

    resource: apigateway.Model
    content_type = 'application/json'
    name = 'MyModel'
    rest_api_id = ref(RestApi)
    schema = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'title': 'MyModel',
        'type': 'object',
        'properties': {
            'callerName': {
                'type': 'string',
            },
        },
    }


@cloudformation_dataclass
class LambdaIamRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class LambdaIamRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIamRoleAllowStatement0]


@cloudformation_dataclass
class LambdaIamRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = LambdaIamRoleAssumeRolePolicyDocument
    role_name = 'LambdaRole'
    policies = [{
        'PolicyName': 'LambdaApipolicy',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Effect': 'Allow',
                    'Action': ['logs:CreateLogGroup'],
                    'Resource': Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:*'),
                },
                {
                    'Effect': 'Allow',
                    'Action': [
                        'logs:CreateLogStream',
                        'logs:PutLogEvents',
                    ],
                    'Resource': Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/${LambdaFunctionName}:*'),
                },
            ],
        },
    }]


@cloudformation_dataclass
class LambdaFunctionCode:
    resource: lambda_.function.Code
    zip_file = {
        'Rain::Embed': 'handler.py',
    }


@cloudformation_dataclass
class LambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    code = LambdaFunctionCode
    handler = 'index.lambda_handler'
    function_name = ref(LambdaFunctionName)
    memory_size = '128'
    runtime = 'python3.12'
    timeout = '10'
    role = get_att(LambdaIamRole, "Arn")


@cloudformation_dataclass
class ApiMethod:
    """AWS::ApiGateway::Method resource."""

    resource: apigateway.Method
    http_method = 'ANY'
    authorization_type = 'NONE'
    request_parameters = {
        'method.request.path.city': 'true',
        'method.request.querystring.time': 'true',
        'method.request.header.day': 'true',
    }
    method_responses = [{
        'StatusCode': '200',
    }]
    integration = {
        'IntegrationHttpMethod': 'POST',
        'Type': 'AWS',
        'TimeoutInMillis': ref(ApigatewayTimeout),
        'Uri': Join('', [
    'arn:',
    AWS_PARTITION,
    ':apigateway:',
    AWS_REGION,
    ':lambda:path/2015-03-31/functions/',
    get_att(LambdaFunction, "Arn"),
    '/invocations',
]),
        'RequestTemplates': {
            'application/json': """#set($inputRoot = $input.path('$'))
    {
      "city": "$input.params('city')",
      "time": "$input.params('time')",
      "day":  "$input.params('day')",
      "name": "$inputRoot.callerName"
    }
""",
        },
        'IntegrationResponses': [{
            'StatusCode': '200',
        }],
    }
    resource_id = ref(ApiResource)
    rest_api_id = ref(RestApi)
    request_models = {
        'application/json': ref(RequestModel),
    }


@cloudformation_dataclass
class LambdaApiGatewayInvoke:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(LambdaFunction, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Join('', [
    'arn:aws:execute-api:',
    AWS_REGION,
    ':',
    AWS_ACCOUNT_ID,
    ':',
    ref(RestApi),
    '/*/*/*',
])
