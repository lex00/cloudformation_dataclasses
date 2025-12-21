from __future__ import annotations

"""ADConnectorLinuxEC2SeamlessDomainJoinSecret - AWS::SecretsManager::Secret resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorLinuxEC2SeamlessDomainJoinSecret:
    """AWS::SecretsManager::Secret resource."""

    resource: Secret
    name = Sub('aws/directory-services/${ADConnectorResource}/seamless-domain-join')
    description = Sub('AD Credentials for Seamless Domain Join Windows/Linux EC2 instances to ${DomainNetBiosName} Domain via AD Connector')
    secret_string = Sub('{ "awsSeamlessDomainUsername" : "${DomainJoinUser}", "awsSeamlessDomainPassword" : "${DomainJoinUserPassword}" }')
    kms_key_id = If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", ref(SecretsManagerDomainCredentialsSecretsKMSKey), AWS_NO_VALUE)
    condition = 'LinuxEC2DomainJoinResourcesCondition'
    deletion_policy = 'Retain'
