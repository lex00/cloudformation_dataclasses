"""EFSSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EFSSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable NFS access from EC2'
    security_group_ingress = [{
        'FromPort': '2049',
        'IpProtocol': 'tcp',
        'ToPort': '2049',
        'SourceSecurityGroupId': get_att(InstanceSecurityGroup, "GroupId"),
    }]
    vpc_id = ref(VPC)
