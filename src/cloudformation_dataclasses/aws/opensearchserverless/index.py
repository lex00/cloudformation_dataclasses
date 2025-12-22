"""PropertyTypes for AWS::OpenSearchServerless::Index."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessPolicyType:
    """AccessPolicyType enum values."""

    DATA = "data"


class CollectionStatus:
    """CollectionStatus enum values."""

    CREATING = "CREATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class CollectionType:
    """CollectionType enum values."""

    SEARCH = "SEARCH"
    TIMESERIES = "TIMESERIES"
    VECTORSEARCH = "VECTORSEARCH"


class IamIdentityCenterGroupAttribute:
    """IamIdentityCenterGroupAttribute enum values."""

    GROUPID = "GroupId"
    GROUPNAME = "GroupName"


class IamIdentityCenterUserAttribute:
    """IamIdentityCenterUserAttribute enum values."""

    USERID = "UserId"
    USERNAME = "UserName"
    EMAIL = "Email"


class LifecyclePolicyType:
    """LifecyclePolicyType enum values."""

    RETENTION = "retention"


class ResourceType:
    """ResourceType enum values."""

    INDEX = "index"


class SecurityConfigType:
    """SecurityConfigType enum values."""

    SAML = "saml"
    IAMIDENTITYCENTER = "iamidentitycenter"
    IAMFEDERATION = "iamfederation"


class SecurityPolicyType:
    """SecurityPolicyType enum values."""

    ENCRYPTION = "encryption"
    NETWORK = "network"


class ServerlessVectorAccelerationStatus:
    """ServerlessVectorAccelerationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ALLOWED = "ALLOWED"


class StandbyReplicas:
    """StandbyReplicas enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class VpcEndpointStatus:
    """VpcEndpointStatus enum values."""

    PENDING = "PENDING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


@dataclass
class Index(PropertyType):
    KNN_ALGO_PARAM_EF_SEARCH = "KnnAlgoParamEfSearch"
    REFRESH_INTERVAL = "RefreshInterval"
    KNN = "Knn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "knn_algo_param_ef_search": "KnnAlgoParamEfSearch",
        "refresh_interval": "RefreshInterval",
        "knn": "Knn",
    }

    knn_algo_param_ef_search: Optional[Union[int, Ref, GetAtt, Sub]] = None
    refresh_interval: Optional[Union[str, Ref, GetAtt, Sub]] = None
    knn: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class IndexSettings(PropertyType):
    INDEX = "Index"

    _property_mappings: ClassVar[dict[str, str]] = {
        "index": "Index",
    }

    index: Optional[Index] = None


@dataclass
class Mappings(PropertyType):
    PROPERTIES = "Properties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "properties": "Properties",
    }

    properties: Optional[dict[str, Any]] = None


@dataclass
class Method(PropertyType):
    PARAMETERS = "Parameters"
    SPACE_TYPE = "SpaceType"
    ENGINE = "Engine"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "space_type": "SpaceType",
        "engine": "Engine",
        "name": "Name",
    }

    parameters: Optional[Parameters] = None
    space_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    engine: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Parameters(PropertyType):
    EF_CONSTRUCTION = "EfConstruction"
    M = "M"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ef_construction": "EfConstruction",
        "m": "M",
    }

    ef_construction: Optional[Union[int, Ref, GetAtt, Sub]] = None
    m: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PropertyMapping(PropertyType):
    TYPE = "Type"
    VALUE = "Value"
    INDEX = "Index"
    DIMENSION = "Dimension"
    METHOD = "Method"
    PROPERTIES = "Properties"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "value": "Value",
        "index": "Index",
        "dimension": "Dimension",
        "method": "Method",
        "properties": "Properties",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    index: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    dimension: Optional[Union[int, Ref, GetAtt, Sub]] = None
    method: Optional[Method] = None
    properties: Optional[dict[str, Any]] = None

