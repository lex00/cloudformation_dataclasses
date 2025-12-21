from __future__ import annotations

"""ECSCluster - AWS::ECS::Cluster resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSCluster:
    """AWS::ECS::Cluster resource."""

    resource: Cluster
