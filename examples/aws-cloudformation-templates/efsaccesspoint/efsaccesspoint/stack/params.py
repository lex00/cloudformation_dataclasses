"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSFileSystemName:
    """Name for the EFS file system"""

    resource: Parameter
    type = STRING
    description = 'Name for the EFS file system'
    default = 'SampleEFSFilesystem'


@cloudformation_dataclass
class AccessPointName:
    """Name for the EFS access point"""

    resource: Parameter
    type = STRING
    description = 'Name for the EFS access point'
    default = 'SampleEFSAccessPoint'


@cloudformation_dataclass
class Subnet1:
    """A subnet for the first EFS mount target"""

    resource: Parameter
    type = ParameterType.AWS_EC2_SUBNET_ID
    description = 'A subnet for the first EFS mount target'


@cloudformation_dataclass
class Subnet2:
    """A subnet for the second EFS mount target"""

    resource: Parameter
    type = ParameterType.AWS_EC2_SUBNET_ID
    description = 'A subnet for the second EFS mount target'


@cloudformation_dataclass
class Subnet3:
    """A subnet for the third EFS mount target"""

    resource: Parameter
    type = ParameterType.AWS_EC2_SUBNET_ID
    description = 'A subnet for the third EFS mount target'


@cloudformation_dataclass
class SecurityGroup1:
    """Security group for the first EFS mount target"""

    resource: Parameter
    type = ParameterType.AWS_EC2_SECURITY_GROUP_ID
    description = 'Security group for the first EFS mount target'


@cloudformation_dataclass
class SecurityGroup2:
    """Security group for the second EFS mount target"""

    resource: Parameter
    type = ParameterType.AWS_EC2_SECURITY_GROUP_ID
    description = 'Security group for the second EFS mount target'


@cloudformation_dataclass
class SecurityGroup3:
    """Security group for the third EFS mount target"""

    resource: Parameter
    type = ParameterType.AWS_EC2_SECURITY_GROUP_ID
    description = 'Security group for the third EFS mount target'
