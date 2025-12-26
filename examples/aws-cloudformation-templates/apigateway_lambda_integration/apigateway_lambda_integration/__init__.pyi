"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
    Parameter,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import apigateway, iam, lambda_
from cloudformation_dataclasses.intrinsics import (
    AWS_ACCOUNT_ID,
    AWS_PARTITION,
    AWS_REGION,
    Join,
    Sub,
)

from .main import ApiMethod as ApiMethod
from .main import ApiMethodIntegration as ApiMethodIntegration
from .main import ApiMethodIntegrationResponse as ApiMethodIntegrationResponse
from .main import ApiMethodMethodResponse as ApiMethodMethodResponse
from .main import ApiResource as ApiResource
from .main import LambdaApiGatewayInvoke as LambdaApiGatewayInvoke
from .main import LambdaFunction as LambdaFunction
from .main import LambdaFunctionCode as LambdaFunctionCode
from .main import RequestModel as RequestModel
from .main import RestApi as RestApi
from .main import RestApiEndpointConfiguration as RestApiEndpointConfiguration
from .params import ApiType as ApiType
from .params import ApigatewayTimeout as ApigatewayTimeout
from .params import LambdaFunctionName as LambdaFunctionName
from .security import LambdaIamRole as LambdaIamRole
from .security import LambdaIamRoleAllowStatement0 as LambdaIamRoleAllowStatement0
from .security import LambdaIamRoleAllowStatement0_1 as LambdaIamRoleAllowStatement0_1
from .security import LambdaIamRoleAllowStatement1 as LambdaIamRoleAllowStatement1
from .security import LambdaIamRoleAssumeRolePolicyDocument as LambdaIamRoleAssumeRolePolicyDocument
from .security import LambdaIamRolePolicies0PolicyDocument as LambdaIamRolePolicies0PolicyDocument
from .security import LambdaIamRolePolicy as LambdaIamRolePolicy

__all__: list[str] = ['AWS_ACCOUNT_ID', 'AWS_PARTITION', 'AWS_REGION', 'ApiMethod', 'ApiMethodIntegration', 'ApiMethodIntegrationResponse', 'ApiMethodMethodResponse', 'ApiResource', 'ApiType', 'ApigatewayTimeout', 'Join', 'LambdaApiGatewayInvoke', 'LambdaFunction', 'LambdaFunctionCode', 'LambdaFunctionName', 'LambdaIamRole', 'LambdaIamRoleAllowStatement0', 'LambdaIamRoleAllowStatement0_1', 'LambdaIamRoleAllowStatement1', 'LambdaIamRoleAssumeRolePolicyDocument', 'LambdaIamRolePolicies0PolicyDocument', 'LambdaIamRolePolicy', 'NUMBER', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'RequestModel', 'RestApi', 'RestApiEndpointConfiguration', 'STRING', 'Sub', 'Template', 'apigateway', 'cloudformation_dataclass', 'get_att', 'iam', 'lambda_', 'ref', 'setup_resources']
