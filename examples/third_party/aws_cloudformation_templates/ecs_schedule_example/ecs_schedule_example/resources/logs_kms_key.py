"""LogsKmsKey - AWS::KMS::Key resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LogsKmsKey:
    """AWS::KMS::Key resource."""

    resource: kms.Key
    description = 'ECS Logs Encryption Key'
    enable_key_rotation = True
