"""KmsKeyAlias - AWS::KMS::Alias resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KmsKeyAlias:
    """AWS::KMS::Alias resource."""

    resource: Alias
    alias_name = Sub('alias/${AWS::StackName}-${AWS::AccountId}-kms-key')
    target_key_id = ref(KmsKey)
