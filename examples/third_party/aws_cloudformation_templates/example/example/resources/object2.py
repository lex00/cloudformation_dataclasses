from __future__ import annotations

"""Object2 - AWS::S3::Object resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Object2:
    """AWS::S3::Object resource."""

    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    target = {
        'Bucket': ref("Bucket"),
        'Key': '1-pixel.gif',
        'ContentType': 'image/png',
    }
    base64_body = 'R0lGODdhAQABAIABAP///0qIbCwAAAAAAQABAAACAkQBADs='
    depends_on = ["Bucket"]
