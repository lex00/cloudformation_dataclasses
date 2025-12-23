"""ServiceCatalogCloudFormationProduct - AWS::ServiceCatalog::CloudFormationProduct resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceCatalogCloudFormationProductProvisioningParameter:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'Name'
    value = Sub('${AppName}')


@cloudformation_dataclass
class ServiceCatalogCloudFormationProductProvisioningParameter1:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'App'
    value = Sub('${AppName}')


@cloudformation_dataclass
class ServiceCatalogCloudFormationProductProvisioningParameter2:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'Dept'
    value = Sub('${Dept}')


@cloudformation_dataclass
class ServiceCatalogCloudFormationProductProvisioningParameter3:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'Env'
    value = Sub('${Env}')


@cloudformation_dataclass
class ServiceCatalogCloudFormationProductProvisioningParameter4:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'User'
    value = Sub('${User}')


@cloudformation_dataclass
class ServiceCatalogCloudFormationProductProvisioningParameter5:
    resource: servicecatalog.cloud_formation_provisioned_product.ProvisioningParameter
    key = 'Owner'
    value = Sub('${Owner}')


@cloudformation_dataclass
class ServiceCatalogCloudFormationProductProvisioningArtifactProperties:
    resource: servicecatalog.cloud_formation_product.ProvisioningArtifactProperties
    name = Sub('${ProvisioningArtifactNameParameter}')
    description = Sub('${ProvisioningArtifactDescriptionParameter}')
    info = {
        'LoadTemplateFromURL': Sub('${ProvisioningArtifactTemplateUrl}'),
    }


@cloudformation_dataclass
class ServiceCatalogCloudFormationProduct:
    """AWS::ServiceCatalog::CloudFormationProduct resource."""

    resource: CloudFormationProduct
    name = ref(SCProductName)
    description = ref(SCProductDescription)
    owner = ref(SCProductOwner)
    support_description = ref(SCProductSupport)
    distributor = ref(SCProductDistributor)
    support_email = ref(SCSupportEmail)
    support_url = Sub('${SCSupportUrl}')
    tags = [ServiceCatalogCloudFormationProductProvisioningParameter, ServiceCatalogCloudFormationProductProvisioningParameter1, ServiceCatalogCloudFormationProductProvisioningParameter2, ServiceCatalogCloudFormationProductProvisioningParameter3, ServiceCatalogCloudFormationProductProvisioningParameter4, ServiceCatalogCloudFormationProductProvisioningParameter5]
    provisioning_artifact_parameters = [ServiceCatalogCloudFormationProductProvisioningArtifactProperties]
