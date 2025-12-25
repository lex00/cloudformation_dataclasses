"""Stack outputs."""

from .. import *  # noqa: F403, F401

ClusterArnOutput = Output(
    value=get_att(EcsCluster, "Arn"),
    description="ECS Cluster ARN",
)

ServiceNameOutput = Output(
    value=get_att(WebService, "Name"),
    description="ECS Service Name",
)

ServiceArnOutput = Output(
    value=get_att(WebService, "ServiceArn"),
    description="ECS Service ARN",
)

__all__ = [
    "ClusterArnOutput",
    "ServiceNameOutput",
    "ServiceArnOutput",
]
