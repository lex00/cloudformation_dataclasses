"""PropertyTypes for AWS::SSM::MaintenanceWindowTask."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccessRequestStatus:
    """AccessRequestStatus enum values."""

    APPROVED = "Approved"
    REJECTED = "Rejected"
    REVOKED = "Revoked"
    EXPIRED = "Expired"
    PENDING = "Pending"


class AccessType:
    """AccessType enum values."""

    STANDARD = "Standard"
    JUSTINTIME = "JustInTime"


class AssociationComplianceSeverity:
    """AssociationComplianceSeverity enum values."""

    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    UNSPECIFIED = "UNSPECIFIED"


class AssociationExecutionFilterKey:
    """AssociationExecutionFilterKey enum values."""

    EXECUTIONID = "ExecutionId"
    STATUS = "Status"
    CREATEDTIME = "CreatedTime"


class AssociationExecutionTargetsFilterKey:
    """AssociationExecutionTargetsFilterKey enum values."""

    STATUS = "Status"
    RESOURCEID = "ResourceId"
    RESOURCETYPE = "ResourceType"


class AssociationFilterKey:
    """AssociationFilterKey enum values."""

    INSTANCEID = "InstanceId"
    NAME = "Name"
    ASSOCIATIONID = "AssociationId"
    ASSOCIATIONSTATUSNAME = "AssociationStatusName"
    LASTEXECUTEDBEFORE = "LastExecutedBefore"
    LASTEXECUTEDAFTER = "LastExecutedAfter"
    ASSOCIATIONNAME = "AssociationName"
    RESOURCEGROUPNAME = "ResourceGroupName"


class AssociationFilterOperatorType:
    """AssociationFilterOperatorType enum values."""

    EQUAL = "EQUAL"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"


class AssociationStatusName:
    """AssociationStatusName enum values."""

    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"


class AssociationSyncCompliance:
    """AssociationSyncCompliance enum values."""

    AUTO = "AUTO"
    MANUAL = "MANUAL"


class AttachmentHashType:
    """AttachmentHashType enum values."""

    SHA256 = "Sha256"


class AttachmentsSourceKey:
    """AttachmentsSourceKey enum values."""

    SOURCEURL = "SourceUrl"
    S3FILEURL = "S3FileUrl"
    ATTACHMENTREFERENCE = "AttachmentReference"


class AutomationExecutionFilterKey:
    """AutomationExecutionFilterKey enum values."""

    DOCUMENTNAMEPREFIX = "DocumentNamePrefix"
    EXECUTIONSTATUS = "ExecutionStatus"
    EXECUTIONID = "ExecutionId"
    PARENTEXECUTIONID = "ParentExecutionId"
    CURRENTACTION = "CurrentAction"
    STARTTIMEBEFORE = "StartTimeBefore"
    STARTTIMEAFTER = "StartTimeAfter"
    AUTOMATIONTYPE = "AutomationType"
    TAGKEY = "TagKey"
    TARGETRESOURCEGROUP = "TargetResourceGroup"
    AUTOMATIONSUBTYPE = "AutomationSubtype"
    OPSITEMID = "OpsItemId"


class AutomationExecutionStatus:
    """AutomationExecutionStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    WAITING = "Waiting"
    SUCCESS = "Success"
    TIMEDOUT = "TimedOut"
    CANCELLING = "Cancelling"
    CANCELLED = "Cancelled"
    FAILED = "Failed"
    PENDINGAPPROVAL = "PendingApproval"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    SCHEDULED = "Scheduled"
    RUNBOOKINPROGRESS = "RunbookInProgress"
    PENDINGCHANGECALENDAROVERRIDE = "PendingChangeCalendarOverride"
    CHANGECALENDAROVERRIDEAPPROVED = "ChangeCalendarOverrideApproved"
    CHANGECALENDAROVERRIDEREJECTED = "ChangeCalendarOverrideRejected"
    COMPLETEDWITHSUCCESS = "CompletedWithSuccess"
    COMPLETEDWITHFAILURE = "CompletedWithFailure"
    EXITED = "Exited"


class AutomationSubtype:
    """AutomationSubtype enum values."""

    CHANGEREQUEST = "ChangeRequest"
    ACCESSREQUEST = "AccessRequest"


