from __future__ import annotations

"""IoTThingPrincipalAttachment - AWS::IoT::ThingPrincipalAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IoTThingPrincipalAttachment:
    """AWS::IoT::ThingPrincipalAttachment resource."""

    resource: ThingPrincipalAttachment
    principal = ref(CertificateARN)
    thing_name: Ref[IoTThing] = ref()
