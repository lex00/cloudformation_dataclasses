"""PropertyTypes for AWS::AuditManager::Assessment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AWSAccount(PropertyType):
    EMAIL_ADDRESS = "EmailAddress"
    ID = "Id"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "email_address": "EmailAddress",
        "id": "Id",
        "name": "Name",
    }

    email_address: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AWSService(PropertyType):
    SERVICE_NAME = "ServiceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "service_name": "ServiceName",
    }

    service_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AssessmentReportsDestination(PropertyType):
    DESTINATION = "Destination"
    DESTINATION_TYPE = "DestinationType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "destination_type": "DestinationType",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Delegation(PropertyType):
    STATUS = "Status"
    COMMENT = "Comment"
    CREATED_BY = "CreatedBy"
    ROLE_TYPE = "RoleType"
    ASSESSMENT_ID = "AssessmentId"
    CREATION_TIME = "CreationTime"
    LAST_UPDATED = "LastUpdated"
    ID = "Id"
    ASSESSMENT_NAME = "AssessmentName"
    ROLE_ARN = "RoleArn"
    CONTROL_SET_ID = "ControlSetId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "comment": "Comment",
        "created_by": "CreatedBy",
        "role_type": "RoleType",
        "assessment_id": "AssessmentId",
        "creation_time": "CreationTime",
        "last_updated": "LastUpdated",
        "id": "Id",
        "assessment_name": "AssessmentName",
        "role_arn": "RoleArn",
        "control_set_id": "ControlSetId",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    created_by: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    assessment_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    creation_time: Optional[Union[float, Ref, GetAtt, Sub]] = None
    last_updated: Optional[Union[float, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    assessment_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    control_set_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Role(PropertyType):
    ROLE_TYPE = "RoleType"
    ROLE_ARN = "RoleArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "role_type": "RoleType",
        "role_arn": "RoleArn",
    }

    role_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Scope(PropertyType):
    AWS_ACCOUNTS = "AwsAccounts"
    AWS_SERVICES = "AwsServices"

    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_accounts": "AwsAccounts",
        "aws_services": "AwsServices",
    }

    aws_accounts: Optional[list[AWSAccount]] = None
    aws_services: Optional[list[AWSService]] = None

