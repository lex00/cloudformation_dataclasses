"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AdditionalExecutionPolicy:
    """An optional IAM Policy ARN to add to the Lambda's execution role so that 
the template's Python code can call AWS services.
"""

    resource: Parameter
    type = STRING
    description = """An optional IAM Policy ARN to add to the Lambda's execution role so that 
the template's Python code can call AWS services.
"""


@cloudformation_dataclass
class LambdaTimeout:
    """Optional setting of the Lambda's execution timeout (in seconds). 
The default of 3 seconds won't be enough if you call AWS services; 
then at least 10 seconds is recommended, more depending on complexity.
"""

    resource: Parameter
    type = NUMBER
    description = """Optional setting of the Lambda's execution timeout (in seconds). 
The default of 3 seconds won't be enough if you call AWS services; 
then at least 10 seconds is recommended, more depending on complexity.
"""
    default = 3
    min_value = 3


@cloudformation_dataclass
class AdditionalPolicyProvidedCondition:
    resource: Condition
    expression = Not(Equals(ref(AdditionalExecutionPolicy), ''))
