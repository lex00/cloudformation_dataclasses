"""PropertyTypes for AWS::AuditManager::Assessment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccountStatus:
    """AccountStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    PENDING_ACTIVATION = "PENDING_ACTIVATION"


class ActionEnum:
    """ActionEnum enum values."""

    CREATE = "CREATE"
    UPDATE_METADATA = "UPDATE_METADATA"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETE = "DELETE"
    UNDER_REVIEW = "UNDER_REVIEW"
    REVIEWED = "REVIEWED"
    IMPORT_EVIDENCE = "IMPORT_EVIDENCE"


class AssessmentReportDestinationType:
    """AssessmentReportDestinationType enum values."""

    S3 = "S3"


class AssessmentReportStatus:
    """AssessmentReportStatus enum values."""

    COMPLETE = "COMPLETE"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


class AssessmentStatus:
    """AssessmentStatus enum values."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class ControlResponse:
    """ControlResponse enum values."""

    MANUAL = "MANUAL"
    AUTOMATE = "AUTOMATE"
    DEFER = "DEFER"
    IGNORE = "IGNORE"


class ControlSetStatus:
    """ControlSetStatus enum values."""

    ACTIVE = "ACTIVE"
    UNDER_REVIEW = "UNDER_REVIEW"
    REVIEWED = "REVIEWED"


class ControlState:
    """ControlState enum values."""

    ACTIVE = "ACTIVE"
    END_OF_SUPPORT = "END_OF_SUPPORT"


class ControlStatus:
    """ControlStatus enum values."""

    UNDER_REVIEW = "UNDER_REVIEW"
    REVIEWED = "REVIEWED"
    INACTIVE = "INACTIVE"


class ControlType:
    """ControlType enum values."""

    STANDARD = "Standard"
    CUSTOM = "Custom"
    CORE = "Core"


class DataSourceType:
    """DataSourceType enum values."""

    AWS_CLOUDTRAIL = "AWS_Cloudtrail"
    AWS_CONFIG = "AWS_Config"
    AWS_SECURITY_HUB = "AWS_Security_Hub"
    AWS_API_CALL = "AWS_API_Call"
    MANUAL = "MANUAL"


class DelegationStatus:
    """DelegationStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    UNDER_REVIEW = "UNDER_REVIEW"
    COMPLETE = "COMPLETE"


class DeleteResources:
    """DeleteResources enum values."""

    ALL = "ALL"
    DEFAULT = "DEFAULT"


class EvidenceFinderBackfillStatus:
    """EvidenceFinderBackfillStatus enum values."""

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class EvidenceFinderEnablementStatus:
    """EvidenceFinderEnablementStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ENABLE_IN_PROGRESS = "ENABLE_IN_PROGRESS"
    DISABLE_IN_PROGRESS = "DISABLE_IN_PROGRESS"


class ExportDestinationType:
    """ExportDestinationType enum values."""

    S3 = "S3"


class FrameworkType:
    """FrameworkType enum values."""

    STANDARD = "Standard"
    CUSTOM = "Custom"


class KeywordInputType:
    """KeywordInputType enum values."""

    SELECT_FROM_LIST = "SELECT_FROM_LIST"
    UPLOAD_FILE = "UPLOAD_FILE"
    INPUT_TEXT = "INPUT_TEXT"


class ObjectTypeEnum:
    """ObjectTypeEnum enum values."""

    ASSESSMENT = "ASSESSMENT"
    CONTROL_SET = "CONTROL_SET"
    CONTROL = "CONTROL"
    DELEGATION = "DELEGATION"
    ASSESSMENT_REPORT = "ASSESSMENT_REPORT"


class RoleType:
    """RoleType enum values."""

    PROCESS_OWNER = "PROCESS_OWNER"
    RESOURCE_OWNER = "RESOURCE_OWNER"


class SettingAttribute:
    """SettingAttribute enum values."""

    ALL = "ALL"
    IS_AWS_ORG_ENABLED = "IS_AWS_ORG_ENABLED"
    SNS_TOPIC = "SNS_TOPIC"
    DEFAULT_ASSESSMENT_REPORTS_DESTINATION = "DEFAULT_ASSESSMENT_REPORTS_DESTINATION"
    DEFAULT_PROCESS_OWNERS = "DEFAULT_PROCESS_OWNERS"
    EVIDENCE_FINDER_ENABLEMENT = "EVIDENCE_FINDER_ENABLEMENT"
    DEREGISTRATION_POLICY = "DEREGISTRATION_POLICY"
    DEFAULT_EXPORT_DESTINATION = "DEFAULT_EXPORT_DESTINATION"


class ShareRequestAction:
    """ShareRequestAction enum values."""

    ACCEPT = "ACCEPT"
    DECLINE = "DECLINE"
    REVOKE = "REVOKE"


class ShareRequestStatus:
    """ShareRequestStatus enum values."""

    ACTIVE = "ACTIVE"
    REPLICATING = "REPLICATING"
    SHARED = "SHARED"
    EXPIRING = "EXPIRING"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"
    DECLINED = "DECLINED"
    REVOKED = "REVOKED"


class ShareRequestType:
    """ShareRequestType enum values."""

    SENT = "SENT"
    RECEIVED = "RECEIVED"


class SourceFrequency:
    """SourceFrequency enum values."""

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class SourceSetUpOption:
    """SourceSetUpOption enum values."""

    SYSTEM_CONTROLS_MAPPING = "System_Controls_Mapping"
    PROCEDURAL_CONTROLS_MAPPING = "Procedural_Controls_Mapping"


class SourceType:
    """SourceType enum values."""

    AWS_CLOUDTRAIL = "AWS_Cloudtrail"
    AWS_CONFIG = "AWS_Config"
    AWS_SECURITY_HUB = "AWS_Security_Hub"
    AWS_API_CALL = "AWS_API_Call"
    MANUAL = "MANUAL"
    COMMON_CONTROL = "Common_Control"
    CORE_CONTROL = "Core_Control"


class ValidationExceptionReason:
    """ValidationExceptionReason enum values."""

    UNKNOWNOPERATION = "unknownOperation"
    CANNOTPARSE = "cannotParse"
    FIELDVALIDATIONFAILED = "fieldValidationFailed"
    OTHER = "other"


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

