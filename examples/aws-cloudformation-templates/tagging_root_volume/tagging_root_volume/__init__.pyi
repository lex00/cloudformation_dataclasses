"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    ParameterType,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2, iam
from cloudformation_dataclasses.intrinsics import AWS_STACK_NAME, Base64
from .params import *  # noqa: F403, F401

from .compute import LinuxInstance as LinuxInstance
from .compute import LinuxInstanceAssociationParameter as LinuxInstanceAssociationParameter
from .compute import LinuxInstanceBlockDeviceMapping as LinuxInstanceBlockDeviceMapping
from .compute import LinuxInstanceEbs as LinuxInstanceEbs
from .compute import WindowsInstance as WindowsInstance
from .compute import WindowsInstanceAssociationParameter as WindowsInstanceAssociationParameter
from .compute import WindowsInstanceBlockDeviceMapping as WindowsInstanceBlockDeviceMapping
from .compute import WindowsInstanceEbs as WindowsInstanceEbs
from .params import InstanceAZ as InstanceAZ
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import LinuxAMIID as LinuxAMIID
from .params import SubnetId as SubnetId
from .params import WindowsAMIID as WindowsAMIID
from .security import InstanceProfile as InstanceProfile
from .security import InstanceRole as InstanceRole
from .security import InstanceRoleAllowStatement0 as InstanceRoleAllowStatement0
from .security import InstanceRoleAllowStatement0_1 as InstanceRoleAllowStatement0_1
from .security import InstanceRoleAssumeRolePolicyDocument as InstanceRoleAssumeRolePolicyDocument
from .security import InstanceRolePolicies0PolicyDocument as InstanceRolePolicies0PolicyDocument
from .security import InstanceRolePolicy as InstanceRolePolicy

__all__: list[str] = ['AWS_STACK_NAME', 'Base64', 'InstanceAZ', 'InstanceProfile', 'InstanceRole', 'InstanceRoleAllowStatement0', 'InstanceRoleAllowStatement0_1', 'InstanceRoleAssumeRolePolicyDocument', 'InstanceRolePolicies0PolicyDocument', 'InstanceRolePolicy', 'InstanceType', 'KeyName', 'LinuxAMIID', 'LinuxInstance', 'LinuxInstanceAssociationParameter', 'LinuxInstanceBlockDeviceMapping', 'LinuxInstanceEbs', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'STRING', 'SubnetId', 'Template', 'WindowsAMIID', 'WindowsInstance', 'WindowsInstanceAssociationParameter', 'WindowsInstanceBlockDeviceMapping', 'WindowsInstanceEbs', 'cloudformation_dataclass', 'ec2', 'get_att', 'iam', 'ref', 'setup_resources']
