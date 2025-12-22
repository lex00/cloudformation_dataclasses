"""PropertyTypes for AWS::CloudFormation::StackSet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccountFilterType:
    """AccountFilterType enum values."""

    NONE = "NONE"
    INTERSECTION = "INTERSECTION"
    DIFFERENCE = "DIFFERENCE"
    UNION = "UNION"


class AccountGateStatus:
    """AccountGateStatus enum values."""

    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


class AfterValueFrom:
    """AfterValueFrom enum values."""

    TEMPLATE = "TEMPLATE"


class AnnotationSeverityLevel:
    """AnnotationSeverityLevel enum values."""

    INFORMATIONAL = "INFORMATIONAL"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class AnnotationStatus:
    """AnnotationStatus enum values."""

    PASSED = "PASSED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


class AttributeChangeType:
    """AttributeChangeType enum values."""

    ADD = "Add"
    REMOVE = "Remove"
    MODIFY = "Modify"
    SYNCWITHACTUAL = "SyncWithActual"


class BeaconStackOperationStatus:
    """BeaconStackOperationStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class BeforeValueFrom:
    """BeforeValueFrom enum values."""

    PREVIOUS_DEPLOYMENT_STATE = "PREVIOUS_DEPLOYMENT_STATE"
    ACTUAL_STATE = "ACTUAL_STATE"


class CallAs:
    """CallAs enum values."""

    SELF = "SELF"
    DELEGATED_ADMIN = "DELEGATED_ADMIN"


class Capability:
    """Capability enum values."""

    CAPABILITY_IAM = "CAPABILITY_IAM"
    CAPABILITY_NAMED_IAM = "CAPABILITY_NAMED_IAM"
    CAPABILITY_AUTO_EXPAND = "CAPABILITY_AUTO_EXPAND"


class Category:
    """Category enum values."""

    REGISTERED = "REGISTERED"
    ACTIVATED = "ACTIVATED"
    THIRD_PARTY = "THIRD_PARTY"
    AWS_TYPES = "AWS_TYPES"


class ChangeAction:
    """ChangeAction enum values."""

    ADD = "Add"
    MODIFY = "Modify"
    REMOVE = "Remove"
    IMPORT = "Import"
    DYNAMIC = "Dynamic"
    SYNCWITHACTUAL = "SyncWithActual"


class ChangeSetHooksStatus:
    """ChangeSetHooksStatus enum values."""

    PLANNING = "PLANNING"
    PLANNED = "PLANNED"
    UNAVAILABLE = "UNAVAILABLE"


class ChangeSetStatus:
    """ChangeSetStatus enum values."""

    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    DELETE_PENDING = "DELETE_PENDING"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_FAILED = "DELETE_FAILED"
    FAILED = "FAILED"


class ChangeSetType:
    """ChangeSetType enum values."""

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    IMPORT = "IMPORT"


class ChangeSource:
    """ChangeSource enum values."""

    RESOURCEREFERENCE = "ResourceReference"
    PARAMETERREFERENCE = "ParameterReference"
    RESOURCEATTRIBUTE = "ResourceAttribute"
    DIRECTMODIFICATION = "DirectModification"
    AUTOMATIC = "Automatic"
    NOMODIFICATION = "NoModification"


class ChangeType:
    """ChangeType enum values."""

    RESOURCE = "Resource"


class ConcurrencyMode:
    """ConcurrencyMode enum values."""

    STRICT_FAILURE_TOLERANCE = "STRICT_FAILURE_TOLERANCE"
    SOFT_FAILURE_TOLERANCE = "SOFT_FAILURE_TOLERANCE"


class DeletionMode:
    """DeletionMode enum values."""

    STANDARD = "STANDARD"
    FORCE_DELETE_STACK = "FORCE_DELETE_STACK"


class DeploymentMode:
    """DeploymentMode enum values."""

    REVERT_DRIFT = "REVERT_DRIFT"


