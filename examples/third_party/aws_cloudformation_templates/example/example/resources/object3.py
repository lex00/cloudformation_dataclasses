from __future__ import annotations

"""Object3 - AWS::S3::Object resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Object3S3Location:
    resource: S3Location
    bucket: GetAtt[Object1] = get_att("Bucket")
    key: GetAtt[Object1] = get_att("Key")


@cloudformation_dataclass
class Object3S3Location1:
    resource: S3Location
    bucket: Ref[Bucket] = ref()
    key = 'README-copy.md'


@cloudformation_dataclass
class Object3:
    """AWS::S3::Object resource."""

    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    source = Object3S3Location
    target = Object3S3Location1
    depends_on = ["Bucket"]