class AutomationType:
    """AutomationType enum values."""

    CROSSACCOUNT = "CrossAccount"
    LOCAL = "Local"


class CalendarState:
    """CalendarState enum values."""

    OPEN = "OPEN"
    CLOSED = "CLOSED"


class CommandFilterKey:
    """CommandFilterKey enum values."""

    INVOKEDAFTER = "InvokedAfter"
    INVOKEDBEFORE = "InvokedBefore"
    STATUS = "Status"
    EXECUTIONSTAGE = "ExecutionStage"
    DOCUMENTNAME = "DocumentName"


class CommandInvocationStatus:
    """CommandInvocationStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    DELAYED = "Delayed"
    SUCCESS = "Success"
    CANCELLED = "Cancelled"
    TIMEDOUT = "TimedOut"
    FAILED = "Failed"
    CANCELLING = "Cancelling"


class CommandPluginStatus:
    """CommandPluginStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    SUCCESS = "Success"
    TIMEDOUT = "TimedOut"
    CANCELLED = "Cancelled"
    FAILED = "Failed"


class CommandStatus:
    """CommandStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    SUCCESS = "Success"
    CANCELLED = "Cancelled"
    FAILED = "Failed"
    TIMEDOUT = "TimedOut"
    CANCELLING = "Cancelling"


class ComplianceQueryOperatorType:
    """ComplianceQueryOperatorType enum values."""

    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    BEGIN_WITH = "BEGIN_WITH"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"


class ComplianceSeverity:
    """ComplianceSeverity enum values."""

    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFORMATIONAL = "INFORMATIONAL"
    UNSPECIFIED = "UNSPECIFIED"


class ComplianceStatus:
    """ComplianceStatus enum values."""

    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"


class ComplianceUploadType:
    """ComplianceUploadType enum values."""

    COMPLETE = "COMPLETE"
    PARTIAL = "PARTIAL"


class ConnectionStatus:
    """ConnectionStatus enum values."""

    CONNECTED = "connected"
    NOTCONNECTED = "notconnected"


class DescribeActivationsFilterKeys:
    """DescribeActivationsFilterKeys enum values."""

    ACTIVATIONIDS = "ActivationIds"
    DEFAULTINSTANCENAME = "DefaultInstanceName"
    IAMROLE = "IamRole"


class DocumentFilterKey:
    """DocumentFilterKey enum values."""

    NAME = "Name"
    OWNER = "Owner"
    PLATFORMTYPES = "PlatformTypes"
    DOCUMENTTYPE = "DocumentType"


class DocumentFormat:
    """DocumentFormat enum values."""

    YAML = "YAML"
    JSON = "JSON"
    TEXT = "TEXT"


class DocumentHashType:
    """DocumentHashType enum values."""

    SHA256 = "Sha256"
    SHA1 = "Sha1"


class DocumentMetadataEnum:
    """DocumentMetadataEnum enum values."""

    DOCUMENTREVIEWS = "DocumentReviews"


class DocumentParameterType:
    """DocumentParameterType enum values."""

    STRING = "String"
    STRINGLIST = "StringList"


class DocumentPermissionType:
    """DocumentPermissionType enum values."""

    SHARE = "Share"


class DocumentReviewAction:
    """DocumentReviewAction enum values."""

    SENDFORREVIEW = "SendForReview"
    UPDATEREVIEW = "UpdateReview"
    APPROVE = "Approve"
    REJECT = "Reject"


class DocumentReviewCommentType:
    """DocumentReviewCommentType enum values."""

    COMMENT = "Comment"


class DocumentStatus:
    """DocumentStatus enum values."""

    CREATING = "Creating"
    ACTIVE = "Active"
    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"


class DocumentType:
    """DocumentType enum values."""

    COMMAND = "Command"
    POLICY = "Policy"
    AUTOMATION = "Automation"
    SESSION = "Session"
    PACKAGE = "Package"
    APPLICATIONCONFIGURATION = "ApplicationConfiguration"
    APPLICATIONCONFIGURATIONSCHEMA = "ApplicationConfigurationSchema"
    DEPLOYMENTSTRATEGY = "DeploymentStrategy"
    CHANGECALENDAR = "ChangeCalendar"
    AUTOMATION_CHANGETEMPLATE = "Automation.ChangeTemplate"
    PROBLEMANALYSIS = "ProblemAnalysis"
    PROBLEMANALYSISTEMPLATE = "ProblemAnalysisTemplate"
    CLOUDFORMATION = "CloudFormation"
    CONFORMANCEPACKTEMPLATE = "ConformancePackTemplate"
    QUICKSETUP = "QuickSetup"
    MANUALAPPROVALPOLICY = "ManualApprovalPolicy"
    AUTOAPPROVALPOLICY = "AutoApprovalPolicy"


class ExecutionMode:
    """ExecutionMode enum values."""

    AUTO = "Auto"
    INTERACTIVE = "Interactive"


class ExecutionPreviewStatus:
    """ExecutionPreviewStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    SUCCESS = "Success"
    FAILED = "Failed"


