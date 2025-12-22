from __future__ import annotations

"""IoTPolicyPrincipalAttachment - AWS::IoT::PolicyPrincipalAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IoTPolicyPrincipalAttachment:
    """AWS::IoT::PolicyPrincipalAttachment resource."""

    resource: PolicyPrincipalAttachment
    policy_name = ref(IoTPolicy)
    principal = ref(CertificateARN)
