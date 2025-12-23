"""ServiceCatalogProductTagOptionsEnv - AWS::ServiceCatalog::TagOption resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogProductTagOptionsEnv:
    """AWS::ServiceCatalog::TagOption resource."""

    resource: servicecatalog.TagOption
    active = ref(ActivateProductTagOptions)
    key = 'Env'
    value = Sub('${ProductEnv}')
