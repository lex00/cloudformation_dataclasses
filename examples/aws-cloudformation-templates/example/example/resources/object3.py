"""Object3 - AWS::S3::Object resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Object3ManifestFileLocation:
    resource: quicksight.data_source.ManifestFileLocation
    bucket = get_att(Object1, "Bucket")
    key = get_att(Object1, "Key")


@cloudformation_dataclass
class Object3ManifestFileLocation1:
    resource: quicksight.data_source.ManifestFileLocation
    bucket = ref(Bucket)
    key = 'README-copy.md'


@cloudformation_dataclass
class Object3:
    """AWS::S3::Object resource."""

    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    source = Object3ManifestFileLocation
    target = Object3ManifestFileLocation1
    depends_on = ["Bucket"]
