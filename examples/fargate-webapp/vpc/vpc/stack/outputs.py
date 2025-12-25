"""VPC stack outputs."""

from .. import *  # noqa: F403, F401
from network import *  # noqa: F403, F401


VpcIdOutput = Output(
    value=ref(Vpc),
    description="VPC ID",
)

PublicSubnetIdsOutput = Output(
    value=Join(
        ",",
        [
            ref(PublicSubnet1),
            ref(PublicSubnet2),
            ref(PublicSubnet3),
        ],
    ),
    description="Public subnet IDs (comma-separated)",
)

PrivateSubnetIdsOutput = Output(
    value=Join(
        ",",
        [
            ref(PrivateSubnet1),
            ref(PrivateSubnet2),
            ref(PrivateSubnet3),
        ],
    ),
    description="Private subnet IDs (comma-separated)",
)

AvailabilityZonesOutput = Output(
    value=Join(
        ",",
        [
            get_att(PublicSubnet1, "AvailabilityZone"),
            get_att(PublicSubnet2, "AvailabilityZone"),
            get_att(PublicSubnet3, "AvailabilityZone"),
        ],
    ),
    description="Availability zones (comma-separated)",
)

VpcCidrOutput = Output(
    value=get_att(Vpc, "CidrBlock"),
    description="VPC CIDR block",
)
