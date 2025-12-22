from __future__ import annotations

"""ServiceCatalogProductTagOptionsDept - AWS::ServiceCatalog::TagOption resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsDept:
    """AWS::ServiceCatalog::TagOption resource."""

    resource: TagOption
    active = ref(ActivateProductTagOptions)
    key = 'Dept'
    value = Sub('${ProductDept}')
