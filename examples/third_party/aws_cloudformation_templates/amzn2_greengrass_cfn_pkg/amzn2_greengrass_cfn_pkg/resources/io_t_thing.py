from __future__ import annotations

"""IoTThing - Custom::IoTThing resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IoTThing:
    """Custom::IoTThing resource."""

    # Unknown resource type: Custom::IoTThing
    resource: CloudFormationResource
    service_token: GetAtt[CreateThingFunction] = get_att("Arn")
    thing_name = Join('_', [
    ref(CoreName),
    'Core',
])
