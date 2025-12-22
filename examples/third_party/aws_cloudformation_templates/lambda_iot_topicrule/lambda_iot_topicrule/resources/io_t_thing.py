from __future__ import annotations

"""IoTThing - AWS::IoT::Thing resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IoTThing:
    """AWS::IoT::Thing resource."""

    resource: Thing
    thing_name = ref(MyLambda)
