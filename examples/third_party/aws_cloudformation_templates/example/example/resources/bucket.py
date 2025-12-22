from __future__ import annotations

"""Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