class ExternalAlarmState:
    """ExternalAlarmState enum values."""

    UNKNOWN = "UNKNOWN"
    ALARM = "ALARM"


class Fault:
    """Fault enum values."""

    CLIENT = "Client"
    SERVER = "Server"
    UNKNOWN = "Unknown"


class ImpactType:
    """ImpactType enum values."""

    MUTATING = "Mutating"
    NONMUTATING = "NonMutating"
    UNDETERMINED = "Undetermined"


class InstanceInformationFilterKey:
    """InstanceInformationFilterKey enum values."""

    INSTANCEIDS = "InstanceIds"
    AGENTVERSION = "AgentVersion"
    PINGSTATUS = "PingStatus"
    PLATFORMTYPES = "PlatformTypes"
    ACTIVATIONIDS = "ActivationIds"
    IAMROLE = "IamRole"
    RESOURCETYPE = "ResourceType"
    ASSOCIATIONSTATUS = "AssociationStatus"


class InstancePatchStateOperatorType:
    """InstancePatchStateOperatorType enum values."""

    EQUAL = "Equal"
    NOTEQUAL = "NotEqual"
    LESSTHAN = "LessThan"
    GREATERTHAN = "GreaterThan"


class InstancePropertyFilterKey:
    """InstancePropertyFilterKey enum values."""

    INSTANCEIDS = "InstanceIds"
    AGENTVERSION = "AgentVersion"
    PINGSTATUS = "PingStatus"
    PLATFORMTYPES = "PlatformTypes"
    DOCUMENTNAME = "DocumentName"
    ACTIVATIONIDS = "ActivationIds"
    IAMROLE = "IamRole"
    RESOURCETYPE = "ResourceType"
    ASSOCIATIONSTATUS = "AssociationStatus"


class InstancePropertyFilterOperator:
    """InstancePropertyFilterOperator enum values."""

    EQUAL = "Equal"
    NOTEQUAL = "NotEqual"
    BEGINWITH = "BeginWith"
    LESSTHAN = "LessThan"
    GREATERTHAN = "GreaterThan"


class InventoryAttributeDataType:
    """InventoryAttributeDataType enum values."""

    STRING = "string"
    NUMBER = "number"


class InventoryDeletionStatus:
    """InventoryDeletionStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETE = "Complete"


class InventoryQueryOperatorType:
    """InventoryQueryOperatorType enum values."""

    EQUAL = "Equal"
    NOTEQUAL = "NotEqual"
    BEGINWITH = "BeginWith"
    LESSTHAN = "LessThan"
    GREATERTHAN = "GreaterThan"
    EXISTS = "Exists"


class InventorySchemaDeleteOption:
    """InventorySchemaDeleteOption enum values."""

    DISABLESCHEMA = "DisableSchema"
    DELETESCHEMA = "DeleteSchema"


class LastResourceDataSyncStatus:
    """LastResourceDataSyncStatus enum values."""

    SUCCESSFUL = "Successful"
    FAILED = "Failed"
    INPROGRESS = "InProgress"


class MaintenanceWindowExecutionStatus:
    """MaintenanceWindowExecutionStatus enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    SKIPPED_OVERLAPPING = "SKIPPED_OVERLAPPING"


class MaintenanceWindowResourceType:
    """MaintenanceWindowResourceType enum values."""

    INSTANCE = "INSTANCE"
    RESOURCE_GROUP = "RESOURCE_GROUP"


