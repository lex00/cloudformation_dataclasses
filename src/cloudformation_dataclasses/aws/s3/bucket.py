"""PropertyTypes for AWS::S3::Bucket."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AbortIncompleteMultipartUpload(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "days_after_initiation": "DaysAfterInitiation",
    }

    days_after_initiation: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AccelerateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "acceleration_status": "AccelerationStatus",
    }

    acceleration_status: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AccessControlTranslation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "owner": "Owner",
    }

    owner: Optional[Union[str, OwnerOverride, Ref, GetAtt, Sub]] = None


@dataclass
class AnalyticsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_class_analysis": "StorageClassAnalysis",
        "tag_filters": "TagFilters",
        "id": "Id",
        "prefix": "Prefix",
    }

    storage_class_analysis: Optional[StorageClassAnalysis] = None
    tag_filters: Optional[list[TagFilter]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class BlockedEncryptionTypes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "encryption_type": "EncryptionType",
    }

    encryption_type: Optional[Union[list[str], Ref]] = None


@dataclass
class BucketEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "server_side_encryption_configuration": "ServerSideEncryptionConfiguration",
    }

    server_side_encryption_configuration: Optional[list[ServerSideEncryptionRule]] = None


@dataclass
class CorsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cors_rules": "CorsRules",
    }

    cors_rules: Optional[list[CorsRule]] = None


@dataclass
class CorsRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "exposed_headers": "ExposedHeaders",
        "allowed_methods": "AllowedMethods",
        "allowed_origins": "AllowedOrigins",
        "allowed_headers": "AllowedHeaders",
        "max_age": "MaxAge",
        "id": "Id",
    }

    exposed_headers: Optional[Union[list[str], Ref]] = None
    allowed_methods: Optional[Union[list[str], Ref]] = None
    allowed_origins: Optional[Union[list[str], Ref]] = None
    allowed_headers: Optional[Union[list[str], Ref]] = None
    max_age: Optional[Union[int, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DataExport(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "output_schema_version": "OutputSchemaVersion",
    }

    destination: Optional[Destination] = None
    output_schema_version: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultRetention(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "years": "Years",
        "days": "Days",
        "mode": "Mode",
    }

    years: Optional[Union[int, Ref, GetAtt, Sub]] = None
    days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    mode: Optional[Union[str, ObjectLockRetentionMode, Ref, GetAtt, Sub]] = None


@dataclass
class DeleteMarkerReplication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, DeleteMarkerReplicationStatus, Ref, GetAtt, Sub]] = None


@dataclass
class Destination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketArn",
        "format": "Format",
        "bucket_account_id": "BucketAccountId",
        "prefix": "Prefix",
    }

    bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    bucket_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "replica_kms_key_id": "ReplicaKmsKeyID",
    }

    replica_kms_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class EventBridgeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "event_bridge_enabled": "EventBridgeEnabled",
    }

    event_bridge_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class FilterRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, FilterRuleName, Ref, GetAtt, Sub]] = None


@dataclass
class IntelligentTieringConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "tierings": "Tierings",
        "tag_filters": "TagFilters",
        "id": "Id",
        "prefix": "Prefix",
    }

    status: Optional[Union[str, IntelligentTieringStatus, Ref, GetAtt, Sub]] = None
    tierings: Optional[list[Tiering]] = None
    tag_filters: Optional[list[TagFilter]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InventoryConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "optional_fields": "OptionalFields",
        "included_object_versions": "IncludedObjectVersions",
        "enabled": "Enabled",
        "id": "Id",
        "prefix": "Prefix",
        "schedule_frequency": "ScheduleFrequency",
    }

    destination: Optional[Destination] = None
    optional_fields: Optional[Union[list[str], Ref]] = None
    included_object_versions: Optional[Union[str, InventoryIncludedObjectVersions, Ref, GetAtt, Sub]] = None
    enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    schedule_frequency: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InventoryTableConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "configuration_state": "ConfigurationState",
        "table_arn": "TableArn",
        "encryption_configuration": "EncryptionConfiguration",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    configuration_state: Optional[Union[str, InventoryConfigurationState, Ref, GetAtt, Sub]] = None
    table_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_configuration: Optional[MetadataTableEncryptionConfiguration] = None


@dataclass
class JournalTableConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_name": "TableName",
        "table_arn": "TableArn",
        "encryption_configuration": "EncryptionConfiguration",
        "record_expiration": "RecordExpiration",
    }

    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_configuration: Optional[MetadataTableEncryptionConfiguration] = None
    record_expiration: Optional[RecordExpiration] = None


@dataclass
class LambdaConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function": "Function",
        "filter": "Filter",
        "event": "Event",
    }

    function: Optional[Union[str, Ref, GetAtt, Sub]] = None
    filter: Optional[NotificationFilter] = None
    event: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class LifecycleConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transition_default_minimum_object_size": "TransitionDefaultMinimumObjectSize",
        "rules": "Rules",
    }

    transition_default_minimum_object_size: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rules: Optional[list[Rule]] = None


@dataclass
class LoggingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_object_key_format": "TargetObjectKeyFormat",
        "log_file_prefix": "LogFilePrefix",
        "destination_bucket_name": "DestinationBucketName",
    }

    target_object_key_format: Optional[TargetObjectKeyFormat] = None
    log_file_prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    destination_bucket_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
        "journal_table_configuration": "JournalTableConfiguration",
        "inventory_table_configuration": "InventoryTableConfiguration",
    }

    destination: Optional[MetadataDestination] = None
    journal_table_configuration: Optional[JournalTableConfiguration] = None
    inventory_table_configuration: Optional[InventoryTableConfiguration] = None


@dataclass
class MetadataDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_bucket_arn": "TableBucketArn",
        "table_bucket_type": "TableBucketType",
        "table_namespace": "TableNamespace",
    }

    table_bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_bucket_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MetadataTableConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_tables_destination": "S3TablesDestination",
    }

    s3_tables_destination: Optional[S3TablesDestination] = None


@dataclass
class MetadataTableEncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KmsKeyArn",
        "sse_algorithm": "SseAlgorithm",
    }

    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sse_algorithm: Optional[Union[str, TableSseAlgorithm, Ref, GetAtt, Sub]] = None


@dataclass
class Metrics(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "event_threshold": "EventThreshold",
    }

    status: Optional[Union[str, MetricsStatus, Ref, GetAtt, Sub]] = None
    event_threshold: Optional[ReplicationTimeValue] = None


@dataclass
class MetricsConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_point_arn": "AccessPointArn",
        "tag_filters": "TagFilters",
        "id": "Id",
        "prefix": "Prefix",
    }

    access_point_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_filters: Optional[list[TagFilter]] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NoncurrentVersionExpiration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "noncurrent_days": "NoncurrentDays",
        "newer_noncurrent_versions": "NewerNoncurrentVersions",
    }

    noncurrent_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    newer_noncurrent_versions: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NoncurrentVersionTransition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "storage_class": "StorageClass",
        "transition_in_days": "TransitionInDays",
        "newer_noncurrent_versions": "NewerNoncurrentVersions",
    }

    storage_class: Optional[Union[str, TransitionStorageClass, Ref, GetAtt, Sub]] = None
    transition_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    newer_noncurrent_versions: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class NotificationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_configurations": "TopicConfigurations",
        "queue_configurations": "QueueConfigurations",
        "lambda_configurations": "LambdaConfigurations",
        "event_bridge_configuration": "EventBridgeConfiguration",
    }

    topic_configurations: Optional[list[TopicConfiguration]] = None
    queue_configurations: Optional[list[QueueConfiguration]] = None
    lambda_configurations: Optional[list[LambdaConfiguration]] = None
    event_bridge_configuration: Optional[EventBridgeConfiguration] = None


@dataclass
class NotificationFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "s3_key": "S3Key",
    }

    s3_key: Optional[S3KeyFilter] = None


@dataclass
class ObjectLockConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "object_lock_enabled": "ObjectLockEnabled",
        "rule": "Rule",
    }

    object_lock_enabled: Optional[Union[str, ObjectLockEnabled, Ref, GetAtt, Sub]] = None
    rule: Optional[ObjectLockRule] = None


@dataclass
class ObjectLockRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_retention": "DefaultRetention",
    }

    default_retention: Optional[DefaultRetention] = None


@dataclass
class OwnershipControls(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
    }

    rules: Optional[list[OwnershipControlsRule]] = None


@dataclass
class OwnershipControlsRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "object_ownership": "ObjectOwnership",
    }

    object_ownership: Optional[Union[str, ObjectOwnership, Ref, GetAtt, Sub]] = None


@dataclass
class PartitionedPrefix(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "partition_date_source": "PartitionDateSource",
    }

    partition_date_source: Optional[Union[str, PartitionDateSource, Ref, GetAtt, Sub]] = None


@dataclass
class PublicAccessBlockConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "restrict_public_buckets": "RestrictPublicBuckets",
        "block_public_policy": "BlockPublicPolicy",
        "block_public_acls": "BlockPublicAcls",
        "ignore_public_acls": "IgnorePublicAcls",
    }

    restrict_public_buckets: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    block_public_policy: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    block_public_acls: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    ignore_public_acls: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class QueueConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "event": "Event",
        "queue": "Queue",
    }

    filter: Optional[NotificationFilter] = None
    event: Optional[Union[str, Ref, GetAtt, Sub]] = None
    queue: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RecordExpiration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "days": "Days",
        "expiration": "Expiration",
    }

    days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    expiration: Optional[Union[str, ExpirationState, Ref, GetAtt, Sub]] = None


@dataclass
class RedirectAllRequestsTo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "protocol": "Protocol",
        "host_name": "HostName",
    }

    protocol: Optional[Union[str, Protocol, Ref, GetAtt, Sub]] = None
    host_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RedirectRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "replace_key_with": "ReplaceKeyWith",
        "http_redirect_code": "HttpRedirectCode",
        "protocol": "Protocol",
        "host_name": "HostName",
        "replace_key_prefix_with": "ReplaceKeyPrefixWith",
    }

    replace_key_with: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_redirect_code: Optional[Union[str, Ref, GetAtt, Sub]] = None
    protocol: Optional[Union[str, Ref, GetAtt, Sub]] = None
    host_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replace_key_prefix_with: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicaModifications(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, ReplicaModificationsStatus, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role": "Role",
        "rules": "Rules",
    }

    role: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rules: Optional[list[ReplicationRule]] = None


@dataclass
class ReplicationDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_control_translation": "AccessControlTranslation",
        "account": "Account",
        "metrics": "Metrics",
        "bucket": "Bucket",
        "encryption_configuration": "EncryptionConfiguration",
        "storage_class": "StorageClass",
        "replication_time": "ReplicationTime",
    }

    access_control_translation: Optional[AccessControlTranslation] = None
    account: Optional[Union[str, Ref, GetAtt, Sub]] = None
    metrics: Optional[Metrics] = None
    bucket: Optional[Union[str, Ref, GetAtt, Sub]] = None
    encryption_configuration: Optional[EncryptionConfiguration] = None
    storage_class: Optional[Union[str, Ref, GetAtt, Sub]] = None
    replication_time: Optional[ReplicationTime] = None


@dataclass
class ReplicationRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "destination": "Destination",
        "filter": "Filter",
        "priority": "Priority",
        "source_selection_criteria": "SourceSelectionCriteria",
        "id": "Id",
        "prefix": "Prefix",
        "delete_marker_replication": "DeleteMarkerReplication",
    }

    status: Optional[Union[str, ReplicationRuleStatus, Ref, GetAtt, Sub]] = None
    destination: Optional[ReplicationDestination] = None
    filter: Optional[ReplicationRuleFilter] = None
    priority: Optional[Union[int, Ref, GetAtt, Sub]] = None
    source_selection_criteria: Optional[SourceSelectionCriteria] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    delete_marker_replication: Optional[DeleteMarkerReplication] = None


@dataclass
class ReplicationRuleAndOperator(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tag_filters": "TagFilters",
        "prefix": "Prefix",
    }

    tag_filters: Optional[list[TagFilter]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationRuleFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "and_": "And",
        "tag_filter": "TagFilter",
        "prefix": "Prefix",
    }

    and_: Optional[ReplicationRuleAndOperator] = None
    tag_filter: Optional[TagFilter] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationTime(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "time": "Time",
    }

    status: Optional[Union[str, ReplicationTimeStatus, Ref, GetAtt, Sub]] = None
    time: Optional[ReplicationTimeValue] = None


@dataclass
class ReplicationTimeValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "minutes": "Minutes",
    }

    minutes: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class RoutingRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "redirect_rule": "RedirectRule",
        "routing_rule_condition": "RoutingRuleCondition",
    }

    redirect_rule: Optional[RedirectRule] = None
    routing_rule_condition: Optional[RoutingRuleCondition] = None


@dataclass
class RoutingRuleCondition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_prefix_equals": "KeyPrefixEquals",
        "http_error_code_returned_equals": "HttpErrorCodeReturnedEquals",
    }

    key_prefix_equals: Optional[Union[str, Ref, GetAtt, Sub]] = None
    http_error_code_returned_equals: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Rule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "expired_object_delete_marker": "ExpiredObjectDeleteMarker",
        "noncurrent_version_expiration_in_days": "NoncurrentVersionExpirationInDays",
        "transitions": "Transitions",
        "object_size_greater_than": "ObjectSizeGreaterThan",
        "tag_filters": "TagFilters",
        "noncurrent_version_transitions": "NoncurrentVersionTransitions",
        "prefix": "Prefix",
        "object_size_less_than": "ObjectSizeLessThan",
        "noncurrent_version_transition": "NoncurrentVersionTransition",
        "expiration_date": "ExpirationDate",
        "noncurrent_version_expiration": "NoncurrentVersionExpiration",
        "expiration_in_days": "ExpirationInDays",
        "transition": "Transition",
        "id": "Id",
        "abort_incomplete_multipart_upload": "AbortIncompleteMultipartUpload",
    }

    status: Optional[Union[str, ExpirationStatus, Ref, GetAtt, Sub]] = None
    expired_object_delete_marker: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    noncurrent_version_expiration_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    transitions: Optional[list[Transition]] = None
    object_size_greater_than: Optional[Union[str, Ref, GetAtt, Sub]] = None
    tag_filters: Optional[list[TagFilter]] = None
    noncurrent_version_transitions: Optional[list[NoncurrentVersionTransition]] = None
    prefix: Optional[Union[str, Ref, GetAtt, Sub]] = None
    object_size_less_than: Optional[Union[str, Ref, GetAtt, Sub]] = None
    noncurrent_version_transition: Optional[NoncurrentVersionTransition] = None
    expiration_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    noncurrent_version_expiration: Optional[NoncurrentVersionExpiration] = None
    expiration_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None
    transition: Optional[Transition] = None
    id: Optional[Union[str, Ref, GetAtt, Sub]] = None
    abort_incomplete_multipart_upload: Optional[AbortIncompleteMultipartUpload] = None


@dataclass
class S3KeyFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "rules": "Rules",
    }

    rules: Optional[list[FilterRule]] = None


@dataclass
class S3TablesDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "table_bucket_arn": "TableBucketArn",
        "table_name": "TableName",
        "table_arn": "TableArn",
        "table_namespace": "TableNamespace",
    }

    table_bucket_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    table_namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionByDefault(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_algorithm": "SSEAlgorithm",
        "kms_master_key_id": "KMSMasterKeyID",
    }

    sse_algorithm: Optional[Union[str, ServerSideEncryption, Ref, GetAtt, Sub]] = None
    kms_master_key_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ServerSideEncryptionRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_key_enabled": "BucketKeyEnabled",
        "blocked_encryption_types": "BlockedEncryptionTypes",
        "server_side_encryption_by_default": "ServerSideEncryptionByDefault",
    }

    bucket_key_enabled: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    blocked_encryption_types: Optional[BlockedEncryptionTypes] = None
    server_side_encryption_by_default: Optional[ServerSideEncryptionByDefault] = None


@dataclass
class SourceSelectionCriteria(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "replica_modifications": "ReplicaModifications",
        "sse_kms_encrypted_objects": "SseKmsEncryptedObjects",
    }

    replica_modifications: Optional[ReplicaModifications] = None
    sse_kms_encrypted_objects: Optional[SseKmsEncryptedObjects] = None


@dataclass
class SseKmsEncryptedObjects(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, SseKmsEncryptedObjectsStatus, Ref, GetAtt, Sub]] = None


@dataclass
class StorageClassAnalysis(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_export": "DataExport",
    }

    data_export: Optional[DataExport] = None


@dataclass
class TagFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TargetObjectKeyFormat(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "partitioned_prefix": "PartitionedPrefix",
        "simple_prefix": "SimplePrefix",
    }

    partitioned_prefix: Optional[PartitionedPrefix] = None
    simple_prefix: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class Tiering(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_tier": "AccessTier",
        "days": "Days",
    }

    access_tier: Optional[Union[str, IntelligentTieringAccessTier, Ref, GetAtt, Sub]] = None
    days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class TopicConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "event": "Event",
        "topic": "Topic",
    }

    filter: Optional[NotificationFilter] = None
    event: Optional[Union[str, Ref, GetAtt, Sub]] = None
    topic: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Transition(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transition_date": "TransitionDate",
        "storage_class": "StorageClass",
        "transition_in_days": "TransitionInDays",
    }

    transition_date: Optional[Union[str, Ref, GetAtt, Sub]] = None
    storage_class: Optional[Union[str, TransitionStorageClass, Ref, GetAtt, Sub]] = None
    transition_in_days: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class VersioningConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, BucketVersioningStatus, Ref, GetAtt, Sub]] = None


@dataclass
class WebsiteConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "index_document": "IndexDocument",
        "redirect_all_requests_to": "RedirectAllRequestsTo",
        "routing_rules": "RoutingRules",
        "error_document": "ErrorDocument",
    }

    index_document: Optional[Union[str, Ref, GetAtt, Sub]] = None
    redirect_all_requests_to: Optional[RedirectAllRequestsTo] = None
    routing_rules: Optional[list[RoutingRule]] = None
    error_document: Optional[Union[str, Ref, GetAtt, Sub]] = None

