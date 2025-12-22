from __future__ import annotations

"""TagVpcPeeringConnectionsResource - Custom::TagVpcPeeringConnection resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TagVpcPeeringConnectionsResource:
    """Custom::TagVpcPeeringConnection resource."""

    # Unknown resource type: Custom::TagVpcPeeringConnection
    resource: CloudFormationResource
    service_token: GetAtt[TagVpcPeeringConnectionsLambdaFunction] = get_att("Arn")
    resource = ref(VPCPeeringConnectionId)
    name = ref(PeerName)