class MaintenanceWindowTaskCutoffBehavior:
    """MaintenanceWindowTaskCutoffBehavior enum values."""

    CONTINUE_TASK = "CONTINUE_TASK"
    CANCEL_TASK = "CANCEL_TASK"


class MaintenanceWindowTaskType:
    """MaintenanceWindowTaskType enum values."""

    RUN_COMMAND = "RUN_COMMAND"
    AUTOMATION = "AUTOMATION"
    STEP_FUNCTIONS = "STEP_FUNCTIONS"
    LAMBDA = "LAMBDA"


class ManagedStatus:
    """ManagedStatus enum values."""

    ALL = "All"
    MANAGED = "Managed"
    UNMANAGED = "Unmanaged"


class NodeAggregatorType:
    """NodeAggregatorType enum values."""

    COUNT = "Count"


class NodeAttributeName:
    """NodeAttributeName enum values."""

    AGENTVERSION = "AgentVersion"
    PLATFORMNAME = "PlatformName"
    PLATFORMTYPE = "PlatformType"
    PLATFORMVERSION = "PlatformVersion"
    REGION = "Region"
    RESOURCETYPE = "ResourceType"


class NodeFilterKey:
    """NodeFilterKey enum values."""

    AGENTTYPE = "AgentType"
    AGENTVERSION = "AgentVersion"
    COMPUTERNAME = "ComputerName"
    INSTANCEID = "InstanceId"
    INSTANCESTATUS = "InstanceStatus"
    IPADDRESS = "IpAddress"
    MANAGEDSTATUS = "ManagedStatus"
    PLATFORMNAME = "PlatformName"
    PLATFORMTYPE = "PlatformType"
    PLATFORMVERSION = "PlatformVersion"
    RESOURCETYPE = "ResourceType"
    ORGANIZATIONALUNITID = "OrganizationalUnitId"
    ORGANIZATIONALUNITPATH = "OrganizationalUnitPath"
    REGION = "Region"
    ACCOUNTID = "AccountId"


class NodeFilterOperatorType:
    """NodeFilterOperatorType enum values."""

    EQUAL = "Equal"
    NOTEQUAL = "NotEqual"
    BEGINWITH = "BeginWith"


class NodeTypeName:
    """NodeTypeName enum values."""

    INSTANCE = "Instance"


class NotificationEvent:
    """NotificationEvent enum values."""

    ALL = "All"
    INPROGRESS = "InProgress"
    SUCCESS = "Success"
    TIMEDOUT = "TimedOut"
    CANCELLED = "Cancelled"
    FAILED = "Failed"


class NotificationType:
    """NotificationType enum values."""

    COMMAND = "Command"
    INVOCATION = "Invocation"


class OperatingSystem:
    """OperatingSystem enum values."""

    WINDOWS = "WINDOWS"
    AMAZON_LINUX = "AMAZON_LINUX"
    AMAZON_LINUX_2 = "AMAZON_LINUX_2"
    AMAZON_LINUX_2022 = "AMAZON_LINUX_2022"
    UBUNTU = "UBUNTU"
    REDHAT_ENTERPRISE_LINUX = "REDHAT_ENTERPRISE_LINUX"
    SUSE = "SUSE"
    CENTOS = "CENTOS"
    ORACLE_LINUX = "ORACLE_LINUX"
    DEBIAN = "DEBIAN"
    MACOS = "MACOS"
    RASPBIAN = "RASPBIAN"
    ROCKY_LINUX = "ROCKY_LINUX"
    ALMA_LINUX = "ALMA_LINUX"
    AMAZON_LINUX_2023 = "AMAZON_LINUX_2023"


class OpsFilterOperatorType:
    """OpsFilterOperatorType enum values."""

    EQUAL = "Equal"
    NOTEQUAL = "NotEqual"
    BEGINWITH = "BeginWith"
    LESSTHAN = "LessThan"
    GREATERTHAN = "GreaterThan"
    EXISTS = "Exists"


class OpsItemDataType:
    """OpsItemDataType enum values."""

    SEARCHABLESTRING = "SearchableString"
    STRING = "String"


class OpsItemEventFilterKey:
    """OpsItemEventFilterKey enum values."""

    OPSITEMID = "OpsItemId"


