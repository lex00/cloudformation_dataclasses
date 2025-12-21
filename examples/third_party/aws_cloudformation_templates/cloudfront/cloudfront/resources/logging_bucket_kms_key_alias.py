from __future__ import annotations

"""LoggingBucketKMSKeyAlias - AWS::KMS::Alias resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoggingBucketKMSKeyAlias:
    """AWS::KMS::Alias resource."""

    resource: Alias
    alias_name = Sub('alias/${AppName}/${Environment}/s3-logging-kms')
    target_key_id = Sub('${LoggingBucketKMSKey}')
