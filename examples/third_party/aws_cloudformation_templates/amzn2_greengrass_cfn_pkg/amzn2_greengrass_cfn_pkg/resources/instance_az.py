from __future__ import annotations

"""InstanceAZ - Custom::InstanceAZ resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceAZ:
    """Custom::InstanceAZ resource."""

    # Unknown resource type: Custom::InstanceAZ
    resource: CloudFormationResource
    region = AWS_REGION
    service_token = get_att(InstanceAZFunction, "Arn")
