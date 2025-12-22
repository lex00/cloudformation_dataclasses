"""PropertyTypes for AWS::DLM::LifecyclePolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class DefaultPoliciesTypeValues:
    """DefaultPoliciesTypeValues enum values."""

    VOLUME = "VOLUME"
    INSTANCE = "INSTANCE"
    ALL = "ALL"


class DefaultPolicyTypeValues:
    """DefaultPolicyTypeValues enum values."""

    VOLUME = "VOLUME"
    INSTANCE = "INSTANCE"


class EventSourceValues:
    """EventSourceValues enum values."""

    MANAGED_CWE = "MANAGED_CWE"


class EventTypeValues:
    """EventTypeValues enum values."""

    SHARESNAPSHOT = "shareSnapshot"


class ExecutionHandlerServiceValues:
    """ExecutionHandlerServiceValues enum values."""

    AWS_SYSTEMS_MANAGER = "AWS_SYSTEMS_MANAGER"


class GettablePolicyStateValues:
    """GettablePolicyStateValues enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    ERROR = "ERROR"


class IntervalUnitValues:
    """IntervalUnitValues enum values."""

    HOURS = "HOURS"


class LocationValues:
    """LocationValues enum values."""

    CLOUD = "CLOUD"
    OUTPOST_LOCAL = "OUTPOST_LOCAL"
    LOCAL_ZONE = "LOCAL_ZONE"


class PolicyLanguageValues:
    """PolicyLanguageValues enum values."""

    SIMPLIFIED = "SIMPLIFIED"
    STANDARD = "STANDARD"


class PolicyTypeValues:
    """PolicyTypeValues enum values."""

    EBS_SNAPSHOT_MANAGEMENT = "EBS_SNAPSHOT_MANAGEMENT"
    IMAGE_MANAGEMENT = "IMAGE_MANAGEMENT"
    EVENT_BASED_POLICY = "EVENT_BASED_POLICY"


class ResourceLocationValues:
    """ResourceLocationValues enum values."""

    CLOUD = "CLOUD"
    OUTPOST = "OUTPOST"
    LOCAL_ZONE = "LOCAL_ZONE"


class ResourceTypeValues:
    """ResourceTypeValues enum values."""

    VOLUME = "VOLUME"
    INSTANCE = "INSTANCE"


class RetentionIntervalUnitValues:
    """RetentionIntervalUnitValues enum values."""

    DAYS = "DAYS"
    WEEKS = "WEEKS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"


