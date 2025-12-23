"""PropertyTypes for AWS::Omics::WorkflowVersion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ContainerRegistryMap(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "registry_mappings": "RegistryMappings",
        "image_mappings": "ImageMappings",
    }

    registry_mappings: Optional[list[RegistryMapping]] = None
    image_mappings: Optional[list[ImageMapping]] = None


@dataclass
class DefinitionRepository(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_reference": "sourceReference",
        "full_repository_id": "fullRepositoryId",
        "exclude_file_patterns": "excludeFilePatterns",
        "connection_arn": "connectionArn",
    }

    source_reference: Optional[SourceReference] = None
    full_repository_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclude_file_patterns: Optional[Union[list[str], Ref]] = None
    connection_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ImageMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_image": "SourceImage",
        "destination_image": "DestinationImage",
    }

    source_image: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_image: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RegistryMapping(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "upstream_registry_url": "UpstreamRegistryUrl",
        "ecr_account_id": "EcrAccountId",
        "upstream_repository_prefix": "UpstreamRepositoryPrefix",
        "ecr_repository_prefix": "EcrRepositoryPrefix",
    }

    upstream_registry_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ecr_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    upstream_repository_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ecr_repository_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceReference(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "type",
        "value": "value",
    }

    type_: Optional[Union[str, SourceReferenceType, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class WorkflowParameter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "optional": "Optional",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    optional: Optional[Union[bool, Ref, GetAtt, Sub]] = None

