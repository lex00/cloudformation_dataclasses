"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import AWSManagedADDomainDNSName, AWSManagedADDomainNetBiosName, AWSManagedADEdition, CreateDHCPOptionSet, CreateDomainMembersSG, CreateLinuxEC2DomainJoinResources, CreateWindowsEC2DomainJoinResources, DHCPOptionSetConditionCondition, DomainMembersSGConditionCondition, LinuxEC2DomainJoinResourcesConditionCondition, PrivateSubnet1ID, PrivateSubnet2ID, SSMLogsBucketName, SSMLogsBucketNameConditionCondition, SecretsManagerDomainCredentialsSecretsKMSKey, SecretsManagerDomainCredentialsSecretsKMSKeyConditionCondition, VPCID, WindowsEC2DomainJoinResourcesConditionCondition
from .outputs import AWSManagedADAWSManagedADDomainMembersSGOutput, AWSManagedADDirectoryIdOutput, AWSManagedADDirectoryNameOutput, AWSManagedADLinuxEC2SeamlessDomainJoinInstanceProfileOutput, AWSManagedADLinuxEC2SeamlessDomainJoinRoleOutput, AWSManagedADWindowsEC2SeamlessDomainJoinInstanceProfileOutput, AWSManagedADWindowsEC2SeamlessDomainJoinRoleOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This template creates an AWS Managed Microsoft AD directory. Tasks accomplished, (1) create AWS Managed Microsoft AD directory (2) option to create seamless domain join resources for Windows & Linux EC2 instances (3) option to create a domain members security group that allows all PrivateIP communications inbound (4) option to create DHCPOptionSet pointing to AWS Managed Microsoft AD DNS servers',
        parameters=[AWSManagedADDomainDNSName, AWSManagedADDomainNetBiosName, AWSManagedADEdition, CreateDHCPOptionSet, CreateDomainMembersSG, CreateLinuxEC2DomainJoinResources, CreateWindowsEC2DomainJoinResources, PrivateSubnet1ID, PrivateSubnet2ID, SecretsManagerDomainCredentialsSecretsKMSKey, SSMLogsBucketName, VPCID],
        outputs=[AWSManagedADDirectoryIdOutput, AWSManagedADDirectoryNameOutput, AWSManagedADAWSManagedADDomainMembersSGOutput, AWSManagedADWindowsEC2SeamlessDomainJoinInstanceProfileOutput, AWSManagedADWindowsEC2SeamlessDomainJoinRoleOutput, AWSManagedADLinuxEC2SeamlessDomainJoinInstanceProfileOutput, AWSManagedADLinuxEC2SeamlessDomainJoinRoleOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
