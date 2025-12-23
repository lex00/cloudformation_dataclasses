"""PropertyTypes for AWS::ServiceCatalog::CloudFormationProduct."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CodeStarParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "artifact_path": "ArtifactPath",
        "repository": "Repository",
        "branch": "Branch",
        "connection_arn": "ConnectionArn",
    }

    artifact_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    repository: Optional[Union[str, Ref, GetAtt, Sub]] = None
    branch: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConnectionParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "code_star": "CodeStar",
    }

    code_star: Optional[CodeStarParameters] = None


@dataclass
class ProvisioningArtifactProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "description": "Description",
        "disable_template_validation": "DisableTemplateValidation",
        "info": "Info",
        "name": "Name",
    }

    type_: Optional[Union[str, ProvisioningArtifactType, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    disable_template_validation: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    info: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceConnection(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "connection_parameters": "ConnectionParameters",
    }

    type_: Optional[Union[str, SourceType, Ref, GetAtt, Sub]] = None
    connection_parameters: Optional[ConnectionParameters] = None

