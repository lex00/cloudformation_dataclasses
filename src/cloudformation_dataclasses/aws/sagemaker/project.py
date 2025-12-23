"""PropertyTypes for AWS::SageMaker::Project."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CfnStackParameter(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CfnTemplateProviderDetail(PropertyType):
    TEMPLATE_URL = "TemplateURL"
    PARAMETERS = "Parameters"
    TEMPLATE_NAME = "TemplateName"
    ROLE_ARN = "RoleARN"

    _property_mappings: ClassVar[dict[str, str]] = {
        "template_url": "TemplateURL",
        "parameters": "Parameters",
        "template_name": "TemplateName",
        "role_arn": "RoleARN",
    }

    template_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[list[CfnStackParameter]] = None
    template_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProvisioningParameter(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceCatalogProvisionedProductDetails(PropertyType):
    PROVISIONED_PRODUCT_STATUS_MESSAGE = "ProvisionedProductStatusMessage"
    PROVISIONED_PRODUCT_ID = "ProvisionedProductId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "provisioned_product_status_message": "ProvisionedProductStatusMessage",
        "provisioned_product_id": "ProvisionedProductId",
    }

    provisioned_product_status_message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    provisioned_product_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServiceCatalogProvisioningDetails(PropertyType):
    PATH_ID = "PathId"
    PROVISIONING_PARAMETERS = "ProvisioningParameters"
    PRODUCT_ID = "ProductId"
    PROVISIONING_ARTIFACT_ID = "ProvisioningArtifactId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "path_id": "PathId",
        "provisioning_parameters": "ProvisioningParameters",
        "product_id": "ProductId",
        "provisioning_artifact_id": "ProvisioningArtifactId",
    }

    path_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    provisioning_parameters: Optional[list[ProvisioningParameter]] = None
    product_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    provisioning_artifact_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TemplateProviderDetail(PropertyType):
    CFN_TEMPLATE_PROVIDER_DETAIL = "CfnTemplateProviderDetail"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cfn_template_provider_detail": "CfnTemplateProviderDetail",
    }

    cfn_template_provider_detail: Optional[CfnTemplateProviderDetail] = None