class OpsItemEventFilterOperator:
    """OpsItemEventFilterOperator enum values."""

    EQUAL = "Equal"


class OpsItemFilterKey:
    """OpsItemFilterKey enum values."""

    STATUS = "Status"
    CREATEDBY = "CreatedBy"
    SOURCE = "Source"
    PRIORITY = "Priority"
    TITLE = "Title"
    OPSITEMID = "OpsItemId"
    CREATEDTIME = "CreatedTime"
    LASTMODIFIEDTIME = "LastModifiedTime"
    ACTUALSTARTTIME = "ActualStartTime"
    ACTUALENDTIME = "ActualEndTime"
    PLANNEDSTARTTIME = "PlannedStartTime"
    PLANNEDENDTIME = "PlannedEndTime"
    OPERATIONALDATA = "OperationalData"
    OPERATIONALDATAKEY = "OperationalDataKey"
    OPERATIONALDATAVALUE = "OperationalDataValue"
    RESOURCEID = "ResourceId"
    AUTOMATIONID = "AutomationId"
    CATEGORY = "Category"
    SEVERITY = "Severity"
    OPSITEMTYPE = "OpsItemType"
    ACCESSREQUESTBYREQUESTERARN = "AccessRequestByRequesterArn"
    ACCESSREQUESTBYREQUESTERID = "AccessRequestByRequesterId"
    ACCESSREQUESTBYAPPROVERARN = "AccessRequestByApproverArn"
    ACCESSREQUESTBYAPPROVERID = "AccessRequestByApproverId"
    ACCESSREQUESTBYSOURCEACCOUNTID = "AccessRequestBySourceAccountId"
    ACCESSREQUESTBYSOURCEOPSITEMID = "AccessRequestBySourceOpsItemId"
    ACCESSREQUESTBYSOURCEREGION = "AccessRequestBySourceRegion"
    ACCESSREQUESTBYISREPLICA = "AccessRequestByIsReplica"
    ACCESSREQUESTBYTARGETRESOURCEID = "AccessRequestByTargetResourceId"
    CHANGEREQUESTBYREQUESTERARN = "ChangeRequestByRequesterArn"
    CHANGEREQUESTBYREQUESTERNAME = "ChangeRequestByRequesterName"
    CHANGEREQUESTBYAPPROVERARN = "ChangeRequestByApproverArn"
    CHANGEREQUESTBYAPPROVERNAME = "ChangeRequestByApproverName"
    CHANGEREQUESTBYTEMPLATE = "ChangeRequestByTemplate"
    CHANGEREQUESTBYTARGETSRESOURCEGROUP = "ChangeRequestByTargetsResourceGroup"
    INSIGHTBYTYPE = "InsightByType"
    ACCOUNTID = "AccountId"


class OpsItemFilterOperator:
    """OpsItemFilterOperator enum values."""

    EQUAL = "Equal"
    CONTAINS = "Contains"
    GREATERTHAN = "GreaterThan"
    LESSTHAN = "LessThan"


class OpsItemRelatedItemsFilterKey:
    """OpsItemRelatedItemsFilterKey enum values."""

    RESOURCETYPE = "ResourceType"
    ASSOCIATIONID = "AssociationId"
    RESOURCEURI = "ResourceUri"


class OpsItemRelatedItemsFilterOperator:
    """OpsItemRelatedItemsFilterOperator enum values."""

    EQUAL = "Equal"


class OpsItemStatus:
    """OpsItemStatus enum values."""

    OPEN = "Open"
    INPROGRESS = "InProgress"
    RESOLVED = "Resolved"
    PENDING = "Pending"
    TIMEDOUT = "TimedOut"
    CANCELLING = "Cancelling"
    CANCELLED = "Cancelled"
    FAILED = "Failed"
    COMPLETEDWITHSUCCESS = "CompletedWithSuccess"
    COMPLETEDWITHFAILURE = "CompletedWithFailure"
    SCHEDULED = "Scheduled"
    RUNBOOKINPROGRESS = "RunbookInProgress"
    PENDINGCHANGECALENDAROVERRIDE = "PendingChangeCalendarOverride"
    CHANGECALENDAROVERRIDEAPPROVED = "ChangeCalendarOverrideApproved"
    CHANGECALENDAROVERRIDEREJECTED = "ChangeCalendarOverrideRejected"
    PENDINGAPPROVAL = "PendingApproval"
    APPROVED = "Approved"
    REVOKED = "Revoked"
    REJECTED = "Rejected"
    CLOSED = "Closed"


