"""ALB stack outputs."""

from .. import *  # noqa: F403, F401

AlbArnOutput = Output(
    value=ref(ApplicationLoadBalancer),
    description="Application Load Balancer ARN",
)

AlbDnsNameOutput = Output(
    value=get_att(ApplicationLoadBalancer, "DNSName"),
    description="ALB DNS name",
)

AlbSecurityGroupIdOutput = Output(
    value=get_att(AlbSecurityGroup, "GroupId"),
    description="ALB Security Group ID",
)

TargetGroupArnOutput = Output(
    value=ref(TargetGroup),
    description="Target Group ARN",
)

HttpsListenerArnOutput = Output(
    value=ref(HttpsListener),
    description="HTTPS Listener ARN",
)
