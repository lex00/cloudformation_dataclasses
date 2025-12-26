"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2, ssm
from cloudformation_dataclasses.aws.ec2.instance import AssociationParameter
from cloudformation_dataclasses.aws.ssm.association import S3OutputLocation
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    Base64,
    Condition,
    Equals,
    If,
    Not,
    Or,
    Sub,
)
from .params import *  # noqa: F403, F401

from .compute import DomainMember1WithInlineSsmAssociation as DomainMember1WithInlineSsmAssociation
from .compute import DomainMember1WithInlineSsmAssociationAssociationParameter as DomainMember1WithInlineSsmAssociationAssociationParameter
from .compute import DomainMember1WithInlineSsmAssociationAssociationParameter1 as DomainMember1WithInlineSsmAssociationAssociationParameter1
from .compute import DomainMember1WithInlineSsmAssociationAssociationParameter2 as DomainMember1WithInlineSsmAssociationAssociationParameter2
from .compute import DomainMember1WithInlineSsmAssociationBlockDeviceMapping as DomainMember1WithInlineSsmAssociationBlockDeviceMapping
from .compute import DomainMember1WithInlineSsmAssociationEbs as DomainMember1WithInlineSsmAssociationEbs
from .compute import DomainMember1WithInlineSsmAssociationSsmAssociation as DomainMember1WithInlineSsmAssociationSsmAssociation
from .compute import DomainMember2WithSsmAssociationInstance as DomainMember2WithSsmAssociationInstance
from .compute import DomainMember2WithSsmAssociationInstanceAssociationParameter as DomainMember2WithSsmAssociationInstanceAssociationParameter
from .compute import DomainMember2WithSsmAssociationInstanceBlockDeviceMapping as DomainMember2WithSsmAssociationInstanceBlockDeviceMapping
from .compute import DomainMember2WithSsmAssociationInstanceEbs as DomainMember2WithSsmAssociationInstanceEbs
from .compute import DomainMember3WithSsmAssociationTag as DomainMember3WithSsmAssociationTag
from .compute import DomainMember3WithSsmAssociationTagAssociationParameter as DomainMember3WithSsmAssociationTagAssociationParameter
from .compute import DomainMember3WithSsmAssociationTagAssociationParameter1 as DomainMember3WithSsmAssociationTagAssociationParameter1
from .compute import DomainMember3WithSsmAssociationTagBlockDeviceMapping as DomainMember3WithSsmAssociationTagBlockDeviceMapping
from .compute import DomainMember3WithSsmAssociationTagEbs as DomainMember3WithSsmAssociationTagEbs
from .compute import DomainMember4LinuxWithSsmAssociationInstance as DomainMember4LinuxWithSsmAssociationInstance
from .compute import DomainMember4LinuxWithSsmAssociationInstanceAssociationParameter as DomainMember4LinuxWithSsmAssociationInstanceAssociationParameter
from .compute import DomainMember4LinuxWithSsmAssociationInstanceBlockDeviceMapping as DomainMember4LinuxWithSsmAssociationInstanceBlockDeviceMapping
from .compute import DomainMember4LinuxWithSsmAssociationInstanceEbs as DomainMember4LinuxWithSsmAssociationInstanceEbs
from .params import AMAZONLINUX2 as AMAZONLINUX2
from .params import DirectoryID as DirectoryID
from .params import DirectoryName as DirectoryName
from .params import DomainDNSServer1 as DomainDNSServer1
from .params import DomainDNSServer1ConditionCondition as DomainDNSServer1ConditionCondition
from .params import DomainDNSServer2 as DomainDNSServer2
from .params import DomainDNSServer2ConditionCondition as DomainDNSServer2ConditionCondition
from .params import DomainDNSServer3 as DomainDNSServer3
from .params import DomainDNSServer3ConditionCondition as DomainDNSServer3ConditionCondition
from .params import DomainDNSServer4 as DomainDNSServer4
from .params import DomainDNSServer4ConditionCondition as DomainDNSServer4ConditionCondition
from .params import DomainDNSServersConditionCondition as DomainDNSServersConditionCondition
from .params import DomainMember1NetBIOSName as DomainMember1NetBIOSName
from .params import DomainMember2NetBIOSName as DomainMember2NetBIOSName
from .params import DomainMember3NetBIOSName as DomainMember3NetBIOSName
from .params import DomainMember4NetBIOSName as DomainMember4NetBIOSName
from .params import DomainMembersInstanceType as DomainMembersInstanceType
from .params import DomainMembersLinuxInstanceProfile as DomainMembersLinuxInstanceProfile
from .params import DomainMembersSGID as DomainMembersSGID
from .params import DomainMembersWindowsInstanceProfile as DomainMembersWindowsInstanceProfile
from .params import EBSKMSKey as EBSKMSKey
from .params import EBSKMSKeyConditionCondition as EBSKMSKeyConditionCondition
from .params import KeyPairName as KeyPairName
from .params import PrivateSubnet1ID as PrivateSubnet1ID
from .params import PrivateSubnet2ID as PrivateSubnet2ID
from .params import SSMLogsBucketConditionCondition as SSMLogsBucketConditionCondition
from .params import SSMLogsBucketName as SSMLogsBucketName
from .params import WINFULLBASE as WINFULLBASE
from .security import JoinDomainAssociationInstances as JoinDomainAssociationInstances
from .security import JoinDomainAssociationInstancesInstanceAssociationOutputLocation as JoinDomainAssociationInstancesInstanceAssociationOutputLocation
from .security import JoinDomainAssociationInstancesTarget as JoinDomainAssociationInstancesTarget
from .security import JoinDomainAssociationTags as JoinDomainAssociationTags
from .security import JoinDomainAssociationTagsInstanceAssociationOutputLocation as JoinDomainAssociationTagsInstanceAssociationOutputLocation
from .security import JoinDomainAssociationTagsTarget as JoinDomainAssociationTagsTarget

