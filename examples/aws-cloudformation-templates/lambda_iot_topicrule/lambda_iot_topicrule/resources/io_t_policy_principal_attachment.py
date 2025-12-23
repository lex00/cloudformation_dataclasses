"""IoTPolicyPrincipalAttachment - AWS::IoT::PolicyPrincipalAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IoTPolicyPrincipalAttachment:
    """AWS::IoT::PolicyPrincipalAttachment resource."""

    resource: iot.PolicyPrincipalAttachment
    policy_name = ref(IoTPolicy)
    principal = ref(CertificateARN)
