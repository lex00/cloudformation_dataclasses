"""PropertyTypes for AWS::Neptune::DBCluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ApplyMethod:
    """ApplyMethod enum values."""

    IMMEDIATE = "immediate"
    PENDING_REBOOT = "pending-reboot"


class FailoverStatus:
    """FailoverStatus enum values."""

    PENDING = "pending"
    FAILING_OVER = "failing-over"
    CANCELLING = "cancelling"


class SourceType:
    """SourceType enum values."""

    DB_INSTANCE = "db-instance"
    DB_PARAMETER_GROUP = "db-parameter-group"
    DB_SECURITY_GROUP = "db-security-group"
    DB_SNAPSHOT = "db-snapshot"
    DB_CLUSTER = "db-cluster"
    DB_CLUSTER_SNAPSHOT = "db-cluster-snapshot"


@dataclass
class DBClusterRole(PropertyType):
    ROLE_ARN = "RoleArn"
    FEATURE_NAME = "FeatureName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleArn",
        "feature_name": "FeatureName",
    }

    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    feature_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerlessScalingConfiguration(PropertyType):
    MIN_CAPACITY = "MinCapacity"
    MAX_CAPACITY = "MaxCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "min_capacity": "MinCapacity",
        "max_capacity": "MaxCapacity",
    }

    min_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None

