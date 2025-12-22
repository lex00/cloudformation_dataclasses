"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorDirectoryIdOutput:
    """AD Connector Directory ID"""

    resource: Output
    value = ref("ADConnectorResource")
    description = 'AD Connector Directory ID'
    export_name = Sub('${AWS::StackName}-ADConnectorDirectoryId')


@cloudformation_dataclass
class ADConnectorDirectoryNameOutput:
    """AD Connector Directory Name"""

    resource: Output
    value = ref(DomainDNSName)
    description = 'AD Connector Directory Name'
    export_name = Sub('${AWS::StackName}-ADConnectorDirectoryName')


@cloudformation_dataclass
class ADConnectorADConnectorDomainMembersSGOutput:
    """ADConnector Domain Members Security Group"""

    resource: Output
    value = ref("ADConnectorDomainMembersSG")
    description = 'ADConnector Domain Members Security Group'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorDomainMembersSG')
    condition = 'DomainMembersSGCondition'


@cloudformation_dataclass
class ADConnectorWindowsEC2SeamlessDomainJoinInstanceProfileOutput:
    """IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector"""

    resource: Output
    value = ref("ADConnectorWindowsEC2DomainJoinInstanceProfile")
    description = 'IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorWindowsEC2DomainJoinProfile')
    condition = 'WindowsEC2DomainJoinResourcesCondition'


@cloudformation_dataclass
class ADConnectorWindowsEC2SeamlessDomainJoinRoleOutput:
    """IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector"""

    resource: Output
    value = ref("ADConnectorWindowsEC2DomainJoinRole")
    description = 'IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorWindowsEC2DomainJoinRole')
    condition = 'WindowsEC2DomainJoinResourcesCondition'


@cloudformation_dataclass
class ADConnectorLinuxEC2SeamlessDomainJoinInstanceProfileOutput:
    """IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector"""

    resource: Output
    value = ref("ADConnectorLinuxEC2DomainJoinInstanceProfile")
    description = 'IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorLinuxEC2DomainJoinProfile')
    condition = 'LinuxEC2DomainJoinResourcesCondition'


@cloudformation_dataclass
class ADConnectorLinuxEC2SeamlessDomainJoinRoleOutput:
    """IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector"""

    resource: Output
    value = ref("ADConnectorLinuxEC2DomainJoinRole")
    description = 'IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorLinuxEC2DomainJoinRole')
    condition = 'LinuxEC2DomainJoinResourcesCondition'
