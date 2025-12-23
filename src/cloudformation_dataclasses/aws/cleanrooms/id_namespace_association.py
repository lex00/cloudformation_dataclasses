"""PropertyTypes for AWS::CleanRooms::IdNamespaceAssociation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IdMappingConfig(PropertyType):
    ALLOW_USE_AS_DIMENSION_COLUMN = "AllowUseAsDimensionColumn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_use_as_dimension_column": "AllowUseAsDimensionColumn",
    }

    allow_use_as_dimension_column: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class IdNamespaceAssociationInputReferenceConfig(PropertyType):
    INPUT_REFERENCE_ARN = "InputReferenceArn"
    MANAGE_RESOURCE_POLICIES = "ManageResourcePolicies"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_reference_arn": "InputReferenceArn",
        "manage_resource_policies": "ManageResourcePolicies",
    }

    input_reference_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manage_resource_policies: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class IdNamespaceAssociationInputReferenceProperties(PropertyType):
    ID_NAMESPACE_TYPE = "IdNamespaceType"
    ID_MAPPING_WORKFLOWS_SUPPORTED = "IdMappingWorkflowsSupported"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id_namespace_type": "IdNamespaceType",
        "id_mapping_workflows_supported": "IdMappingWorkflowsSupported",
    }

    id_namespace_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id_mapping_workflows_supported: Optional[Union[list[dict[str, Any]], Ref]] = None

