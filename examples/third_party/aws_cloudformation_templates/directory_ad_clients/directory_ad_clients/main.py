"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import AMAZONLINUX2, DirectoryID, DirectoryName, DomainDNSServer1, DomainDNSServer1ConditionCondition, DomainDNSServer2, DomainDNSServer2ConditionCondition, DomainDNSServer3, DomainDNSServer3ConditionCondition, DomainDNSServer4, DomainDNSServer4ConditionCondition, DomainDNSServersConditionCondition, DomainMember1NetBIOSName, DomainMember2NetBIOSName, DomainMember3NetBIOSName, DomainMember4NetBIOSName, DomainMembersInstanceType, DomainMembersLinuxInstanceProfile, DomainMembersSGID, DomainMembersWindowsInstanceProfile, EBSKMSKey, EBSKMSKeyConditionCondition, KeyPairName, PrivateSubnet1ID, PrivateSubnet2ID, SSMLogsBucketConditionCondition, SSMLogsBucketName, WINFULLBASE


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="This template creates (1) Linux and (3) Windows EC2 instances and joins them to Active Directory using the 'AWS-JoinDirectoryServiceDomain' SSM document via AD Connector or AWS Managed AD directory. By default, it relies on the DNS servers being used by the EC2 instances knowing how to resolve the AD domain (i.e., Route 53 Resolvers, DHCP OptionsSet), with an option to set the DNS servers manually on the EC2 instances, as necessary. Several methods used to initiate the domain join (1) Windows EC2 instance with inline SSM association (2) Windows and Linux EC2 instance with SSM association targeting EC2 instance IDs (3) Windows EC2 instance with SSM association targeting EC2 instance tags",
        parameters=[AMAZONLINUX2, DirectoryID, DirectoryName, DomainDNSServer1, DomainDNSServer2, DomainDNSServer3, DomainDNSServer4, DomainMember1NetBIOSName, DomainMember2NetBIOSName, DomainMember3NetBIOSName, DomainMember4NetBIOSName, DomainMembersInstanceType, DomainMembersLinuxInstanceProfile, DomainMembersWindowsInstanceProfile, DomainMembersSGID, EBSKMSKey, KeyPairName, PrivateSubnet1ID, PrivateSubnet2ID, SSMLogsBucketName, WINFULLBASE],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
