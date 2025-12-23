"""DHCPOptionsVPCAssociation - AWS::EC2::VPCDHCPOptionsAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DHCPOptionsVPCAssociation:
    """AWS::EC2::VPCDHCPOptionsAssociation resource."""

    resource: VPCDHCPOptionsAssociation
    vpc_id = ref(VPCID)
    dhcp_options_id = ref(DHCPOptions)
    condition = 'DHCPOptionSetCondition'