class ParameterTier:
    """ParameterTier enum values."""

    STANDARD = "Standard"
    ADVANCED = "Advanced"
    INTELLIGENT_TIERING = "Intelligent-Tiering"


class ParameterType:
    """ParameterType enum values."""

    STRING = "String"
    STRINGLIST = "StringList"
    SECURESTRING = "SecureString"


class ParametersFilterKey:
    """ParametersFilterKey enum values."""

    NAME = "Name"
    TYPE = "Type"
    KEYID = "KeyId"


class PatchAction:
    """PatchAction enum values."""

    ALLOW_AS_DEPENDENCY = "ALLOW_AS_DEPENDENCY"
    BLOCK = "BLOCK"


class PatchComplianceDataState:
    """PatchComplianceDataState enum values."""

    INSTALLED = "INSTALLED"
    INSTALLED_OTHER = "INSTALLED_OTHER"
    INSTALLED_PENDING_REBOOT = "INSTALLED_PENDING_REBOOT"
    INSTALLED_REJECTED = "INSTALLED_REJECTED"
    MISSING = "MISSING"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    FAILED = "FAILED"
    AVAILABLE_SECURITY_UPDATE = "AVAILABLE_SECURITY_UPDATE"


class PatchComplianceLevel:
    """PatchComplianceLevel enum values."""

    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFORMATIONAL = "INFORMATIONAL"
    UNSPECIFIED = "UNSPECIFIED"


class PatchComplianceStatus:
    """PatchComplianceStatus enum values."""

    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"


class PatchDeploymentStatus:
    """PatchDeploymentStatus enum values."""

    APPROVED = "APPROVED"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    EXPLICIT_APPROVED = "EXPLICIT_APPROVED"
    EXPLICIT_REJECTED = "EXPLICIT_REJECTED"


class PatchFilterKey:
    """PatchFilterKey enum values."""

    ARCH = "ARCH"
    ADVISORY_ID = "ADVISORY_ID"
    BUGZILLA_ID = "BUGZILLA_ID"
    PATCH_SET = "PATCH_SET"
    PRODUCT = "PRODUCT"
    PRODUCT_FAMILY = "PRODUCT_FAMILY"
    CLASSIFICATION = "CLASSIFICATION"
    CVE_ID = "CVE_ID"
    EPOCH = "EPOCH"
    MSRC_SEVERITY = "MSRC_SEVERITY"
    NAME = "NAME"
    PATCH_ID = "PATCH_ID"
    SECTION = "SECTION"
    PRIORITY = "PRIORITY"
    REPOSITORY = "REPOSITORY"
    RELEASE = "RELEASE"
    SEVERITY = "SEVERITY"
    SECURITY = "SECURITY"
    VERSION = "VERSION"


class PatchOperationType:
    """PatchOperationType enum values."""

    SCAN = "Scan"
    INSTALL = "Install"


class PatchProperty:
    """PatchProperty enum values."""

    PRODUCT = "PRODUCT"
    PRODUCT_FAMILY = "PRODUCT_FAMILY"
    CLASSIFICATION = "CLASSIFICATION"
    MSRC_SEVERITY = "MSRC_SEVERITY"
    PRIORITY = "PRIORITY"
    SEVERITY = "SEVERITY"


class PatchSet:
    """PatchSet enum values."""

    OS = "OS"
    APPLICATION = "APPLICATION"


class PingStatus:
    """PingStatus enum values."""

    ONLINE = "Online"
    CONNECTIONLOST = "ConnectionLost"
    INACTIVE = "Inactive"


class PlatformType:
    """PlatformType enum values."""

    WINDOWS = "Windows"
    LINUX = "Linux"
    MACOS = "MacOS"


class RebootOption:
    """RebootOption enum values."""

    REBOOTIFNEEDED = "RebootIfNeeded"
    NOREBOOT = "NoReboot"


