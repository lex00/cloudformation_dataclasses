"""PropertyTypes for AWS::RDS::DBInstance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CertificateDetails(PropertyType):
    VALID_TILL = "ValidTill"
    CA_IDENTIFIER = "CAIdentifier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "valid_till": "ValidTill",
        "ca_identifier": "CAIdentifier",
    }

    valid_till: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ca_identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DBInstanceRole(PropertyType):
    ROLE_ARN = "RoleArn"
    FEATURE_NAME = "FeatureName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleArn",
        "feature_name": "FeatureName",
    }

    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    feature_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DBInstanceStatusInfo(PropertyType):
    STATUS = "Status"
    MESSAGE = "Message"
    STATUS_TYPE = "StatusType"
    NORMAL = "Normal"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "message": "Message",
        "status_type": "StatusType",
        "normal": "Normal",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    normal: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Endpoint(PropertyType):
    ADDRESS = "Address"
    PORT = "Port"
    HOSTED_ZONE_ID = "HostedZoneId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "address": "Address",
        "port": "Port",
        "hosted_zone_id": "HostedZoneId",
    }

    address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    port: Optional[Union[str, Ref, GetAtt, Sub]] = None
    hosted_zone_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class ProcessorFeature(PropertyType):
    VALUE = "Value"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

