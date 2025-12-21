from __future__ import annotations

"""AWSManagedADLinuxEC2SeamlessDomainJoinSecret - AWS::SecretsManager::Secret resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AWSManagedADLinuxEC2SeamlessDomainJoinSecret:
    """AWS::SecretsManager::Secret resource."""

    resource: Secret
    name = Sub('aws/directory-services/${AWSManagedAD}/seamless-domain-join')
    description = Sub('AD Credentials for Seamless Domain Join Windows/Linux EC2 instances to ${AWSManagedADDomainNetBiosName} Domain via AWS Managed Microsoft AD')
    secret_string = '{ "awsSeamlessDomainUsername" : "Admin", "awsSeamlessDomainPassword" : "{{resolve:secretsmanager:AWSManagedADAdminPassword:SecretString:password}}" }'
    kms_key_id = If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", ref(SecretsManagerDomainCredentialsSecretsKMSKey), AWS_NO_VALUE)
    condition = 'LinuxEC2DomainJoinResourcesCondition'
