"""IoTThingPrincipalAttachment - AWS::IoT::ThingPrincipalAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IoTThingPrincipalAttachment:
    """AWS::IoT::ThingPrincipalAttachment resource."""

    resource: iot.ThingPrincipalAttachment
    principal = ref(CertificateARN)
    thing_name = ref(IoTThing)
