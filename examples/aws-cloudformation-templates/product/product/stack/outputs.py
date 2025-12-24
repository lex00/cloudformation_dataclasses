"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogCloudFormationProductNameOutput:
    resource: Output
    value = get_att(ServiceCatalogCloudFormationProduct, "ProductName")
    export_name = Sub('${AppName}-ServiceCatalogCloudFormationProductName')


@cloudformation_dataclass
class ServiceCatalogProvisioningArtifactIdsOutput:
    resource: Output
    value = get_att(ServiceCatalogCloudFormationProduct, "ProvisioningArtifactIds")
    export_name = Sub('${AppName}-ServiceCatalogCloudFormationProvisioningArtifactIds')


@cloudformation_dataclass
class ServiceCatalogProvisioningArtifactNamesOutput:
    resource: Output
    value = get_att(ServiceCatalogCloudFormationProduct, "ProvisioningArtifactNames")
    export_name = Sub('${AppName}-ServiceCatalogCloudFormationProvisioningArtifactNames')
