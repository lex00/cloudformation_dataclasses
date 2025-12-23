"""PropertyTypes for AWS::Panorama::Package."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class StorageLocation(PropertyType):
    REPO_PREFIX_LOCATION = "RepoPrefixLocation"
    GENERATED_PREFIX_LOCATION = "GeneratedPrefixLocation"
    BINARY_PREFIX_LOCATION = "BinaryPrefixLocation"
    BUCKET = "Bucket"
    MANIFEST_PREFIX_LOCATION = "ManifestPrefixLocation"

    _property_mappings: ClassVar[dict[str, str]] = {
        "repo_prefix_location": "RepoPrefixLocation",
        "generated_prefix_location": "GeneratedPrefixLocation",
        "binary_prefix_location": "BinaryPrefixLocation",
        "bucket": "Bucket",
        "manifest_prefix_location": "ManifestPrefixLocation",
    }

    repo_prefix_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    generated_prefix_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    binary_prefix_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    manifest_prefix_location: Optional[Union[str, Ref, GetAtt, Sub]] = None

