"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class BucketName:
    """The name of the S3 Bucket to create, make this unique"""

    resource: Parameter
    type = STRING
    description = 'The name of the S3 Bucket to create, make this unique'


@cloudformation_dataclass
class PublisherAccountID:
    """The AWS account ID with whom you are sharing access"""

    resource: Parameter
    type = STRING
    description = 'The AWS account ID with whom you are sharing access'
