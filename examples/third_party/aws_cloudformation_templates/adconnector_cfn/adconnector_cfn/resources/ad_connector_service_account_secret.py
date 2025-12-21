from __future__ import annotations

"""ADConnectorServiceAccountSecret - AWS::SecretsManager::Secret resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorServiceAccountSecret:
    """AWS::SecretsManager::Secret resource."""

    resource: Secret
    name = Sub('ADConnector-ServiceAccount-${DomainNetBiosName}-Domain')
    description = Sub('ADConnector Service Account for ${DomainNetBiosName} Domain')
    secret_string = Sub('{ "username" : "${DomainJoinUser}", "password" : "${DomainJoinUserPassword}" }')
    kms_key_id = If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", ref(SecretsManagerDomainCredentialsSecretsKMSKey), AWS_NO_VALUE)
    deletion_policy = 'Retain'
