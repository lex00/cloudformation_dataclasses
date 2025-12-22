"""PropertyTypes for AWS::PCS::Queue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccountingMode:
    """AccountingMode enum values."""

    STANDARD = "STANDARD"
    NONE = "NONE"


class ClusterStatus:
    """ClusterStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    SUSPENDING = "SUSPENDING"
    SUSPENDED = "SUSPENDED"


class ComputeNodeGroupStatus:
    """ComputeNodeGroupStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETED = "DELETED"
    SUSPENDING = "SUSPENDING"
    SUSPENDED = "SUSPENDED"


class EndpointType:
    """EndpointType enum values."""

    SLURMCTLD = "SLURMCTLD"
    SLURMDBD = "SLURMDBD"
    SLURMRESTD = "SLURMRESTD"


class NetworkType:
    """NetworkType enum values."""

    IPV4 = "IPV4"
    IPV6 = "IPV6"


class PurchaseOption:
    """PurchaseOption enum values."""

    ONDEMAND = "ONDEMAND"
    SPOT = "SPOT"
    CAPACITY_BLOCK = "CAPACITY_BLOCK"


class QueueStatus:
    """QueueStatus enum values."""

    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    SUSPENDING = "SUSPENDING"
    SUSPENDED = "SUSPENDED"


class SchedulerType:
    """SchedulerType enum values."""

    SLURM = "SLURM"


class Size:
    """Size enum values."""

    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class SlurmRestMode:
    """SlurmRestMode enum values."""

    STANDARD = "STANDARD"
    NONE = "NONE"


class SpotAllocationStrategy:
    """SpotAllocationStrategy enum values."""

    LOWEST_PRICE = "lowest-price"
    CAPACITY_OPTIMIZED = "capacity-optimized"
    PRICE_CAPACITY_OPTIMIZED = "price-capacity-optimized"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


@dataclass
class ComputeNodeGroupConfiguration(PropertyType):
    COMPUTE_NODE_GROUP_ID = "ComputeNodeGroupId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_node_group_id": "ComputeNodeGroupId",
    }

    compute_node_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ErrorInfo(PropertyType):
    MESSAGE = "Message"
    CODE = "Code"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "code": "Code",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlurmConfiguration(PropertyType):
    SLURM_CUSTOM_SETTINGS = "SlurmCustomSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "slurm_custom_settings": "SlurmCustomSettings",
    }

    slurm_custom_settings: Optional[list[SlurmCustomSetting]] = None


@dataclass
class SlurmCustomSetting(PropertyType):
    PARAMETER_VALUE = "ParameterValue"
    PARAMETER_NAME = "ParameterName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value": "ParameterValue",
        "parameter_name": "ParameterName",
    }

    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