class SettablePolicyStateValues:
    """SettablePolicyStateValues enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class StageValues:
    """StageValues enum values."""

    PRE = "PRE"
    POST = "POST"


@dataclass
class Action(PropertyType):
    CROSS_REGION_COPY = "CrossRegionCopy"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cross_region_copy": "CrossRegionCopy",
        "name": "Name",
    }

    cross_region_copy: Optional[list[CrossRegionCopyAction]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ArchiveRetainRule(PropertyType):
    RETENTION_ARCHIVE_TIER = "RetentionArchiveTier"

    _property_mappings: ClassVar[dict[str, str]] = {
        "retention_archive_tier": "RetentionArchiveTier",
    }

    retention_archive_tier: Optional[RetentionArchiveTier] = None


@dataclass
class ArchiveRule(PropertyType):
    RETAIN_RULE = "RetainRule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "retain_rule": "RetainRule",
    }

    retain_rule: Optional[ArchiveRetainRule] = None


@dataclass
class CreateRule(PropertyType):
    INTERVAL_UNIT = "IntervalUnit"
    SCRIPTS = "Scripts"
    TIMES = "Times"
    CRON_EXPRESSION = "CronExpression"
    INTERVAL = "Interval"
    LOCATION = "Location"

    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_unit": "IntervalUnit",
        "scripts": "Scripts",
        "times": "Times",
        "cron_expression": "CronExpression",
        "interval": "Interval",
        "location": "Location",
    }

    interval_unit: Optional[Union[str, IntervalUnitValues, Ref, GetAtt, Sub]] = None
    scripts: Optional[list[Script]] = None
    times: Optional[Union[list[str], Ref]] = None
    cron_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    location: Optional[Union[str, LocationValues, Ref, GetAtt, Sub]] = None


@dataclass
class CrossRegionCopyAction(PropertyType):
    TARGET = "Target"
    ENCRYPTION_CONFIGURATION = "EncryptionConfiguration"
    RETAIN_RULE = "RetainRule"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target": "Target",
        "encryption_configuration": "EncryptionConfiguration",
        "retain_rule": "RetainRule",
    }

    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_configuration: Optional[EncryptionConfiguration] = None
    retain_rule: Optional[CrossRegionCopyRetainRule] = None


@dataclass
class CrossRegionCopyDeprecateRule(PropertyType):
    INTERVAL_UNIT = "IntervalUnit"
    INTERVAL = "Interval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_unit": "IntervalUnit",
        "interval": "Interval",
    }

    interval_unit: Optional[Union[str, RetentionIntervalUnitValues, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CrossRegionCopyRetainRule(PropertyType):
    INTERVAL_UNIT = "IntervalUnit"
    INTERVAL = "Interval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_unit": "IntervalUnit",
        "interval": "Interval",
    }

    interval_unit: Optional[Union[str, RetentionIntervalUnitValues, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class CrossRegionCopyRule(PropertyType):
    TARGET_REGION = "TargetRegion"
    TARGET = "Target"
    DEPRECATE_RULE = "DeprecateRule"
    ENCRYPTED = "Encrypted"
    CMK_ARN = "CmkArn"
    RETAIN_RULE = "RetainRule"
    COPY_TAGS = "CopyTags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_region": "TargetRegion",
        "target": "Target",
        "deprecate_rule": "DeprecateRule",
        "encrypted": "Encrypted",
        "cmk_arn": "CmkArn",
        "retain_rule": "RetainRule",
        "copy_tags": "CopyTags",
    }

    target_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target: Optional[Union[str, Ref, GetAtt, Sub]] = None
    deprecate_rule: Optional[CrossRegionCopyDeprecateRule] = None
    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cmk_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    retain_rule: Optional[CrossRegionCopyRetainRule] = None
    copy_tags: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CrossRegionCopyTarget(PropertyType):
    TARGET_REGION = "TargetRegion"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_region": "TargetRegion",
    }

    target_region: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CrossRegionCopyTargets(PropertyType):
    pass


@dataclass
class DeprecateRule(PropertyType):
    INTERVAL_UNIT = "IntervalUnit"
    COUNT = "Count"
    INTERVAL = "Interval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_unit": "IntervalUnit",
        "count": "Count",
        "interval": "Interval",
    }

    interval_unit: Optional[Union[str, RetentionIntervalUnitValues, Ref, GetAtt, Sub]] = None
    count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    ENCRYPTED = "Encrypted"
    CMK_ARN = "CmkArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "encrypted": "Encrypted",
        "cmk_arn": "CmkArn",
    }

    encrypted: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    cmk_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventParameters(PropertyType):
    EVENT_TYPE = "EventType"
    SNAPSHOT_OWNER = "SnapshotOwner"
    DESCRIPTION_REGEX = "DescriptionRegex"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_type": "EventType",
        "snapshot_owner": "SnapshotOwner",
        "description_regex": "DescriptionRegex",
    }

    event_type: Optional[Union[str, EventTypeValues, Ref, GetAtt, Sub]] = None
    snapshot_owner: Optional[Union[list[str], Ref]] = None
    description_regex: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventSource(PropertyType):
    TYPE = "Type"
    PARAMETERS = "Parameters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "parameters": "Parameters",
    }

    type_: Optional[Union[str, EventSourceValues, Ref, GetAtt, Sub]] = None
    parameters: Optional[EventParameters] = None


@dataclass
class ExcludeTags(PropertyType):
    pass


@dataclass
class ExcludeVolumeTypesList(PropertyType):
    pass


@dataclass
class Exclusions(PropertyType):
    EXCLUDE_BOOT_VOLUMES = "ExcludeBootVolumes"
    EXCLUDE_TAGS = "ExcludeTags"
    EXCLUDE_VOLUME_TYPES = "ExcludeVolumeTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude_boot_volumes": "ExcludeBootVolumes",
        "exclude_tags": "ExcludeTags",
        "exclude_volume_types": "ExcludeVolumeTypes",
    }

    exclude_boot_volumes: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exclude_tags: Optional[ExcludeTags] = None
    exclude_volume_types: Optional[ExcludeVolumeTypesList] = None


@dataclass
class FastRestoreRule(PropertyType):
    INTERVAL_UNIT = "IntervalUnit"
    AVAILABILITY_ZONES = "AvailabilityZones"
    COUNT = "Count"
    INTERVAL = "Interval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_unit": "IntervalUnit",
        "availability_zones": "AvailabilityZones",
        "count": "Count",
        "interval": "Interval",
    }

    interval_unit: Optional[Union[str, RetentionIntervalUnitValues, Ref, GetAtt, Sub]] = None
    availability_zones: Optional[Union[list[str], Ref]] = None
    count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Parameters(PropertyType):
    EXCLUDE_BOOT_VOLUME = "ExcludeBootVolume"
    EXCLUDE_DATA_VOLUME_TAGS = "ExcludeDataVolumeTags"
    NO_REBOOT = "NoReboot"

    _property_mappings: ClassVar[dict[str, str]] = {
        "exclude_boot_volume": "ExcludeBootVolume",
        "exclude_data_volume_tags": "ExcludeDataVolumeTags",
        "no_reboot": "NoReboot",
    }

    exclude_boot_volume: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exclude_data_volume_tags: Optional[list[Tag]] = None
    no_reboot: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyDetails(PropertyType):
    POLICY_LANGUAGE = "PolicyLanguage"
    RESOURCE_TYPES = "ResourceTypes"
    SCHEDULES = "Schedules"
    POLICY_TYPE = "PolicyType"
    CREATE_INTERVAL = "CreateInterval"
    PARAMETERS = "Parameters"
    EXTEND_DELETION = "ExtendDeletion"
    EXCLUSIONS = "Exclusions"
    ACTIONS = "Actions"
    RESOURCE_TYPE = "ResourceType"
    RETAIN_INTERVAL = "RetainInterval"
    EVENT_SOURCE = "EventSource"
    CROSS_REGION_COPY_TARGETS = "CrossRegionCopyTargets"
    TARGET_TAGS = "TargetTags"
    RESOURCE_LOCATIONS = "ResourceLocations"
    COPY_TAGS = "CopyTags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "policy_language": "PolicyLanguage",
        "resource_types": "ResourceTypes",
        "schedules": "Schedules",
        "policy_type": "PolicyType",
        "create_interval": "CreateInterval",
        "parameters": "Parameters",
        "extend_deletion": "ExtendDeletion",
        "exclusions": "Exclusions",
        "actions": "Actions",
        "resource_type": "ResourceType",
        "retain_interval": "RetainInterval",
        "event_source": "EventSource",
        "cross_region_copy_targets": "CrossRegionCopyTargets",
        "target_tags": "TargetTags",
        "resource_locations": "ResourceLocations",
        "copy_tags": "CopyTags",
    }

    policy_language: Optional[Union[str, PolicyLanguageValues, Ref, GetAtt, Sub]] = None
    resource_types: Optional[Union[list[str], Ref]] = None
    schedules: Optional[list[Schedule]] = None
    policy_type: Optional[Union[str, PolicyTypeValues, Ref, GetAtt, Sub]] = None
    create_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    parameters: Optional[Parameters] = None
    extend_deletion: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exclusions: Optional[Exclusions] = None
    actions: Optional[list[Action]] = None
    resource_type: Optional[Union[str, ResourceTypeValues, Ref, GetAtt, Sub]] = None
    retain_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None
    event_source: Optional[EventSource] = None
    cross_region_copy_targets: Optional[CrossRegionCopyTargets] = None
    target_tags: Optional[list[Tag]] = None
    resource_locations: Optional[Union[list[str], Ref]] = None
    copy_tags: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class RetainRule(PropertyType):
    INTERVAL_UNIT = "IntervalUnit"
    COUNT = "Count"
    INTERVAL = "Interval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_unit": "IntervalUnit",
        "count": "Count",
        "interval": "Interval",
    }

    interval_unit: Optional[Union[str, RetentionIntervalUnitValues, Ref, GetAtt, Sub]] = None
    count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RetentionArchiveTier(PropertyType):
    INTERVAL_UNIT = "IntervalUnit"
    COUNT = "Count"
    INTERVAL = "Interval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "interval_unit": "IntervalUnit",
        "count": "Count",
        "interval": "Interval",
    }

    interval_unit: Optional[Union[str, RetentionIntervalUnitValues, Ref, GetAtt, Sub]] = None
    count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class Schedule(PropertyType):
    SHARE_RULES = "ShareRules"
    DEPRECATE_RULE = "DeprecateRule"
    TAGS_TO_ADD = "TagsToAdd"
    CREATE_RULE = "CreateRule"
    VARIABLE_TAGS = "VariableTags"
    FAST_RESTORE_RULE = "FastRestoreRule"
    ARCHIVE_RULE = "ArchiveRule"
    RETAIN_RULE = "RetainRule"
    CROSS_REGION_COPY_RULES = "CrossRegionCopyRules"
    NAME = "Name"
    COPY_TAGS = "CopyTags"

    _property_mappings: ClassVar[dict[str, str]] = {
        "share_rules": "ShareRules",
        "deprecate_rule": "DeprecateRule",
        "tags_to_add": "TagsToAdd",
        "create_rule": "CreateRule",
        "variable_tags": "VariableTags",
        "fast_restore_rule": "FastRestoreRule",
        "archive_rule": "ArchiveRule",
        "retain_rule": "RetainRule",
        "cross_region_copy_rules": "CrossRegionCopyRules",
        "name": "Name",
        "copy_tags": "CopyTags",
    }

    share_rules: Optional[list[ShareRule]] = None
    deprecate_rule: Optional[DeprecateRule] = None
    tags_to_add: Optional[list[Tag]] = None
    create_rule: Optional[CreateRule] = None
    variable_tags: Optional[list[Tag]] = None
    fast_restore_rule: Optional[FastRestoreRule] = None
    archive_rule: Optional[ArchiveRule] = None
    retain_rule: Optional[RetainRule] = None
    cross_region_copy_rules: Optional[list[CrossRegionCopyRule]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    copy_tags: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Script(PropertyType):
    EXECUTION_HANDLER_SERVICE = "ExecutionHandlerService"
    EXECUTION_TIMEOUT = "ExecutionTimeout"
    STAGES = "Stages"
    EXECUTION_HANDLER = "ExecutionHandler"
    MAXIMUM_RETRY_COUNT = "MaximumRetryCount"
    EXECUTE_OPERATION_ON_SCRIPT_FAILURE = "ExecuteOperationOnScriptFailure"

    _property_mappings: ClassVar[dict[str, str]] = {
        "execution_handler_service": "ExecutionHandlerService",
        "execution_timeout": "ExecutionTimeout",
        "stages": "Stages",
        "execution_handler": "ExecutionHandler",
        "maximum_retry_count": "MaximumRetryCount",
        "execute_operation_on_script_failure": "ExecuteOperationOnScriptFailure",
    }

    execution_handler_service: Optional[Union[str, ExecutionHandlerServiceValues, Ref, GetAtt, Sub]] = None
    execution_timeout: Optional[Union[int, Ref, GetAtt, Sub]] = None
    stages: Optional[Union[list[str], Ref]] = None
    execution_handler: Optional[Union[str, Ref, GetAtt, Sub]] = None
    maximum_retry_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    execute_operation_on_script_failure: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class ShareRule(PropertyType):
    TARGET_ACCOUNTS = "TargetAccounts"
    UNSHARE_INTERVAL_UNIT = "UnshareIntervalUnit"
    UNSHARE_INTERVAL = "UnshareInterval"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_accounts": "TargetAccounts",
        "unshare_interval_unit": "UnshareIntervalUnit",
        "unshare_interval": "UnshareInterval",
    }

    target_accounts: Optional[Union[list[str], Ref]] = None
    unshare_interval_unit: Optional[Union[str, RetentionIntervalUnitValues, Ref, GetAtt, Sub]] = None
    unshare_interval: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VolumeTypeValues(PropertyType):
    pass

