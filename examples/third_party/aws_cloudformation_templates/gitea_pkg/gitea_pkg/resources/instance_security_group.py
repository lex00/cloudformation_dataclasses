from __future__ import annotations

"""InstanceSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: Ingress
    description = 'Allow HTTP from com.amazonaws.global.cloudfront.origin-facing'
    ip_protocol = 'tcp'
    from_port = 8080
    to_port = 8080
    source_prefix_list_id = FindInMap("Prefixes", AWS_REGION, 'PrefixList')


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: Egress
    cidr_ip = '0.0.0.0/0'
    description = 'Allow all outbound traffic by default'
    ip_protocol = '-1'


@cloudformation_dataclass
class InstanceSecurityGroupAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitea-server-isg'


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'gitea-server-isg'
    security_group_ingress = [InstanceSecurityGroupIngress]
    security_group_egress = [InstanceSecurityGroupEgress]
    tags = [InstanceSecurityGroupAssociationParameter]
    vpc_id: Ref[NetworkVPC] = ref()
