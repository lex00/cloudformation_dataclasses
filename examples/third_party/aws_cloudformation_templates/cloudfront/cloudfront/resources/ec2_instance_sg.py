"""EC2InstanceSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2InstanceSGAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AppName}-${Environment}-ec2-instance-SG')


@cloudformation_dataclass
class EC2InstanceSGAssociationParameter1:
    resource: AssociationParameter
    key = 'Environment'
    value = ref(Environment)


@cloudformation_dataclass
class EC2InstanceSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'EC2 Instance Security Group'
    vpc_id = ref(VpcId)
    tags = [EC2InstanceSGAssociationParameter, EC2InstanceSGAssociationParameter1]
