from __future__ import annotations

"""TagVpcPeeringConnectionsResource - Custom::TagVpcPeeringConnection resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TagVpcPeeringConnectionsResource:
    """Custom::TagVpcPeeringConnection resource."""

    # Unknown resource type: Custom::TagVpcPeeringConnection
    resource: CloudFormationResource
    service_token = get_att(TagVpcPeeringConnectionsLambdaFunction, "Arn")
    resource = ref(VPCPeeringConnectionId)
    name = ref(PeerName)
