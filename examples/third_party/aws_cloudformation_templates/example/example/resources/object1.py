"""Object1 - AWS::S3::Object resource."""

from .. import *  # noqa: F403


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
