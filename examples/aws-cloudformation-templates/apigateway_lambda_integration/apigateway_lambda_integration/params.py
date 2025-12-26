"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ApiType:
    """The Endpoint type for RESTApi"""

    resource: Parameter
    type = STRING
    description = 'The Endpoint type for RESTApi'
    default = 'REGIONAL'
    allowed_values = [
    'EDGE',
    'REGIONAL',
    'PRIVATE',
]


@cloudformation_dataclass
class ApigatewayTimeout:
    """ApiGateway Backend Integration timeout in milliseconds"""

    resource: Parameter
    type = NUMBER
    description = 'ApiGateway Backend Integration timeout in milliseconds'
    default = '29000'
    min_value = 50
    max_value = 29000


@cloudformation_dataclass
class LambdaFunctionName:
    """The Name for the Lambda Function"""

    resource: Parameter
    type = STRING
    description = 'The Name for the Lambda Function'
    default = 'My-APIGW-Integ-Function'
