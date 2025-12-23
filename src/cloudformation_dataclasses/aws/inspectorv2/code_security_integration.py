"""PropertyTypes for AWS::InspectorV2::CodeSecurityIntegration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CreateDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "gitlab_self_managed": "gitlabSelfManaged",
    }

    gitlab_self_managed: Optional[CreateGitLabSelfManagedIntegrationDetail] = None


@dataclass
class CreateGitLabSelfManagedIntegrationDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_token": "accessToken",
        "instance_url": "instanceUrl",
    }

    access_token: Optional[Union[str, Ref, GetAtt, Sub]] = None
    instance_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UpdateDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "gitlab_self_managed": "gitlabSelfManaged",
        "github": "github",
    }

    gitlab_self_managed: Optional[UpdateGitLabSelfManagedIntegrationDetail] = None
    github: Optional[UpdateGitHubIntegrationDetail] = None


@dataclass
class UpdateGitHubIntegrationDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "code": "code",
        "installation_id": "installationId",
    }

    code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    installation_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class UpdateGitLabSelfManagedIntegrationDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_code": "authCode",
    }

    auth_code: Optional[Union[str, Ref, GetAtt, Sub]] = None