class DeprecatedStatus:
    """DeprecatedStatus enum values."""

    LIVE = "LIVE"
    DEPRECATED = "DEPRECATED"


class DetailedStatus:
    """DetailedStatus enum values."""

    CONFIGURATION_COMPLETE = "CONFIGURATION_COMPLETE"
    VALIDATION_FAILED = "VALIDATION_FAILED"


class DifferenceType:
    """DifferenceType enum values."""

    ADD = "ADD"
    REMOVE = "REMOVE"
    NOT_EQUAL = "NOT_EQUAL"


class DriftIgnoredReason:
    """DriftIgnoredReason enum values."""

    MANAGED_BY_AWS = "MANAGED_BY_AWS"
    WRITE_ONLY_PROPERTY = "WRITE_ONLY_PROPERTY"


class EvaluationType:
    """EvaluationType enum values."""

    STATIC = "Static"
    DYNAMIC = "Dynamic"


class EventType:
    """EventType enum values."""

    STACK_EVENT = "STACK_EVENT"
    PROGRESS_EVENT = "PROGRESS_EVENT"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    PROVISIONING_ERROR = "PROVISIONING_ERROR"
    HOOK_INVOCATION_ERROR = "HOOK_INVOCATION_ERROR"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    UNAVAILABLE = "UNAVAILABLE"
    AVAILABLE = "AVAILABLE"
    EXECUTE_IN_PROGRESS = "EXECUTE_IN_PROGRESS"
    EXECUTE_COMPLETE = "EXECUTE_COMPLETE"
    EXECUTE_FAILED = "EXECUTE_FAILED"
    OBSOLETE = "OBSOLETE"


class GeneratedTemplateDeletionPolicy:
    """GeneratedTemplateDeletionPolicy enum values."""

    DELETE = "DELETE"
    RETAIN = "RETAIN"


class GeneratedTemplateResourceStatus:
    """GeneratedTemplateResourceStatus enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETE = "COMPLETE"


class GeneratedTemplateStatus:
    """GeneratedTemplateStatus enum values."""

    CREATE_PENDING = "CREATE_PENDING"
    UPDATE_PENDING = "UPDATE_PENDING"
    DELETE_PENDING = "DELETE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETE = "COMPLETE"


class GeneratedTemplateUpdateReplacePolicy:
    """GeneratedTemplateUpdateReplacePolicy enum values."""

    DELETE = "DELETE"
    RETAIN = "RETAIN"


class HandlerErrorCode:
    """HandlerErrorCode enum values."""

    NOTUPDATABLE = "NotUpdatable"
    INVALIDREQUEST = "InvalidRequest"
    ACCESSDENIED = "AccessDenied"
    INVALIDCREDENTIALS = "InvalidCredentials"
    ALREADYEXISTS = "AlreadyExists"
    NOTFOUND = "NotFound"
    RESOURCECONFLICT = "ResourceConflict"
    THROTTLING = "Throttling"
    SERVICELIMITEXCEEDED = "ServiceLimitExceeded"
    NOTSTABILIZED = "NotStabilized"
    GENERALSERVICEEXCEPTION = "GeneralServiceException"
    SERVICEINTERNALERROR = "ServiceInternalError"
    NETWORKFAILURE = "NetworkFailure"
    INTERNALFAILURE = "InternalFailure"
    INVALIDTYPECONFIGURATION = "InvalidTypeConfiguration"
    HANDLERINTERNALFAILURE = "HandlerInternalFailure"
    NONCOMPLIANT = "NonCompliant"
    UNKNOWN = "Unknown"
    UNSUPPORTEDTARGET = "UnsupportedTarget"


class HookFailureMode:
    """HookFailureMode enum values."""

    FAIL = "FAIL"
    WARN = "WARN"


class HookInvocationPoint:
    """HookInvocationPoint enum values."""

    PRE_PROVISION = "PRE_PROVISION"


class HookStatus:
    """HookStatus enum values."""

    HOOK_IN_PROGRESS = "HOOK_IN_PROGRESS"
    HOOK_COMPLETE_SUCCEEDED = "HOOK_COMPLETE_SUCCEEDED"
    HOOK_COMPLETE_FAILED = "HOOK_COMPLETE_FAILED"
    HOOK_FAILED = "HOOK_FAILED"


class HookTargetAction:
    """HookTargetAction enum values."""

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    IMPORT = "IMPORT"


class HookTargetType:
    """HookTargetType enum values."""

    RESOURCE = "RESOURCE"


class IdentityProvider:
    """IdentityProvider enum values."""

    AWS_MARKETPLACE = "AWS_Marketplace"
    GITHUB = "GitHub"
    BITBUCKET = "Bitbucket"


class ListHookResultsTargetType:
    """ListHookResultsTargetType enum values."""

    CHANGE_SET = "CHANGE_SET"
    STACK = "STACK"
    RESOURCE = "RESOURCE"
    CLOUD_CONTROL = "CLOUD_CONTROL"


class OnFailure:
    """OnFailure enum values."""

    DO_NOTHING = "DO_NOTHING"
    ROLLBACK = "ROLLBACK"
    DELETE = "DELETE"


class OnStackFailure:
    """OnStackFailure enum values."""

    DO_NOTHING = "DO_NOTHING"
    ROLLBACK = "ROLLBACK"
    DELETE = "DELETE"


class OperationResultFilterName:
    """OperationResultFilterName enum values."""

    OPERATION_RESULT_STATUS = "OPERATION_RESULT_STATUS"


class OperationStatus:
    """OperationStatus enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class OperationType:
    """OperationType enum values."""

    CREATE_STACK = "CREATE_STACK"
    UPDATE_STACK = "UPDATE_STACK"
    DELETE_STACK = "DELETE_STACK"
    CONTINUE_ROLLBACK = "CONTINUE_ROLLBACK"
    ROLLBACK = "ROLLBACK"
    CREATE_CHANGESET = "CREATE_CHANGESET"


