"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AWSManagedADDirectoryIdOutput:
    """AWS Managed Microsoft AD Directory ID"""

    resource: Output
    value = ref("AWSManagedAD")
    description = 'AWS Managed Microsoft AD Directory ID'
    export_name = Sub('${AWS::StackName}-AWSManagedADDirectoryId')


@cloudformation_dataclass
class AWSManagedADDirectoryNameOutput:
    """AWS Managed Microsoft AD Directory Name"""

    resource: Output
    value = ref(AWSManagedADDomainDNSName)
    description = 'AWS Managed Microsoft AD Directory Name'
    export_name = Sub('${AWS::StackName}-AWSManagedADDirectoryName')


@cloudformation_dataclass
class AWSManagedADAWSManagedADDomainMembersSGOutput:
    """AWS Managed Microsoft AD Domain Members Security Group"""

    resource: Output
    value = ref("AWSManagedADDomainMembersSG")
    description = 'AWS Managed Microsoft AD Domain Members Security Group'
    export_name = Sub('${AWS::StackName}-${AWSManagedADDomainNetBiosName}-AWSManagedADDomainMembersSG')
    condition = 'DomainMembersSGCondition'


@cloudformation_dataclass
class AWSManagedADWindowsEC2SeamlessDomainJoinInstanceProfileOutput:
    """IAM Instance Profile with SSM Document Rights to Join Windows Computers via AWS Managed Microsoft AD"""

    resource: Output
    value = ref("AWSManagedADWindowsEC2DomainJoinInstanceProfile")
    description = 'IAM Instance Profile with SSM Document Rights to Join Windows Computers via AWS Managed Microsoft AD'
    export_name = Sub('${AWS::StackName}-${AWSManagedADDomainNetBiosName}-AWSManagedADWindowsEC2DomainJoinProfile')
    condition = 'WindowsEC2DomainJoinResourcesCondition'


@cloudformation_dataclass
class AWSManagedADWindowsEC2SeamlessDomainJoinRoleOutput:
    """IAM Instance Profile with SSM Document Rights to Join Windows Computers via AWS Managed Microsoft AD"""

    resource: Output
    value = ref("AWSManagedADWindowsEC2DomainJoinRole")
    description = 'IAM Instance Profile with SSM Document Rights to Join Windows Computers via AWS Managed Microsoft AD'
    export_name = Sub('${AWS::StackName}-${AWSManagedADDomainNetBiosName}-AWSManagedADWindowsEC2DomainJoinRole')
    condition = 'WindowsEC2DomainJoinResourcesCondition'


@cloudformation_dataclass
class AWSManagedADLinuxEC2SeamlessDomainJoinInstanceProfileOutput:
    """IAM Instance Profile with SSM Document Rights to Join Linux Computers via AWS Managed Microsoft AD"""

    resource: Output
    value = ref("AWSManagedADLinuxEC2DomainJoinInstanceProfile")
    description = 'IAM Instance Profile with SSM Document Rights to Join Linux Computers via AWS Managed Microsoft AD'
    export_name = Sub('${AWS::StackName}-${AWSManagedADDomainNetBiosName}-AWSManagedADLinuxEC2DomainJoinProfile')
    condition = 'LinuxEC2DomainJoinResourcesCondition'


@cloudformation_dataclass
class AWSManagedADLinuxEC2SeamlessDomainJoinRoleOutput:
    """IAM Instance Profile with SSM Document Rights to Join Linux Computers via AWS Managed Microsoft AD"""

    resource: Output
    value = ref("AWSManagedADLinuxEC2DomainJoinRole")
    description = 'IAM Instance Profile with SSM Document Rights to Join Linux Computers via AWS Managed Microsoft AD'
    export_name = Sub('${AWS::StackName}-${AWSManagedADDomainNetBiosName}-AWSManagedADLinuxEC2DomainJoinRole')
    condition = 'LinuxEC2DomainJoinResourcesCondition'
