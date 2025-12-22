"""PropertyTypes for AWS::FinSpace::Environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AutoScalingMetric:
    """AutoScalingMetric enum values."""

    CPU_UTILIZATION_PERCENTAGE = "CPU_UTILIZATION_PERCENTAGE"


class ChangeType:
    """ChangeType enum values."""

    PUT = "PUT"
    DELETE = "DELETE"


class ChangesetStatus:
    """ChangesetStatus enum values."""

    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"


class EnvironmentStatus:
    """EnvironmentStatus enum values."""

    CREATE_REQUESTED = "CREATE_REQUESTED"
    CREATING = "CREATING"
    CREATED = "CREATED"
    DELETE_REQUESTED = "DELETE_REQUESTED"
    DELETING = "DELETING"
    DELETED = "DELETED"
    FAILED_CREATION = "FAILED_CREATION"
    RETRY_DELETION = "RETRY_DELETION"
    FAILED_DELETION = "FAILED_DELETION"
    UPDATE_NETWORK_REQUESTED = "UPDATE_NETWORK_REQUESTED"
    UPDATING_NETWORK = "UPDATING_NETWORK"
    FAILED_UPDATING_NETWORK = "FAILED_UPDATING_NETWORK"
    SUSPENDED = "SUSPENDED"


class ErrorDetails:
    """ErrorDetails enum values."""

    THE_INPUTS_TO_THIS_REQUEST_ARE_INVALID_ = "The inputs to this request are invalid."
    SERVICE_LIMITS_HAVE_BEEN_EXCEEDED_ = "Service limits have been exceeded."
    MISSING_REQUIRED_PERMISSION_TO_PERFORM_THIS_REQUEST_ = "Missing required permission to perform this request."
    ONE_OR_MORE_INPUTS_TO_THIS_REQUEST_WERE_NOT_FOUND_ = "One or more inputs to this request were not found."
    THE_SYSTEM_TEMPORARILY_LACKS_SUFFICIENT_RESOURCES_TO_PROCESS_THE_REQUEST_ = "The system temporarily lacks sufficient resources to process the request."
    AN_INTERNAL_ERROR_HAS_OCCURRED_ = "An internal error has occurred."
    CANCELLED = "Cancelled"
    A_USER_RECOVERABLE_ERROR_HAS_OCCURRED = "A user recoverable error has occurred"


class FederationMode:
    """FederationMode enum values."""

    FEDERATED = "FEDERATED"
    LOCAL = "LOCAL"


class IPAddressType:
    """IPAddressType enum values."""

    IP_V4 = "IP_V4"


class KxAzMode:
    """KxAzMode enum values."""

    SINGLE = "SINGLE"
    MULTI = "MULTI"


class KxClusterCodeDeploymentStrategy:
    """KxClusterCodeDeploymentStrategy enum values."""

    NO_RESTART = "NO_RESTART"
    ROLLING = "ROLLING"
    FORCE = "FORCE"


class KxClusterStatus:
    """KxClusterStatus enum values."""

    PENDING = "PENDING"
    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    RUNNING = "RUNNING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    DELETED = "DELETED"
    DELETE_FAILED = "DELETE_FAILED"


class KxClusterType:
    """KxClusterType enum values."""

    HDB = "HDB"
    RDB = "RDB"
    GATEWAY = "GATEWAY"
    GP = "GP"
    TICKERPLANT = "TICKERPLANT"


class KxDataviewStatus:
    """KxDataviewStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    FAILED = "FAILED"
    DELETING = "DELETING"


class KxDeploymentStrategy:
    """KxDeploymentStrategy enum values."""

    NO_RESTART = "NO_RESTART"
    ROLLING = "ROLLING"


class KxNAS1Type:
    """KxNAS1Type enum values."""

    SSD_1000 = "SSD_1000"
    SSD_250 = "SSD_250"
    HDD_12 = "HDD_12"


class KxNodeStatus:
    """KxNodeStatus enum values."""

    RUNNING = "RUNNING"
    PROVISIONING = "PROVISIONING"


class KxSavedownStorageType:
    """KxSavedownStorageType enum values."""

    SDS01 = "SDS01"


class KxScalingGroupStatus:
    """KxScalingGroupStatus enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"
    DELETE_FAILED = "DELETE_FAILED"


class KxVolumeStatus:
    """KxVolumeStatus enum values."""

    CREATING = "CREATING"
    CREATE_FAILED = "CREATE_FAILED"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    UPDATED = "UPDATED"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETING = "DELETING"
    DELETED = "DELETED"
    DELETE_FAILED = "DELETE_FAILED"


class KxVolumeType:
    """KxVolumeType enum values."""

    NAS_1 = "NAS_1"


class RuleAction:
    """RuleAction enum values."""

    ALLOW = "allow"
    DENY = "deny"


class VolumeType:
    """VolumeType enum values."""

    NAS_1 = "NAS_1"


class dnsStatus:
    """dnsStatus enum values."""

    NONE = "NONE"
    UPDATE_REQUESTED = "UPDATE_REQUESTED"
    UPDATING = "UPDATING"
    FAILED_UPDATE = "FAILED_UPDATE"
    SUCCESSFULLY_UPDATED = "SUCCESSFULLY_UPDATED"


class tgwStatus:
    """tgwStatus enum values."""

    NONE = "NONE"
    UPDATE_REQUESTED = "UPDATE_REQUESTED"
    UPDATING = "UPDATING"
    FAILED_UPDATE = "FAILED_UPDATE"
    SUCCESSFULLY_UPDATED = "SUCCESSFULLY_UPDATED"


@dataclass
class AttributeMapItems(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FederationParameters(PropertyType):
    ATTRIBUTE_MAP = "AttributeMap"
    FEDERATION_PROVIDER_NAME = "FederationProviderName"
    SAML_METADATA_URL = "SamlMetadataURL"
    FEDERATION_URN = "FederationURN"
    SAML_METADATA_DOCUMENT = "SamlMetadataDocument"
    APPLICATION_CALL_BACK_URL = "ApplicationCallBackURL"

    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute_map": "AttributeMap",
        "federation_provider_name": "FederationProviderName",
        "saml_metadata_url": "SamlMetadataURL",
        "federation_urn": "FederationURN",
        "saml_metadata_document": "SamlMetadataDocument",
        "application_call_back_url": "ApplicationCallBackURL",
    }

    attribute_map: Optional[list[AttributeMapItems]] = None
    federation_provider_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    saml_metadata_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    federation_urn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    saml_metadata_document: Optional[Union[str, Ref, GetAtt, Sub]] = None
    application_call_back_url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SuperuserParameters(PropertyType):
    FIRST_NAME = "FirstName"
    LAST_NAME = "LastName"
    EMAIL_ADDRESS = "EmailAddress"

    _property_mappings: ClassVar[dict[str, str]] = {
        "first_name": "FirstName",
        "last_name": "LastName",
        "email_address": "EmailAddress",
    }

    first_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    last_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    email_address: Optional[Union[str, Ref, GetAtt, Sub]] = None

