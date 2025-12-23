"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TransformExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class TransformExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [TransformExecutionRoleAllowStatement0]


@cloudformation_dataclass
class TransformExecutionRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = TransformExecutionRoleAssumeRolePolicyDocument
    path = '/'
    policies = [{
        'PolicyName': 'root',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Effect': 'Allow',
                'Action': ['logs:*'],
                'Resource': 'arn:aws:logs:*:*:*',
            }],
        },
    }]
    managed_policy_arns = [If("AdditionalPolicyProvided", ref(AdditionalExecutionPolicy), AWS_NO_VALUE)]


@cloudformation_dataclass
class TransformFunctionCode:
    resource: lambda_.function.Code
    zip_file = {
        'Rain::Embed': 'handler.py',
    }


@cloudformation_dataclass
class TransformFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    description = 'Support for the PyPlate CloudFormation macro'
    code = TransformFunctionCode
    handler = 'index.handler'
    runtime = 'python3.11'
    role = get_att(TransformExecutionRole, "Arn")
    timeout = ref(LambdaTimeout)


@cloudformation_dataclass
class TransformFunctionPermissions:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(TransformFunction, "Arn")
    principal = 'cloudformation.amazonaws.com'


@cloudformation_dataclass
class Transform:
    """AWS::CloudFormation::Macro resource."""

    resource: cloudformation.Macro
    name = Sub('PyPlate')
    description = 'Processes inline python in templates'
    function_name = get_att(TransformFunction, "Arn")
