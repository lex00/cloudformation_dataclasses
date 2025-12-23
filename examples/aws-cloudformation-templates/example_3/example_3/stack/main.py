"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket


@cloudformation_dataclass
class Object1:
    """AWS::S3::Object resource."""

    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    target = {
        'Bucket': ref(Bucket),
        'Key': 'README.md',
        'ContentType': 'text/markdown',
    }
    body = """# My text file

This is my text file;
there are many like it,
but this one is mine.
"""
    depends_on = ["Bucket"]


@cloudformation_dataclass
class Object2:
    """AWS::S3::Object resource."""

    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    target = {
        'Bucket': ref(Bucket),
        'Key': '1-pixel.gif',
        'ContentType': 'image/png',
    }
    base64_body = 'R0lGODdhAQABAIABAP///0qIbCwAAAAAAQABAAACAkQBADs='
    depends_on = ["Bucket"]


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


@cloudformation_dataclass
class Object4ManifestFileLocation:
    resource: quicksight.data_source.ManifestFileLocation
    bucket = ref(Bucket)
    key = 'readme.md'


@cloudformation_dataclass
class Object4:
    """AWS::S3::Object resource."""

    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    target = Object4ManifestFileLocation
    url = 'https://raw.githubusercontent.com/aws-cloudformation/aws-cloudformation-templates/main/README.md'
    depends_on = ["Bucket"]
