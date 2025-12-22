from __future__ import annotations

"""NonExplodingBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NonExplodingBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