class OrganizationStatus:
    """OrganizationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    DISABLED_PERMANENTLY = "DISABLED_PERMANENTLY"


class PermissionModels:
    """PermissionModels enum values."""

    SERVICE_MANAGED = "SERVICE_MANAGED"
    SELF_MANAGED = "SELF_MANAGED"


class PolicyAction:
    """PolicyAction enum values."""

    DELETE = "Delete"
    RETAIN = "Retain"
    SNAPSHOT = "Snapshot"
    REPLACEANDDELETE = "ReplaceAndDelete"
    REPLACEANDRETAIN = "ReplaceAndRetain"
    REPLACEANDSNAPSHOT = "ReplaceAndSnapshot"


class ProvisioningType:
    """ProvisioningType enum values."""

    NON_PROVISIONABLE = "NON_PROVISIONABLE"
    IMMUTABLE = "IMMUTABLE"
    FULLY_MUTABLE = "FULLY_MUTABLE"


class PublisherStatus:
    """PublisherStatus enum values."""

    VERIFIED = "VERIFIED"
    UNVERIFIED = "UNVERIFIED"


class RegionConcurrencyType:
    """RegionConcurrencyType enum values."""

    SEQUENTIAL = "SEQUENTIAL"
    PARALLEL = "PARALLEL"


class RegistrationStatus:
    """RegistrationStatus enum values."""

    COMPLETE = "COMPLETE"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


class RegistryType:
    """RegistryType enum values."""

    RESOURCE = "RESOURCE"
    MODULE = "MODULE"
    HOOK = "HOOK"


class Replacement:
    """Replacement enum values."""

    TRUE = "True"
    FALSE = "False"
    CONDITIONAL = "Conditional"


class RequiresRecreation:
    """RequiresRecreation enum values."""

    NEVER = "Never"
    CONDITIONALLY = "Conditionally"
    ALWAYS = "Always"


class ResourceAttribute:
    """ResourceAttribute enum values."""

    PROPERTIES = "Properties"
    METADATA = "Metadata"
    CREATIONPOLICY = "CreationPolicy"
    UPDATEPOLICY = "UpdatePolicy"
    DELETIONPOLICY = "DeletionPolicy"
    UPDATEREPLACEPOLICY = "UpdateReplacePolicy"
    TAGS = "Tags"


class ResourceScanStatus:
    """ResourceScanStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    COMPLETE = "COMPLETE"
    EXPIRED = "EXPIRED"


