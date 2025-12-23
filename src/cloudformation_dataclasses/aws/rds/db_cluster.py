"""PropertyTypes for AWS::RDS::DBCluster."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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
class Endpoint(PropertyType):
    ADDRESS = "Address"
    PORT = "Port"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "port": "Port",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MasterUserSecret(PropertyType):
    SECRET_ARN = "SecretArn"
    KMS_KEY_ID = "KmsKeyId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "secret_arn": "SecretArn",
        "kms_key_id": "KmsKeyId",
    }

    secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReadEndpoint(PropertyType):
    ADDRESS = "Address"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingConfiguration(PropertyType):
    TIMEOUT_ACTION = "TimeoutAction"
    SECONDS_BEFORE_TIMEOUT = "SecondsBeforeTimeout"
    SECONDS_UNTIL_AUTO_PAUSE = "SecondsUntilAutoPause"
    AUTO_PAUSE = "AutoPause"
    MIN_CAPACITY = "MinCapacity"
    MAX_CAPACITY = "MaxCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_action": "TimeoutAction",
        "seconds_before_timeout": "SecondsBeforeTimeout",
        "seconds_until_auto_pause": "SecondsUntilAutoPause",
        "auto_pause": "AutoPause",
        "min_capacity": "MinCapacity",
        "max_capacity": "MaxCapacity",
    }

    timeout_action: Optional[Union[str, Ref, GetAtt, Sub]] = None
    seconds_before_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    seconds_until_auto_pause: Optional[Union[int, Ref, GetAtt, Sub]] = None
    auto_pause: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    min_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None
    max_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class ServerlessV2ScalingConfiguration(PropertyType):
    SECONDS_UNTIL_AUTO_PAUSE = "SecondsUntilAutoPause"
    MIN_CAPACITY = "MinCapacity"
    MAX_CAPACITY = "MaxCapacity"

    _property_mappings: ClassVar[dict[str, str]] = {
        "seconds_until_auto_pause": "SecondsUntilAutoPause",
        "min_capacity": "MinCapacity",
        "max_capacity": "MaxCapacity",
    }

    seconds_until_auto_pause: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None
    max_capacity: Optional[Union[float, Ref, GetAtt, Sub]] = None

