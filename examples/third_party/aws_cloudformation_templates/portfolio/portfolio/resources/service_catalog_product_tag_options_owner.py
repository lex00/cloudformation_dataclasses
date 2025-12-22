"""ServiceCatalogProductTagOptionsOwner - AWS::ServiceCatalog::TagOption resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsOwner:
    """AWS::ServiceCatalog::TagOption resource."""

    resource: TagOption
    active = ref(ActivateProductTagOptions)
    key = 'Owner'
    value = Sub('${ProductOwner}')
