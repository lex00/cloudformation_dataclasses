"""PropertyTypes for AWS::CodePipeline::CustomActionType."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ArtifactDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "minimum_count": "MinimumCount",
        "maximum_count": "MaximumCount",
    }

    minimum_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    maximum_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ConfigurationProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "secret": "Secret",
        "type_": "Type",
        "description": "Description",
        "required": "Required",
        "queryable": "Queryable",
        "key": "Key",
        "name": "Name",
    }

    secret: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    required: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    queryable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    key: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Settings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "entity_url_template": "EntityUrlTemplate",
        "execution_url_template": "ExecutionUrlTemplate",
        "revision_url_template": "RevisionUrlTemplate",
        "third_party_configuration_url": "ThirdPartyConfigurationUrl",
    }

    entity_url_template: Optional[Union[str, Ref, GetAtt, Sub]] = None
    execution_url_template: Optional[Union[str, Ref, GetAtt, Sub]] = None
    revision_url_template: Optional[Union[str, Ref, GetAtt, Sub]] = None
    third_party_configuration_url: Optional[Union[str, Ref, GetAtt, Sub]] = None

