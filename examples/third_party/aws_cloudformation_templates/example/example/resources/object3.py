"""Object3 - AWS::S3::Object resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Object3S3Location:
    resource: databrew.S3Location
    bucket = get_att(Object1, "Bucket")
    key = get_att(Object1, "Key")


@cloudformation_dataclass
class Object3S3Location1:
    resource: databrew.S3Location
    bucket = ref(Bucket)
    key = 'README-copy.md'


@cloudformation_dataclass
class Object3:
    """AWS::S3::Object resource."""

    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    source = Object3S3Location
    target = Object3S3Location1
    depends_on = ["Bucket"]