__all__: list[str] = ['AMAZONLINUX2', 'AWS_NO_VALUE', 'AssociationParameter', 'Base64', 'Condition', 'DirectoryID', 'DirectoryName', 'DomainDNSServer1', 'DomainDNSServer1ConditionCondition', 'DomainDNSServer2', 'DomainDNSServer2ConditionCondition', 'DomainDNSServer3', 'DomainDNSServer3ConditionCondition', 'DomainDNSServer4', 'DomainDNSServer4ConditionCondition', 'DomainDNSServersConditionCondition', 'DomainMember1NetBIOSName', 'DomainMember1WithInlineSsmAssociation', 'DomainMember1WithInlineSsmAssociationAssociationParameter', 'DomainMember1WithInlineSsmAssociationAssociationParameter1', 'DomainMember1WithInlineSsmAssociationAssociationParameter2', 'DomainMember1WithInlineSsmAssociationBlockDeviceMapping', 'DomainMember1WithInlineSsmAssociationEbs', 'DomainMember1WithInlineSsmAssociationSsmAssociation', 'DomainMember2NetBIOSName', 'DomainMember2WithSsmAssociationInstance', 'DomainMember2WithSsmAssociationInstanceAssociationParameter', 'DomainMember2WithSsmAssociationInstanceBlockDeviceMapping', 'DomainMember2WithSsmAssociationInstanceEbs', 'DomainMember3NetBIOSName', 'DomainMember3WithSsmAssociationTag', 'DomainMember3WithSsmAssociationTagAssociationParameter', 'DomainMember3WithSsmAssociationTagAssociationParameter1', 'DomainMember3WithSsmAssociationTagBlockDeviceMapping', 'DomainMember3WithSsmAssociationTagEbs', 'DomainMember4LinuxWithSsmAssociationInstance', 'DomainMember4LinuxWithSsmAssociationInstanceAssociationParameter', 'DomainMember4LinuxWithSsmAssociationInstanceBlockDeviceMapping', 'DomainMember4LinuxWithSsmAssociationInstanceEbs', 'DomainMember4NetBIOSName', 'DomainMembersInstanceType', 'DomainMembersLinuxInstanceProfile', 'DomainMembersSGID', 'DomainMembersWindowsInstanceProfile', 'EBSKMSKey', 'EBSKMSKeyConditionCondition', 'Equals', 'If', 'JoinDomainAssociationInstances', 'JoinDomainAssociationInstancesInstanceAssociationOutputLocation', 'JoinDomainAssociationInstancesTarget', 'JoinDomainAssociationTags', 'JoinDomainAssociationTagsInstanceAssociationOutputLocation', 'JoinDomainAssociationTagsTarget', 'KeyPairName', 'Not', 'Or', 'Parameter', 'ParameterType', 'PrivateSubnet1ID', 'PrivateSubnet2ID', 'S3OutputLocation', 'SSMLogsBucketConditionCondition', 'SSMLogsBucketName', 'STRING', 'Sub', 'Template', 'TemplateCondition', 'WINFULLBASE', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources', 'ssm']
