"""PropertyTypes for AWS::Lambda::CodeSigningConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AllowedPublishers(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "signing_profile_version_arns": "SigningProfileVersionArns",
    }

    signing_profile_version_arns: Optional[Union[list[str], Ref]] = None


@dataclass
class CodeSigningPolicies(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "untrusted_artifact_on_deployment": "UntrustedArtifactOnDeployment",
    }

    untrusted_artifact_on_deployment: Optional[Union[str, CodeSigningPolicy, Ref, GetAtt, Sub]] = None