class ResourceSignalStatus:
    """ResourceSignalStatus enum values."""

    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class ResourceStatus:
    """ResourceStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_SKIPPED = "DELETE_SKIPPED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    IMPORT_FAILED = "IMPORT_FAILED"
    IMPORT_COMPLETE = "IMPORT_COMPLETE"
    IMPORT_IN_PROGRESS = "IMPORT_IN_PROGRESS"
    IMPORT_ROLLBACK_IN_PROGRESS = "IMPORT_ROLLBACK_IN_PROGRESS"
    IMPORT_ROLLBACK_FAILED = "IMPORT_ROLLBACK_FAILED"
    IMPORT_ROLLBACK_COMPLETE = "IMPORT_ROLLBACK_COMPLETE"
    EXPORT_FAILED = "EXPORT_FAILED"
    EXPORT_COMPLETE = "EXPORT_COMPLETE"
    EXPORT_IN_PROGRESS = "EXPORT_IN_PROGRESS"
    EXPORT_ROLLBACK_IN_PROGRESS = "EXPORT_ROLLBACK_IN_PROGRESS"
    EXPORT_ROLLBACK_FAILED = "EXPORT_ROLLBACK_FAILED"
    EXPORT_ROLLBACK_COMPLETE = "EXPORT_ROLLBACK_COMPLETE"
    UPDATE_ROLLBACK_IN_PROGRESS = "UPDATE_ROLLBACK_IN_PROGRESS"
    UPDATE_ROLLBACK_COMPLETE = "UPDATE_ROLLBACK_COMPLETE"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"


class ScanType:
    """ScanType enum values."""

    FULL = "FULL"
    PARTIAL = "PARTIAL"


class StackDriftDetectionStatus:
    """StackDriftDetectionStatus enum values."""

    DETECTION_IN_PROGRESS = "DETECTION_IN_PROGRESS"
    DETECTION_FAILED = "DETECTION_FAILED"
    DETECTION_COMPLETE = "DETECTION_COMPLETE"


class StackDriftStatus:
    """StackDriftStatus enum values."""

    DRIFTED = "DRIFTED"
    IN_SYNC = "IN_SYNC"
    UNKNOWN = "UNKNOWN"
    NOT_CHECKED = "NOT_CHECKED"


class StackInstanceDetailedStatus:
    """StackInstanceDetailedStatus enum values."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    INOPERABLE = "INOPERABLE"
    SKIPPED_SUSPENDED_ACCOUNT = "SKIPPED_SUSPENDED_ACCOUNT"
    FAILED_IMPORT = "FAILED_IMPORT"


class StackInstanceFilterName:
    """StackInstanceFilterName enum values."""

    DETAILED_STATUS = "DETAILED_STATUS"
    LAST_OPERATION_ID = "LAST_OPERATION_ID"
    DRIFT_STATUS = "DRIFT_STATUS"


class StackInstanceStatus:
    """StackInstanceStatus enum values."""

    CURRENT = "CURRENT"
    OUTDATED = "OUTDATED"
    INOPERABLE = "INOPERABLE"


class StackRefactorActionEntity:
    """StackRefactorActionEntity enum values."""

    RESOURCE = "RESOURCE"
    STACK = "STACK"


class StackRefactorActionType:
    """StackRefactorActionType enum values."""

    MOVE = "MOVE"
    CREATE = "CREATE"


