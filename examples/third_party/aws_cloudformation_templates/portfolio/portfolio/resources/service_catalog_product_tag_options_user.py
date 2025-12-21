from __future__ import annotations

"""ServiceCatalogProductTagOptionsUser - AWS::ServiceCatalog::TagOption resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsUser:
    """AWS::ServiceCatalog::TagOption resource."""

    resource: TagOption
    active = ref(ActivateProductTagOptions)
    key = 'User'
    value = Sub('${ProductUser}')
