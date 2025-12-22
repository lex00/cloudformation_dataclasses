from __future__ import annotations

"""NeptuneDBSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneDBSGAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-neptune-sg')


@cloudformation_dataclass
class NeptuneDBSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'SG of Neptune DB'
    vpc_id = ImportValue(Sub('${VPCStack}-VPCID'))
    tags = [NeptuneDBSGAssociationParameter]