class StackRefactorDetection:
    """StackRefactorDetection enum values."""

    AUTO = "AUTO"
    MANUAL = "MANUAL"


class StackRefactorExecutionStatus:
    """StackRefactorExecutionStatus enum values."""

    UNAVAILABLE = "UNAVAILABLE"
    AVAILABLE = "AVAILABLE"
    OBSOLETE = "OBSOLETE"
    EXECUTE_IN_PROGRESS = "EXECUTE_IN_PROGRESS"
    EXECUTE_COMPLETE = "EXECUTE_COMPLETE"
    EXECUTE_FAILED = "EXECUTE_FAILED"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"


class StackRefactorStatus:
    """StackRefactorStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_FAILED = "DELETE_FAILED"


class StackResourceDriftStatus:
    """StackResourceDriftStatus enum values."""

    IN_SYNC = "IN_SYNC"
    MODIFIED = "MODIFIED"
    DELETED = "DELETED"
    NOT_CHECKED = "NOT_CHECKED"
    UNKNOWN = "UNKNOWN"
    UNSUPPORTED = "UNSUPPORTED"


class StackSetDriftDetectionStatus:
    """StackSetDriftDetectionStatus enum values."""

    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    IN_PROGRESS = "IN_PROGRESS"
    STOPPED = "STOPPED"


class StackSetDriftStatus:
    """StackSetDriftStatus enum values."""

    DRIFTED = "DRIFTED"
    IN_SYNC = "IN_SYNC"
    NOT_CHECKED = "NOT_CHECKED"


class StackSetOperationAction:
    """StackSetOperationAction enum values."""

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    DETECT_DRIFT = "DETECT_DRIFT"


class StackSetOperationResultStatus:
    """StackSetOperationResultStatus enum values."""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class StackSetOperationStatus:
    """StackSetOperationStatus enum values."""

    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    QUEUED = "QUEUED"


class StackSetStatus:
    """StackSetStatus enum values."""

    ACTIVE = "ACTIVE"
    DELETED = "DELETED"


class StackStatus:
    """StackStatus enum values."""

    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_COMPLETE_CLEANUP_IN_PROGRESS = "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_FAILED = "UPDATE_FAILED"
    UPDATE_ROLLBACK_IN_PROGRESS = "UPDATE_ROLLBACK_IN_PROGRESS"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS = "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS"
    UPDATE_ROLLBACK_COMPLETE = "UPDATE_ROLLBACK_COMPLETE"
    REVIEW_IN_PROGRESS = "REVIEW_IN_PROGRESS"
    IMPORT_IN_PROGRESS = "IMPORT_IN_PROGRESS"
    IMPORT_COMPLETE = "IMPORT_COMPLETE"
    IMPORT_ROLLBACK_IN_PROGRESS = "IMPORT_ROLLBACK_IN_PROGRESS"
    IMPORT_ROLLBACK_FAILED = "IMPORT_ROLLBACK_FAILED"
    IMPORT_ROLLBACK_COMPLETE = "IMPORT_ROLLBACK_COMPLETE"


class TemplateFormat:
    """TemplateFormat enum values."""

    JSON = "JSON"
    YAML = "YAML"


class TemplateStage:
    """TemplateStage enum values."""

    ORIGINAL = "Original"
    PROCESSED = "Processed"


class ThirdPartyType:
    """ThirdPartyType enum values."""

    RESOURCE = "RESOURCE"
    MODULE = "MODULE"
    HOOK = "HOOK"


class TypeTestsStatus:
    """TypeTestsStatus enum values."""

    PASSED = "PASSED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    NOT_TESTED = "NOT_TESTED"


class ValidationStatus:
    """ValidationStatus enum values."""

    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


class VersionBump:
    """VersionBump enum values."""

    MAJOR = "MAJOR"
    MINOR = "MINOR"


class Visibility:
    """Visibility enum values."""

    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


class WarningType:
    """WarningType enum values."""

    MUTUALLY_EXCLUSIVE_PROPERTIES = "MUTUALLY_EXCLUSIVE_PROPERTIES"
    UNSUPPORTED_PROPERTIES = "UNSUPPORTED_PROPERTIES"
    MUTUALLY_EXCLUSIVE_TYPES = "MUTUALLY_EXCLUSIVE_TYPES"
    EXCLUDED_PROPERTIES = "EXCLUDED_PROPERTIES"
    EXCLUDED_RESOURCES = "EXCLUDED_RESOURCES"


@dataclass
class AutoDeployment(PropertyType):
    DEPENDS_ON = "DependsOn"
    ENABLED = "Enabled"
    RETAIN_STACKS_ON_ACCOUNT_REMOVAL = "RetainStacksOnAccountRemoval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "depends_on": "DependsOn",
        "enabled": "Enabled",
        "retain_stacks_on_account_removal": "RetainStacksOnAccountRemoval",
    }

    depends_on: Optional[Union[list[str], Ref]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    retain_stacks_on_account_removal: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DeploymentTargets(PropertyType):
    ACCOUNT_FILTER_TYPE = "AccountFilterType"
    ACCOUNTS = "Accounts"
    ACCOUNTS_URL = "AccountsUrl"
    ORGANIZATIONAL_UNIT_IDS = "OrganizationalUnitIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "account_filter_type": "AccountFilterType",
        "accounts": "Accounts",
        "accounts_url": "AccountsUrl",
        "organizational_unit_ids": "OrganizationalUnitIds",
    }

    account_filter_type: Optional[Union[str, AccountFilterType, Ref, GetAtt, Sub]] = None
    accounts: Optional[Union[list[str], Ref]] = None
    accounts_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    organizational_unit_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class ManagedExecution(PropertyType):
    ACTIVE = "Active"

    _property_mappings: ClassVar[dict[str, str]] = {
        "active": "Active",
    }

    active: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class OperationPreferences(PropertyType):
    MAX_CONCURRENT_PERCENTAGE = "MaxConcurrentPercentage"
    REGION_CONCURRENCY_TYPE = "RegionConcurrencyType"
    MAX_CONCURRENT_COUNT = "MaxConcurrentCount"
    FAILURE_TOLERANCE_PERCENTAGE = "FailureTolerancePercentage"
    CONCURRENCY_MODE = "ConcurrencyMode"
    FAILURE_TOLERANCE_COUNT = "FailureToleranceCount"
    REGION_ORDER = "RegionOrder"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_concurrent_percentage": "MaxConcurrentPercentage",
        "region_concurrency_type": "RegionConcurrencyType",
        "max_concurrent_count": "MaxConcurrentCount",
        "failure_tolerance_percentage": "FailureTolerancePercentage",
        "concurrency_mode": "ConcurrencyMode",
        "failure_tolerance_count": "FailureToleranceCount",
        "region_order": "RegionOrder",
    }

    max_concurrent_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    region_concurrency_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    max_concurrent_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    failure_tolerance_percentage: Optional[Union[int, Ref, GetAtt, Sub]] = None
    concurrency_mode: Optional[Union[str, Ref, GetAtt, Sub]] = None
    failure_tolerance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    region_order: Optional[Union[list[str], Ref]] = None


@dataclass
class Parameter(PropertyType):
    PARAMETER_VALUE = "ParameterValue"
    PARAMETER_KEY = "ParameterKey"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value": "ParameterValue",
        "parameter_key": "ParameterKey",
    }

    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StackInstances(PropertyType):
    PARAMETER_OVERRIDES = "ParameterOverrides"
    DEPLOYMENT_TARGETS = "DeploymentTargets"
    REGIONS = "Regions"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_overrides": "ParameterOverrides",
        "deployment_targets": "DeploymentTargets",
        "regions": "Regions",
    }

    parameter_overrides: Optional[list[Parameter]] = None
    deployment_targets: Optional[DeploymentTargets] = None
    regions: Optional[Union[list[str], Ref]] = None