class ResourceDataSyncS3Format:
    """ResourceDataSyncS3Format enum values."""

    JSONSERDE = "JsonSerDe"


class ResourceType:
    """ResourceType enum values."""

    MANAGEDINSTANCE = "ManagedInstance"
    EC2INSTANCE = "EC2Instance"


class ResourceTypeForTagging:
    """ResourceTypeForTagging enum values."""

    DOCUMENT = "Document"
    MANAGEDINSTANCE = "ManagedInstance"
    MAINTENANCEWINDOW = "MaintenanceWindow"
    PARAMETER = "Parameter"
    PATCHBASELINE = "PatchBaseline"
    OPSITEM = "OpsItem"
    OPSMETADATA = "OpsMetadata"
    AUTOMATION = "Automation"
    ASSOCIATION = "Association"


class ReviewStatus:
    """ReviewStatus enum values."""

    APPROVED = "APPROVED"
    NOT_REVIEWED = "NOT_REVIEWED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"


class SessionFilterKey:
    """SessionFilterKey enum values."""

    INVOKEDAFTER = "InvokedAfter"
    INVOKEDBEFORE = "InvokedBefore"
    TARGET = "Target"
    OWNER = "Owner"
    STATUS = "Status"
    SESSIONID = "SessionId"
    ACCESSTYPE = "AccessType"


class SessionState:
    """SessionState enum values."""

    ACTIVE = "Active"
    HISTORY = "History"


class SessionStatus:
    """SessionStatus enum values."""

    CONNECTED = "Connected"
    CONNECTING = "Connecting"
    DISCONNECTED = "Disconnected"
    TERMINATED = "Terminated"
    TERMINATING = "Terminating"
    FAILED = "Failed"


class SignalType:
    """SignalType enum values."""

    APPROVE = "Approve"
    REJECT = "Reject"
    STARTSTEP = "StartStep"
    STOPSTEP = "StopStep"
    RESUME = "Resume"
    REVOKE = "Revoke"


class SourceType:
    """SourceType enum values."""

    AWS_EC2_INSTANCE = "AWS::EC2::Instance"
    AWS_IOT_THING = "AWS::IoT::Thing"
    AWS_SSM_MANAGEDINSTANCE = "AWS::SSM::ManagedInstance"


class StepExecutionFilterKey:
    """StepExecutionFilterKey enum values."""

    STARTTIMEBEFORE = "StartTimeBefore"
    STARTTIMEAFTER = "StartTimeAfter"
    STEPEXECUTIONSTATUS = "StepExecutionStatus"
    STEPEXECUTIONID = "StepExecutionId"
    STEPNAME = "StepName"
    ACTION = "Action"
    PARENTSTEPEXECUTIONID = "ParentStepExecutionId"
    PARENTSTEPITERATION = "ParentStepIteration"
    PARENTSTEPITERATORVALUE = "ParentStepIteratorValue"


class StopType:
    """StopType enum values."""

    COMPLETE = "Complete"
    CANCEL = "Cancel"


