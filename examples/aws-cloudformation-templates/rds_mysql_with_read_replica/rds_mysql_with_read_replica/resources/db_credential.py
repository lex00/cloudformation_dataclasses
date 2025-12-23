"""DBCredential - AWS::SecretsManager::Secret resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DBCredentialGenerateSecretString:
    resource: secretsmanager.secret.GenerateSecretString
    password_length = 16
    exclude_characters = '"@/\\'
    require_each_included_type = True


@cloudformation_dataclass
class DBCredential:
    """AWS::SecretsManager::Secret resource."""

    resource: secretsmanager.Secret
    generate_secret_string = DBCredentialGenerateSecretString
