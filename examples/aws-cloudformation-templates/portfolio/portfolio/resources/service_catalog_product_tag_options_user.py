"""ServiceCatalogProductTagOptionsUser - AWS::ServiceCatalog::TagOption resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsUser:
    """AWS::ServiceCatalog::TagOption resource."""

    resource: servicecatalog.TagOption
    active = ref(ActivateProductTagOptions)
    key = 'User'
    value = Sub('${ProductUser}')
