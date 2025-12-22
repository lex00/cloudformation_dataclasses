"""Object4 - AWS::S3::Object resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Object4S3Location:
    resource: databrew.S3Location
    bucket = ref(Bucket)
    key = 'readme.md'


@cloudformation_dataclass
class Object4:
    """AWS::S3::Object resource."""

    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    target = Object4S3Location
    url = 'https://raw.githubusercontent.com/aws-cloudformation/aws-cloudformation-templates/main/README.md'
    depends_on = ["Bucket"]