@dataclass
class CloudWatchOutputConfig(PropertyType):
    CLOUD_WATCH_OUTPUT_ENABLED = "CloudWatchOutputEnabled"
    CLOUD_WATCH_LOG_GROUP_NAME = "CloudWatchLogGroupName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_watch_output_enabled": "CloudWatchOutputEnabled",
        "cloud_watch_log_group_name": "CloudWatchLogGroupName",
    }

    cloud_watch_output_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cloud_watch_log_group_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LoggingInfo(PropertyType):
    S3_BUCKET = "S3Bucket"
    REGION = "Region"
    S3_PREFIX = "S3Prefix"

    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_bucket": "S3Bucket",
        "region": "Region",
        "s3_prefix": "S3Prefix",
    }

    s3_bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    s3_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindowAutomationParameters(PropertyType):
    PARAMETERS = "Parameters"
    DOCUMENT_VERSION = "DocumentVersion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "document_version": "DocumentVersion",
    }

    parameters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    document_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindowLambdaParameters(PropertyType):
    CLIENT_CONTEXT = "ClientContext"
    QUALIFIER = "Qualifier"
    PAYLOAD = "Payload"

    _property_mappings: ClassVar[dict[str, str]] = {
        "client_context": "ClientContext",
        "qualifier": "Qualifier",
        "payload": "Payload",
    }

    client_context: Optional[Union[str, Ref, GetAtt, Sub]] = None
    qualifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    payload: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindowRunCommandParameters(PropertyType):
    TIMEOUT_SECONDS = "TimeoutSeconds"
    COMMENT = "Comment"
    OUTPUT_S3_KEY_PREFIX = "OutputS3KeyPrefix"
    PARAMETERS = "Parameters"
    CLOUD_WATCH_OUTPUT_CONFIG = "CloudWatchOutputConfig"
    DOCUMENT_HASH_TYPE = "DocumentHashType"
    SERVICE_ROLE_ARN = "ServiceRoleArn"
    NOTIFICATION_CONFIG = "NotificationConfig"
    DOCUMENT_VERSION = "DocumentVersion"
    OUTPUT_S3_BUCKET_NAME = "OutputS3BucketName"
    DOCUMENT_HASH = "DocumentHash"

    _property_mappings: ClassVar[dict[str, str]] = {
        "timeout_seconds": "TimeoutSeconds",
        "comment": "Comment",
        "output_s3_key_prefix": "OutputS3KeyPrefix",
        "parameters": "Parameters",
        "cloud_watch_output_config": "CloudWatchOutputConfig",
        "document_hash_type": "DocumentHashType",
        "service_role_arn": "ServiceRoleArn",
        "notification_config": "NotificationConfig",
        "document_version": "DocumentVersion",
        "output_s3_bucket_name": "OutputS3BucketName",
        "document_hash": "DocumentHash",
    }

    timeout_seconds: Optional[Union[int, Ref, GetAtt, Sub]] = None
    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_s3_key_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameters: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    cloud_watch_output_config: Optional[CloudWatchOutputConfig] = None
    document_hash_type: Optional[Union[str, DocumentHashType, Ref, GetAtt, Sub]] = None
    service_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    notification_config: Optional[NotificationConfig] = None
    document_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    output_s3_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    document_hash: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MaintenanceWindowStepFunctionsParameters(PropertyType):
    INPUT = "Input"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "input": "Input",
        "name": "Name",
    }

    input: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationConfig(PropertyType):
    NOTIFICATION_ARN = "NotificationArn"
    NOTIFICATION_TYPE = "NotificationType"
    NOTIFICATION_EVENTS = "NotificationEvents"

    _property_mappings: ClassVar[dict[str, str]] = {
        "notification_arn": "NotificationArn",
        "notification_type": "NotificationType",
        "notification_events": "NotificationEvents",
    }

    notification_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    notification_type: Optional[Union[str, NotificationType, Ref, GetAtt, Sub]] = None
    notification_events: Optional[Union[list[str], Ref]] = None


@dataclass
class Target(PropertyType):
    VALUES = "Values"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "values": "Values",
        "key": "Key",
    }

    values: Optional[Union[list[str], Ref]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TaskInvocationParameters(PropertyType):
    MAINTENANCE_WINDOW_RUN_COMMAND_PARAMETERS = "MaintenanceWindowRunCommandParameters"
    MAINTENANCE_WINDOW_AUTOMATION_PARAMETERS = "MaintenanceWindowAutomationParameters"
    MAINTENANCE_WINDOW_STEP_FUNCTIONS_PARAMETERS = "MaintenanceWindowStepFunctionsParameters"
    MAINTENANCE_WINDOW_LAMBDA_PARAMETERS = "MaintenanceWindowLambdaParameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "maintenance_window_run_command_parameters": "MaintenanceWindowRunCommandParameters",
        "maintenance_window_automation_parameters": "MaintenanceWindowAutomationParameters",
        "maintenance_window_step_functions_parameters": "MaintenanceWindowStepFunctionsParameters",
        "maintenance_window_lambda_parameters": "MaintenanceWindowLambdaParameters",
    }

    maintenance_window_run_command_parameters: Optional[MaintenanceWindowRunCommandParameters] = None
    maintenance_window_automation_parameters: Optional[MaintenanceWindowAutomationParameters] = None
    maintenance_window_step_functions_parameters: Optional[MaintenanceWindowStepFunctionsParameters] = None
    maintenance_window_lambda_parameters: Optional[MaintenanceWindowLambdaParameters] = None

