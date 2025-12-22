"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AppName:
    """This name is used as a prefix for resource names"""

    resource: Parameter
    type = STRING
    description = 'This name is used as a prefix for resource names'
    default = 'rain-webapp-sample'


@cloudformation_dataclass
class LambdaCodeS3Bucket:
    """The bucket where your lambda handler is"""

    resource: Parameter
    type = STRING
    description = 'The bucket where your lambda handler is'
    default = 'rain-artifacts-207567786752-us-east-1'


@cloudformation_dataclass
class LambdaCodeS3Key:
    """The object key for your lambda handler"""

    resource: Parameter
    type = STRING
    description = 'The object key for your lambda handler'
    default = '512113b95e9fc6345b2e19a43350af82aaa815011120288f16b1f281d5efdc95'
