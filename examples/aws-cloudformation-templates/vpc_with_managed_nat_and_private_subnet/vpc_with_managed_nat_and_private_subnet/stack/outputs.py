"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCIdOutput:
    """VPCId of VPC"""

    resource: Output
    value = ref(VPC)
    description = 'VPCId of VPC'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-VPC')


@cloudformation_dataclass
class PublicSubnet0Output:
    """SubnetId of public subnet 0"""

    resource: Output
    value = ref(PublicSubnet0)
    description = 'SubnetId of public subnet 0'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PublicSubnet0')


@cloudformation_dataclass
class PublicSubnet1Output:
    """SubnetId of public subnet 1"""

    resource: Output
    value = ref(PublicSubnet1)
    description = 'SubnetId of public subnet 1'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PublicSubnet1')


@cloudformation_dataclass
class PrivateSubnet0Output:
    """SubnetId of private subnet 0"""

    resource: Output
    value = ref(PrivateSubnet0)
    description = 'SubnetId of private subnet 0'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PrivateSubnet0')


@cloudformation_dataclass
class PrivateSubnet1Output:
    """SubnetId of private subnet 1"""

    resource: Output
    value = ref(PrivateSubnet1)
    description = 'SubnetId of private subnet 1'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PrivateSubnet1')


@cloudformation_dataclass
class DefaultSecurityGroupOutput:
    """DefaultSecurityGroup Id"""

    resource: Output
    value = get_att(VPC, "DefaultSecurityGroup")
    description = 'DefaultSecurityGroup Id'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-DefaultSecurityGroup')
