"""IoTThing - Custom::IoTThing resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IoTThing:
    """Custom::IoTThing resource."""

    # Unknown resource type: Custom::IoTThing
    resource: CloudFormationResource
    service_token = get_att(CreateThingFunction, "Arn")
    thing_name = Join('_', [
    ref(CoreName),
    'Core',
])
