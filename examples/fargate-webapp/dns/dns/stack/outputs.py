"""DNS stack outputs."""

from .. import *  # noqa: F403, F401
from dns import *  # noqa: F403, F401


HostedZoneIdOutput = Output(
    value=ref(HostedZone),
    description="Route53 Hosted Zone ID",
)

CertificateArnOutput = Output(
    value=ref(Certificate),
    description="ACM Certificate ARN",
)

NameServersOutput = Output(
    value=Join(",", get_att(HostedZone, "NameServers")),
    description="Nameservers for domain delegation (comma-separated)",
)
