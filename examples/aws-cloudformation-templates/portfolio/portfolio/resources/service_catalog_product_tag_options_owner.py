"""ServiceCatalogProductTagOptionsOwner - AWS::ServiceCatalog::TagOption resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsOwner:
    """AWS::ServiceCatalog::TagOption resource."""

    resource: servicecatalog.TagOption
    active = ref(ActivateProductTagOptions)
    key = 'Owner'
    value = Sub('${ProductOwner}')
