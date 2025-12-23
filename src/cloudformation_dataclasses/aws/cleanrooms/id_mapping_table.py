"""PropertyTypes for AWS::CleanRooms::IdMappingTable."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class IdMappingTableInputReferenceConfig(PropertyType):
    INPUT_REFERENCE_ARN = "InputReferenceArn"
    MANAGE_RESOURCE_POLICIES = "ManageResourcePolicies"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input_reference_arn": "InputReferenceArn",
        "manage_resource_policies": "ManageResourcePolicies",
    }

    input_reference_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manage_resource_policies: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class IdMappingTableInputReferenceProperties(PropertyType):
    ID_MAPPING_TABLE_INPUT_SOURCE = "IdMappingTableInputSource"

    _property_mappings: ClassVar[dict[str, str]] = {
        "id_mapping_table_input_source": "IdMappingTableInputSource",
    }

    id_mapping_table_input_source: Optional[list[IdMappingTableInputSource]] = None


@dataclass
class IdMappingTableInputSource(PropertyType):
    TYPE = "Type"
    ID_NAMESPACE_ASSOCIATION_ID = "IdNamespaceAssociationId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "id_namespace_association_id": "IdNamespaceAssociationId",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id_namespace_association_id: Optional[Union[str, Ref, GetAtt, Sub]] = None

