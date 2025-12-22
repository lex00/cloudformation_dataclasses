"""ALBExternalAccessSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ALBExternalAccessSGAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AppName}-${Environment}-alb-external-access-ingrees-SG')


@cloudformation_dataclass
class ALBExternalAccessSGAssociationParameter1:
    resource: AssociationParameter
    key = 'Environment'
    value = ref(Environment)


@cloudformation_dataclass
class ALBExternalAccessSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Allow external access to ALB'
    vpc_id = ref(VpcId)
    tags = [ALBExternalAccessSGAssociationParameter, ALBExternalAccessSGAssociationParameter1]
