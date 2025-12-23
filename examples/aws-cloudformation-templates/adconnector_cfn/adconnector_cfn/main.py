"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This template creates an AD Connector to connect to an on-premises directory. Tasks accomplished, (1) create AD Connector (2) option to create seamless domain join resources for Windows & Linux EC2 instances (3) option to create a domain members security group that allows all PrivateIP communications inbound (4) option to create DHCPOptionSet pointing to Domain DNS servers',
        parameters=[ADConnectorDescription, ADConnectorSize, CreateDHCPOptionSet, CreateADConnectorDomainMembersSG, CreateLinuxEC2DomainJoinResources, CreateWindowsEC2DomainJoinResources, DomainDNSName, DomainDNSServers, DomainNetBiosName, DomainJoinUser, DomainJoinUserPassword, LambdaFunctionName, LambdaLogLevel, LambdaLogsLogGroupRetention, LambdaLogsCloudWatchKMSKey, LambdaS3BucketName, LambdaZipFileName, PrivateSubnet1ID, PrivateSubnet2ID, SecretsManagerDomainCredentialsSecretsKMSKey, SSMLogsBucketName, VPCID],
        outputs=[ADConnectorDirectoryIdOutput, ADConnectorDirectoryNameOutput, ADConnectorADConnectorDomainMembersSGOutput, ADConnectorWindowsEC2SeamlessDomainJoinInstanceProfileOutput, ADConnectorWindowsEC2SeamlessDomainJoinRoleOutput, ADConnectorLinuxEC2SeamlessDomainJoinInstanceProfileOutput, ADConnectorLinuxEC2SeamlessDomainJoinRoleOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
