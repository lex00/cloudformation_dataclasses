"""PropertyTypes for AWS::SecurityHub::Insight."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class ActorSessionMfaStatus:
    """ActorSessionMfaStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AdminStatus:
    """AdminStatus enum values."""

    ENABLED = "ENABLED"
    DISABLE_IN_PROGRESS = "DISABLE_IN_PROGRESS"


class AllowedOperators:
    """AllowedOperators enum values."""

    AND = "AND"
    OR = "OR"


class AssociationStatus:
    """AssociationStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AssociationType:
    """AssociationType enum values."""

    INHERITED = "INHERITED"
    APPLIED = "APPLIED"


class AutoEnableStandards:
    """AutoEnableStandards enum values."""

    NONE = "NONE"
    DEFAULT = "DEFAULT"


class AutomationRulesActionType:
    """AutomationRulesActionType enum values."""

    FINDING_FIELDS_UPDATE = "FINDING_FIELDS_UPDATE"


class AutomationRulesActionTypeV2:
    """AutomationRulesActionTypeV2 enum values."""

    FINDING_FIELDS_UPDATE = "FINDING_FIELDS_UPDATE"
    EXTERNAL_INTEGRATION = "EXTERNAL_INTEGRATION"


class AwsIamAccessKeyStatus:
    """AwsIamAccessKeyStatus enum values."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"


class AwsS3BucketNotificationConfigurationS3KeyFilterRuleName:
    """AwsS3BucketNotificationConfigurationS3KeyFilterRuleName enum values."""

    PREFIX = "Prefix"
    SUFFIX = "Suffix"


class BatchUpdateFindingsV2UnprocessedFindingErrorCode:
    """BatchUpdateFindingsV2UnprocessedFindingErrorCode enum values."""

    RESOURCENOTFOUNDEXCEPTION = "ResourceNotFoundException"
    VALIDATIONEXCEPTION = "ValidationException"
    INTERNALSERVEREXCEPTION = "InternalServerException"
    CONFLICTEXCEPTION = "ConflictException"


class ComplianceStatus:
    """ComplianceStatus enum values."""

    PASSED = "PASSED"
    WARNING = "WARNING"
    FAILED = "FAILED"
    NOT_AVAILABLE = "NOT_AVAILABLE"


class ConfigurationPolicyAssociationStatus:
    """ConfigurationPolicyAssociationStatus enum values."""

    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class ConnectionDirection:
    """ConnectionDirection enum values."""

    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"


class ConnectorAuthStatus:
    """ConnectorAuthStatus enum values."""

    ACTIVE = "ACTIVE"
    FAILED = "FAILED"


class ConnectorProviderName:
    """ConnectorProviderName enum values."""

    JIRA_CLOUD = "JIRA_CLOUD"
    SERVICENOW = "SERVICENOW"


class ConnectorStatus:
    """ConnectorStatus enum values."""

    CONNECTED = "CONNECTED"
    FAILED_TO_CONNECT = "FAILED_TO_CONNECT"
    PENDING_CONFIGURATION = "PENDING_CONFIGURATION"
    PENDING_AUTHORIZATION = "PENDING_AUTHORIZATION"


class ControlFindingGenerator:
    """ControlFindingGenerator enum values."""

    STANDARD_CONTROL = "STANDARD_CONTROL"
    SECURITY_CONTROL = "SECURITY_CONTROL"


class ControlStatus:
    """ControlStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DateRangeUnit:
    """DateRangeUnit enum values."""

    DAYS = "DAYS"


class FindingHistoryUpdateSourceType:
    """FindingHistoryUpdateSourceType enum values."""

    BATCH_UPDATE_FINDINGS = "BATCH_UPDATE_FINDINGS"
    BATCH_IMPORT_FINDINGS = "BATCH_IMPORT_FINDINGS"


class FindingsTrendsStringField:
    """FindingsTrendsStringField enum values."""

    ACCOUNT_ID = "account_id"
    REGION = "region"
    FINDING_TYPES = "finding_types"
    FINDING_STATUS = "finding_status"
    FINDING_CVE_IDS = "finding_cve_ids"
    FINDING_COMPLIANCE_STATUS = "finding_compliance_status"
    FINDING_CONTROL_ID = "finding_control_id"
    FINDING_CLASS_NAME = "finding_class_name"
    FINDING_PROVIDER = "finding_provider"
    FINDING_ACTIVITY_NAME = "finding_activity_name"


class GranularityField:
    """GranularityField enum values."""

    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"


class GroupByField:
    """GroupByField enum values."""

    ACTIVITY_NAME = "activity_name"
    CLOUD_ACCOUNT_UID = "cloud.account.uid"
    CLOUD_PROVIDER = "cloud.provider"
    CLOUD_REGION = "cloud.region"
    COMPLIANCE_ASSESSMENTS_NAME = "compliance.assessments.name"
    COMPLIANCE_STATUS = "compliance.status"
    COMPLIANCE_CONTROL = "compliance.control"
    FINDING_INFO_TITLE = "finding_info.title"
    FINDING_INFO_RELATED_EVENTS_TRAITS_CATEGORY = "finding_info.related_events.traits.category"
    FINDING_INFO_TYPES = "finding_info.types"
    METADATA_PRODUCT_NAME = "metadata.product.name"
    METADATA_PRODUCT_UID = "metadata.product.uid"
    RESOURCES_TYPE = "resources.type"
    RESOURCES_UID = "resources.uid"
    SEVERITY = "severity"
    STATUS = "status"
    VULNERABILITIES_FIX_COVERAGE = "vulnerabilities.fix_coverage"
    CLASS_NAME = "class_name"
    VULNERABILITIES_AFFECTED_PACKAGES_NAME = "vulnerabilities.affected_packages.name"
    FINDING_INFO_ANALYTIC_NAME = "finding_info.analytic.name"
    COMPLIANCE_STANDARDS = "compliance.standards"
    CLOUD_ACCOUNT_NAME = "cloud.account.name"
    VENDOR_ATTRIBUTES_SEVERITY = "vendor_attributes.severity"


class IntegrationType:
    """IntegrationType enum values."""

    SEND_FINDINGS_TO_SECURITY_HUB = "SEND_FINDINGS_TO_SECURITY_HUB"
    RECEIVE_FINDINGS_FROM_SECURITY_HUB = "RECEIVE_FINDINGS_FROM_SECURITY_HUB"
    UPDATE_FINDINGS_IN_SECURITY_HUB = "UPDATE_FINDINGS_IN_SECURITY_HUB"


class IntegrationV2Type:
    """IntegrationV2Type enum values."""

    SEND_FINDINGS_TO_SECURITY_HUB = "SEND_FINDINGS_TO_SECURITY_HUB"
    RECEIVE_FINDINGS_FROM_SECURITY_HUB = "RECEIVE_FINDINGS_FROM_SECURITY_HUB"
    UPDATE_FINDINGS_IN_SECURITY_HUB = "UPDATE_FINDINGS_IN_SECURITY_HUB"


class MalwareState:
    """MalwareState enum values."""

    OBSERVED = "OBSERVED"
    REMOVAL_FAILED = "REMOVAL_FAILED"
    REMOVED = "REMOVED"


class MalwareType:
    """MalwareType enum values."""

    ADWARE = "ADWARE"
    BLENDED_THREAT = "BLENDED_THREAT"
    BOTNET_AGENT = "BOTNET_AGENT"
    COIN_MINER = "COIN_MINER"
    EXPLOIT_KIT = "EXPLOIT_KIT"
    KEYLOGGER = "KEYLOGGER"
    MACRO = "MACRO"
    POTENTIALLY_UNWANTED = "POTENTIALLY_UNWANTED"
    SPYWARE = "SPYWARE"
    RANSOMWARE = "RANSOMWARE"
    REMOTE_ACCESS = "REMOTE_ACCESS"
    ROOTKIT = "ROOTKIT"
    TROJAN = "TROJAN"
    VIRUS = "VIRUS"
    WORM = "WORM"


class MapFilterComparison:
    """MapFilterComparison enum values."""

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"


class NetworkDirection:
    """NetworkDirection enum values."""

    IN = "IN"
    OUT = "OUT"


class OcsfBooleanField:
    """OcsfBooleanField enum values."""

    COMPLIANCE_ASSESSMENTS_MEETS_CRITERIA = "compliance.assessments.meets_criteria"
    VULNERABILITIES_IS_EXPLOIT_AVAILABLE = "vulnerabilities.is_exploit_available"
    VULNERABILITIES_IS_FIX_AVAILABLE = "vulnerabilities.is_fix_available"


class OcsfDateField:
    """OcsfDateField enum values."""

    FINDING_INFO_CREATED_TIME_DT = "finding_info.created_time_dt"
    FINDING_INFO_FIRST_SEEN_TIME_DT = "finding_info.first_seen_time_dt"
    FINDING_INFO_LAST_SEEN_TIME_DT = "finding_info.last_seen_time_dt"
    FINDING_INFO_MODIFIED_TIME_DT = "finding_info.modified_time_dt"
    RESOURCES_IMAGE_CREATED_TIME_DT = "resources.image.created_time_dt"
    RESOURCES_IMAGE_LAST_USED_TIME_DT = "resources.image.last_used_time_dt"
    RESOURCES_MODIFIED_TIME_DT = "resources.modified_time_dt"


class OcsfIpField:
    """OcsfIpField enum values."""

    EVIDENCES_DST_ENDPOINT_IP = "evidences.dst_endpoint.ip"
    EVIDENCES_SRC_ENDPOINT_IP = "evidences.src_endpoint.ip"


class OcsfMapField:
    """OcsfMapField enum values."""

    RESOURCES_TAGS = "resources.tags"
    COMPLIANCE_CONTROL_PARAMETERS = "compliance.control_parameters"
    DATABUCKET_TAGS = "databucket.tags"
    FINDING_INFO_TAGS = "finding_info.tags"


class OcsfNumberField:
    """OcsfNumberField enum values."""

    ACTIVITY_ID = "activity_id"
    COMPLIANCE_STATUS_ID = "compliance.status_id"
    CONFIDENCE_SCORE = "confidence_score"
    SEVERITY_ID = "severity_id"
    STATUS_ID = "status_id"
    FINDING_INFO_RELATED_EVENTS_COUNT = "finding_info.related_events_count"
    EVIDENCES_API_RESPONSE_CODE = "evidences.api.response.code"
    EVIDENCES_DST_ENDPOINT_AUTONOMOUS_SYSTEM_NUMBER = "evidences.dst_endpoint.autonomous_system.number"
    EVIDENCES_DST_ENDPOINT_PORT = "evidences.dst_endpoint.port"
    EVIDENCES_SRC_ENDPOINT_AUTONOMOUS_SYSTEM_NUMBER = "evidences.src_endpoint.autonomous_system.number"
    EVIDENCES_SRC_ENDPOINT_PORT = "evidences.src_endpoint.port"
    RESOURCES_IMAGE_IN_USE_COUNT = "resources.image.in_use_count"
    VULNERABILITIES_CVE_CVSS_BASE_SCORE = "vulnerabilities.cve.cvss.base_score"
    VENDOR_ATTRIBUTES_SEVERITY_ID = "vendor_attributes.severity_id"


class OcsfStringField:
    """OcsfStringField enum values."""

    METADATA_UID = "metadata.uid"
    ACTIVITY_NAME = "activity_name"
    CLOUD_ACCOUNT_UID = "cloud.account.uid"
    CLOUD_PROVIDER = "cloud.provider"
    CLOUD_REGION = "cloud.region"
    COMPLIANCE_ASSESSMENTS_CATEGORY = "compliance.assessments.category"
    COMPLIANCE_ASSESSMENTS_NAME = "compliance.assessments.name"
    COMPLIANCE_CONTROL = "compliance.control"
    COMPLIANCE_STATUS = "compliance.status"
    COMPLIANCE_STANDARDS = "compliance.standards"
    FINDING_INFO_DESC = "finding_info.desc"
    FINDING_INFO_SRC_URL = "finding_info.src_url"
    FINDING_INFO_TITLE = "finding_info.title"
    FINDING_INFO_TYPES = "finding_info.types"
    FINDING_INFO_UID = "finding_info.uid"
    FINDING_INFO_RELATED_EVENTS_TRAITS_CATEGORY = "finding_info.related_events.traits.category"
    FINDING_INFO_RELATED_EVENTS_UID = "finding_info.related_events.uid"
    FINDING_INFO_RELATED_EVENTS_PRODUCT_UID = "finding_info.related_events.product.uid"
    FINDING_INFO_RELATED_EVENTS_TITLE = "finding_info.related_events.title"
    METADATA_PRODUCT_NAME = "metadata.product.name"
    METADATA_PRODUCT_UID = "metadata.product.uid"
    METADATA_PRODUCT_VENDOR_NAME = "metadata.product.vendor_name"
    REMEDIATION_DESC = "remediation.desc"
    REMEDIATION_REFERENCES = "remediation.references"
    RESOURCES_CLOUD_PARTITION = "resources.cloud_partition"
    RESOURCES_REGION = "resources.region"
    RESOURCES_TYPE = "resources.type"
    RESOURCES_UID = "resources.uid"
    SEVERITY = "severity"
    STATUS = "status"
    COMMENT = "comment"
    VULNERABILITIES_FIX_COVERAGE = "vulnerabilities.fix_coverage"
    CLASS_NAME = "class_name"
    DATABUCKET_ENCRYPTION_DETAILS_ALGORITHM = "databucket.encryption_details.algorithm"
    DATABUCKET_ENCRYPTION_DETAILS_KEY_UID = "databucket.encryption_details.key_uid"
    DATABUCKET_FILE_DATA_CLASSIFICATIONS_CLASSIFIER_DETAILS_TYPE = "databucket.file.data_classifications.classifier_details.type"
    EVIDENCES_ACTOR_USER_ACCOUNT_UID = "evidences.actor.user.account.uid"
    EVIDENCES_API_OPERATION = "evidences.api.operation"
    EVIDENCES_API_RESPONSE_ERROR_MESSAGE = "evidences.api.response.error_message"
    EVIDENCES_API_SERVICE_NAME = "evidences.api.service.name"
    EVIDENCES_CONNECTION_INFO_DIRECTION = "evidences.connection_info.direction"
    EVIDENCES_CONNECTION_INFO_PROTOCOL_NAME = "evidences.connection_info.protocol_name"
    EVIDENCES_DST_ENDPOINT_AUTONOMOUS_SYSTEM_NAME = "evidences.dst_endpoint.autonomous_system.name"
    EVIDENCES_DST_ENDPOINT_LOCATION_CITY = "evidences.dst_endpoint.location.city"
    EVIDENCES_DST_ENDPOINT_LOCATION_COUNTRY = "evidences.dst_endpoint.location.country"
    EVIDENCES_SRC_ENDPOINT_AUTONOMOUS_SYSTEM_NAME = "evidences.src_endpoint.autonomous_system.name"
    EVIDENCES_SRC_ENDPOINT_HOSTNAME = "evidences.src_endpoint.hostname"
    EVIDENCES_SRC_ENDPOINT_LOCATION_CITY = "evidences.src_endpoint.location.city"
    EVIDENCES_SRC_ENDPOINT_LOCATION_COUNTRY = "evidences.src_endpoint.location.country"
    FINDING_INFO_ANALYTIC_NAME = "finding_info.analytic.name"
    MALWARE_NAME = "malware.name"
    MALWARE_SCAN_INFO_UID = "malware_scan_info.uid"
    MALWARE_SEVERITY = "malware.severity"
    RESOURCES_CLOUD_FUNCTION_LAYERS_UID_ALT = "resources.cloud_function.layers.uid_alt"
    RESOURCES_CLOUD_FUNCTION_RUNTIME = "resources.cloud_function.runtime"
    RESOURCES_CLOUD_FUNCTION_USER_UID = "resources.cloud_function.user.uid"
    RESOURCES_DEVICE_ENCRYPTION_DETAILS_KEY_UID = "resources.device.encryption_details.key_uid"
    RESOURCES_DEVICE_IMAGE_UID = "resources.device.image.uid"
    RESOURCES_IMAGE_ARCHITECTURE = "resources.image.architecture"
    RESOURCES_IMAGE_REGISTRY_UID = "resources.image.registry_uid"
    RESOURCES_IMAGE_REPOSITORY_NAME = "resources.image.repository_name"
    RESOURCES_IMAGE_UID = "resources.image.uid"
    RESOURCES_SUBNET_INFO_UID = "resources.subnet_info.uid"
    RESOURCES_VPC_UID = "resources.vpc_uid"
    VULNERABILITIES_AFFECTED_CODE_FILE_PATH = "vulnerabilities.affected_code.file.path"
    VULNERABILITIES_AFFECTED_PACKAGES_NAME = "vulnerabilities.affected_packages.name"
    VULNERABILITIES_CVE_EPSS_SCORE = "vulnerabilities.cve.epss.score"
    VULNERABILITIES_CVE_UID = "vulnerabilities.cve.uid"
    VULNERABILITIES_RELATED_VULNERABILITIES = "vulnerabilities.related_vulnerabilities"
    CLOUD_ACCOUNT_NAME = "cloud.account.name"
    VENDOR_ATTRIBUTES_SEVERITY = "vendor_attributes.severity"


class OrganizationConfigurationConfigurationType:
    """OrganizationConfigurationConfigurationType enum values."""

    CENTRAL = "CENTRAL"
    LOCAL = "LOCAL"


class OrganizationConfigurationStatus:
    """OrganizationConfigurationStatus enum values."""

    PENDING = "PENDING"
    ENABLED = "ENABLED"
    FAILED = "FAILED"


class ParameterValueType:
    """ParameterValueType enum values."""

    DEFAULT = "DEFAULT"
    CUSTOM = "CUSTOM"


class Partition:
    """Partition enum values."""

    AWS = "aws"
    AWS_CN = "aws-cn"
    AWS_US_GOV = "aws-us-gov"


class RecordState:
    """RecordState enum values."""

    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"


class RegionAvailabilityStatus:
    """RegionAvailabilityStatus enum values."""

    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"


class ResourceCategory:
    """ResourceCategory enum values."""

    COMPUTE = "Compute"
    DATABASE = "Database"
    STORAGE = "Storage"
    CODE = "Code"
    AI_ML = "AI/ML"
    IDENTITY = "Identity"
    NETWORK = "Network"
    OTHER = "Other"


class ResourceGroupByField:
    """ResourceGroupByField enum values."""

    ACCOUNTID = "AccountId"
    REGION = "Region"
    RESOURCECATEGORY = "ResourceCategory"
    RESOURCETYPE = "ResourceType"
    RESOURCENAME = "ResourceName"
    FINDINGSSUMMARY_FINDINGTYPE = "FindingsSummary.FindingType"


class ResourcesDateField:
    """ResourcesDateField enum values."""

    RESOURCEDETAILCAPTURETIME = "ResourceDetailCaptureTime"
    RESOURCECREATIONTIME = "ResourceCreationTime"


class ResourcesMapField:
    """ResourcesMapField enum values."""

    RESOURCETAGS = "ResourceTags"


class ResourcesNumberField:
    """ResourcesNumberField enum values."""

    FINDINGSSUMMARY_TOTALFINDINGS = "FindingsSummary.TotalFindings"
    FINDINGSSUMMARY_SEVERITIES_OTHER = "FindingsSummary.Severities.Other"
    FINDINGSSUMMARY_SEVERITIES_FATAL = "FindingsSummary.Severities.Fatal"
    FINDINGSSUMMARY_SEVERITIES_CRITICAL = "FindingsSummary.Severities.Critical"
    FINDINGSSUMMARY_SEVERITIES_HIGH = "FindingsSummary.Severities.High"
    FINDINGSSUMMARY_SEVERITIES_MEDIUM = "FindingsSummary.Severities.Medium"
    FINDINGSSUMMARY_SEVERITIES_LOW = "FindingsSummary.Severities.Low"
    FINDINGSSUMMARY_SEVERITIES_INFORMATIONAL = "FindingsSummary.Severities.Informational"
    FINDINGSSUMMARY_SEVERITIES_UNKNOWN = "FindingsSummary.Severities.Unknown"


class ResourcesStringField:
    """ResourcesStringField enum values."""

    RESOURCEGUID = "ResourceGuid"
    RESOURCEID = "ResourceId"
    ACCOUNTID = "AccountId"
    REGION = "Region"
    RESOURCECATEGORY = "ResourceCategory"
    RESOURCETYPE = "ResourceType"
    RESOURCENAME = "ResourceName"
    FINDINGSSUMMARY_FINDINGTYPE = "FindingsSummary.FindingType"
    FINDINGSSUMMARY_PRODUCTNAME = "FindingsSummary.ProductName"


class ResourcesTrendsStringField:
    """ResourcesTrendsStringField enum values."""

    ACCOUNT_ID = "account_id"
    REGION = "region"
    RESOURCE_TYPE = "resource_type"
    RESOURCE_CATEGORY = "resource_category"


class RuleStatus:
    """RuleStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RuleStatusV2:
    """RuleStatusV2 enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class SecurityControlProperty:
    """SecurityControlProperty enum values."""

    PARAMETERS = "Parameters"


class SecurityHubFeature:
    """SecurityHubFeature enum values."""

    SECURITYHUB = "SecurityHub"
    SECURITYHUBV2 = "SecurityHubV2"


class SeverityLabel:
    """SeverityLabel enum values."""

    INFORMATIONAL = "INFORMATIONAL"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class SeverityRating:
    """SeverityRating enum values."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class SortOrder:
    """SortOrder enum values."""

    ASC = "asc"
    DESC = "desc"


class StandardsControlsUpdatable:
    """StandardsControlsUpdatable enum values."""

    READY_FOR_UPDATES = "READY_FOR_UPDATES"
    NOT_READY_FOR_UPDATES = "NOT_READY_FOR_UPDATES"


class StandardsStatus:
    """StandardsStatus enum values."""

    PENDING = "PENDING"
    READY = "READY"
    FAILED = "FAILED"
    DELETING = "DELETING"
    INCOMPLETE = "INCOMPLETE"


class StatusReasonCode:
    """StatusReasonCode enum values."""

    NO_AVAILABLE_CONFIGURATION_RECORDER = "NO_AVAILABLE_CONFIGURATION_RECORDER"
    MAXIMUM_NUMBER_OF_CONFIG_RULES_EXCEEDED = "MAXIMUM_NUMBER_OF_CONFIG_RULES_EXCEEDED"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class StringFilterComparison:
    """StringFilterComparison enum values."""

    EQUALS = "EQUALS"
    PREFIX = "PREFIX"
    NOT_EQUALS = "NOT_EQUALS"
    PREFIX_NOT_EQUALS = "PREFIX_NOT_EQUALS"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    CONTAINS_WORD = "CONTAINS_WORD"


class TargetType:
    """TargetType enum values."""

    ACCOUNT = "ACCOUNT"
    ORGANIZATIONAL_UNIT = "ORGANIZATIONAL_UNIT"
    ROOT = "ROOT"


class ThreatIntelIndicatorCategory:
    """ThreatIntelIndicatorCategory enum values."""

    BACKDOOR = "BACKDOOR"
    CARD_STEALER = "CARD_STEALER"
    COMMAND_AND_CONTROL = "COMMAND_AND_CONTROL"
    DROP_SITE = "DROP_SITE"
    EXPLOIT_SITE = "EXPLOIT_SITE"
    KEYLOGGER = "KEYLOGGER"


class ThreatIntelIndicatorType:
    """ThreatIntelIndicatorType enum values."""

    DOMAIN = "DOMAIN"
    EMAIL_ADDRESS = "EMAIL_ADDRESS"
    HASH_MD5 = "HASH_MD5"
    HASH_SHA1 = "HASH_SHA1"
    HASH_SHA256 = "HASH_SHA256"
    HASH_SHA512 = "HASH_SHA512"
    IPV4_ADDRESS = "IPV4_ADDRESS"
    IPV6_ADDRESS = "IPV6_ADDRESS"
    MUTEX = "MUTEX"
    PROCESS = "PROCESS"
    URL = "URL"


class TicketCreationMode:
    """TicketCreationMode enum values."""

    DRYRUN = "DRYRUN"


class UnprocessedErrorCode:
    """UnprocessedErrorCode enum values."""

    INVALID_INPUT = "INVALID_INPUT"
    ACCESS_DENIED = "ACCESS_DENIED"
    NOT_FOUND = "NOT_FOUND"
    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"
    LIMIT_EXCEEDED = "LIMIT_EXCEEDED"


class UpdateStatus:
    """UpdateStatus enum values."""

    READY = "READY"
    UPDATING = "UPDATING"


class VerificationState:
    """VerificationState enum values."""

    UNKNOWN = "UNKNOWN"
    TRUE_POSITIVE = "TRUE_POSITIVE"
    FALSE_POSITIVE = "FALSE_POSITIVE"
    BENIGN_POSITIVE = "BENIGN_POSITIVE"


class VulnerabilityExploitAvailable:
    """VulnerabilityExploitAvailable enum values."""

    YES = "YES"
    NO = "NO"


class VulnerabilityFixAvailable:
    """VulnerabilityFixAvailable enum values."""

    YES = "YES"
    NO = "NO"
    PARTIAL = "PARTIAL"


class WorkflowState:
    """WorkflowState enum values."""

    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    DEFERRED = "DEFERRED"
    RESOLVED = "RESOLVED"


class WorkflowStatus:
    """WorkflowStatus enum values."""

    NEW = "NEW"
    NOTIFIED = "NOTIFIED"
    RESOLVED = "RESOLVED"
    SUPPRESSED = "SUPPRESSED"


@dataclass
class AwsSecurityFindingFilters(PropertyType):
    RESOURCE_AWS_EC2_INSTANCE_IAM_INSTANCE_PROFILE_ARN = "ResourceAwsEc2InstanceIamInstanceProfileArn"
    SOURCE_URL = "SourceUrl"
    PROCESS_NAME = "ProcessName"
    FINDING_PROVIDER_FIELDS_CONFIDENCE = "FindingProviderFieldsConfidence"
    FIRST_OBSERVED_AT = "FirstObservedAt"
    CREATED_AT = "CreatedAt"
    MALWARE_STATE = "MalwareState"
    USER_DEFINED_FIELDS = "UserDefinedFields"
    NETWORK_SOURCE_PORT = "NetworkSourcePort"
    RESOURCE_AWS_IAM_USER_USER_NAME = "ResourceAwsIamUserUserName"
    NETWORK_SOURCE_DOMAIN = "NetworkSourceDomain"
    RESOURCE_PARTITION = "ResourcePartition"
    FINDING_PROVIDER_FIELDS_RELATED_FINDINGS_ID = "FindingProviderFieldsRelatedFindingsId"
    NETWORK_DIRECTION = "NetworkDirection"
    CRITICALITY = "Criticality"
    RESOURCE_APPLICATION_ARN = "ResourceApplicationArn"
    COMPLIANCE_SECURITY_CONTROL_PARAMETERS_VALUE = "ComplianceSecurityControlParametersValue"
    SEVERITY_LABEL = "SeverityLabel"
    RELATED_FINDINGS_PRODUCT_ARN = "RelatedFindingsProductArn"
    RESOURCE_AWS_IAM_ACCESS_KEY_PRINCIPAL_NAME = "ResourceAwsIamAccessKeyPrincipalName"
    THREAT_INTEL_INDICATOR_CATEGORY = "ThreatIntelIndicatorCategory"
    COMPLIANCE_STATUS = "ComplianceStatus"
    THREAT_INTEL_INDICATOR_VALUE = "ThreatIntelIndicatorValue"
    RESOURCE_CONTAINER_IMAGE_NAME = "ResourceContainerImageName"
    MALWARE_TYPE = "MalwareType"
    THREAT_INTEL_INDICATOR_SOURCE = "ThreatIntelIndicatorSource"
    RESOURCE_AWS_IAM_ACCESS_KEY_CREATED_AT = "ResourceAwsIamAccessKeyCreatedAt"
    RESOURCE_AWS_EC2_INSTANCE_TYPE = "ResourceAwsEc2InstanceType"
    RECOMMENDATION_TEXT = "RecommendationText"
    AWS_ACCOUNT_NAME = "AwsAccountName"
    FINDING_PROVIDER_FIELDS_RELATED_FINDINGS_PRODUCT_ARN = "FindingProviderFieldsRelatedFindingsProductArn"
    AWS_ACCOUNT_ID = "AwsAccountId"
    ID = "Id"
    PROCESS_PARENT_PID = "ProcessParentPid"
    RESOURCE_APPLICATION_NAME = "ResourceApplicationName"
    PRODUCT_ARN = "ProductArn"
    RESOURCE_AWS_EC2_INSTANCE_IP_V6_ADDRESSES = "ResourceAwsEc2InstanceIpV6Addresses"
    MALWARE_NAME = "MalwareName"
    DESCRIPTION = "Description"
    RESOURCE_CONTAINER_LAUNCHED_AT = "ResourceContainerLaunchedAt"
    PROCESS_PID = "ProcessPid"
    NOTE_TEXT = "NoteText"
    RESOURCE_AWS_EC2_INSTANCE_KEY_NAME = "ResourceAwsEc2InstanceKeyName"
    FINDING_PROVIDER_FIELDS_TYPES = "FindingProviderFieldsTypes"
    COMPLIANCE_SECURITY_CONTROL_ID = "ComplianceSecurityControlId"
    NOTE_UPDATED_BY = "NoteUpdatedBy"
    VERIFICATION_STATE = "VerificationState"
    GENERATOR_ID = "GeneratorId"
    RESOURCE_TYPE = "ResourceType"
    NETWORK_PROTOCOL = "NetworkProtocol"
    UPDATED_AT = "UpdatedAt"
    PROCESS_PATH = "ProcessPath"
    WORKFLOW_STATUS = "WorkflowStatus"
    RESOURCE_CONTAINER_NAME = "ResourceContainerName"
    TYPE = "Type"
    RESOURCE_ID = "ResourceId"
    NETWORK_DESTINATION_DOMAIN = "NetworkDestinationDomain"
    PRODUCT_NAME = "ProductName"
    RESOURCE_TAGS = "ResourceTags"
    RESOURCE_AWS_EC2_INSTANCE_VPC_ID = "ResourceAwsEc2InstanceVpcId"
    RESOURCE_AWS_S3_BUCKET_OWNER_NAME = "ResourceAwsS3BucketOwnerName"
    LAST_OBSERVED_AT = "LastObservedAt"
    COMPLIANCE_SECURITY_CONTROL_PARAMETERS_NAME = "ComplianceSecurityControlParametersName"
    NETWORK_SOURCE_IP_V4 = "NetworkSourceIpV4"
    PROCESS_LAUNCHED_AT = "ProcessLaunchedAt"
    RESOURCE_AWS_EC2_INSTANCE_LAUNCHED_AT = "ResourceAwsEc2InstanceLaunchedAt"
    NOTE_UPDATED_AT = "NoteUpdatedAt"
    THREAT_INTEL_INDICATOR_TYPE = "ThreatIntelIndicatorType"
    COMPANY_NAME = "CompanyName"
    RESOURCE_REGION = "ResourceRegion"
    RESOURCE_AWS_IAM_ACCESS_KEY_STATUS = "ResourceAwsIamAccessKeyStatus"
    NETWORK_SOURCE_IP_V6 = "NetworkSourceIpV6"
    CONFIDENCE = "Confidence"
    PRODUCT_FIELDS = "ProductFields"
    THREAT_INTEL_INDICATOR_LAST_OBSERVED_AT = "ThreatIntelIndicatorLastObservedAt"
    RESOURCE_AWS_EC2_INSTANCE_SUBNET_ID = "ResourceAwsEc2InstanceSubnetId"
    COMPLIANCE_ASSOCIATED_STANDARDS_ID = "ComplianceAssociatedStandardsId"
    RESOURCE_AWS_EC2_INSTANCE_IMAGE_ID = "ResourceAwsEc2InstanceImageId"
    RESOURCE_AWS_EC2_INSTANCE_IP_V4_ADDRESSES = "ResourceAwsEc2InstanceIpV4Addresses"
    RELATED_FINDINGS_ID = "RelatedFindingsId"
    PROCESS_TERMINATED_AT = "ProcessTerminatedAt"
    RESOURCE_CONTAINER_IMAGE_ID = "ResourceContainerImageId"
    NETWORK_DESTINATION_IP_V4 = "NetworkDestinationIpV4"
    REGION = "Region"
    NETWORK_DESTINATION_IP_V6 = "NetworkDestinationIpV6"
    VULNERABILITIES_EXPLOIT_AVAILABLE = "VulnerabilitiesExploitAvailable"
    FINDING_PROVIDER_FIELDS_CRITICALITY = "FindingProviderFieldsCriticality"
    NETWORK_DESTINATION_PORT = "NetworkDestinationPort"
    RESOURCE_DETAILS_OTHER = "ResourceDetailsOther"
    FINDING_PROVIDER_FIELDS_SEVERITY_LABEL = "FindingProviderFieldsSeverityLabel"
    THREAT_INTEL_INDICATOR_SOURCE_URL = "ThreatIntelIndicatorSourceUrl"
    FINDING_PROVIDER_FIELDS_SEVERITY_ORIGINAL = "FindingProviderFieldsSeverityOriginal"
    MALWARE_PATH = "MalwarePath"
    SAMPLE = "Sample"
    RECORD_STATE = "RecordState"
    TITLE = "Title"
    WORKFLOW_STATE = "WorkflowState"
    NETWORK_SOURCE_MAC = "NetworkSourceMac"
    RESOURCE_AWS_S3_BUCKET_OWNER_ID = "ResourceAwsS3BucketOwnerId"
    VULNERABILITIES_FIX_AVAILABLE = "VulnerabilitiesFixAvailable"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_aws_ec2_instance_iam_instance_profile_arn": "ResourceAwsEc2InstanceIamInstanceProfileArn",
        "source_url": "SourceUrl",
        "process_name": "ProcessName",
        "finding_provider_fields_confidence": "FindingProviderFieldsConfidence",
        "first_observed_at": "FirstObservedAt",
        "created_at": "CreatedAt",
        "malware_state": "MalwareState",
        "user_defined_fields": "UserDefinedFields",
        "network_source_port": "NetworkSourcePort",
        "resource_aws_iam_user_user_name": "ResourceAwsIamUserUserName",
        "network_source_domain": "NetworkSourceDomain",
        "resource_partition": "ResourcePartition",
        "finding_provider_fields_related_findings_id": "FindingProviderFieldsRelatedFindingsId",
        "network_direction": "NetworkDirection",
        "criticality": "Criticality",
        "resource_application_arn": "ResourceApplicationArn",
        "compliance_security_control_parameters_value": "ComplianceSecurityControlParametersValue",
        "severity_label": "SeverityLabel",
        "related_findings_product_arn": "RelatedFindingsProductArn",
        "resource_aws_iam_access_key_principal_name": "ResourceAwsIamAccessKeyPrincipalName",
        "threat_intel_indicator_category": "ThreatIntelIndicatorCategory",
        "compliance_status": "ComplianceStatus",
        "threat_intel_indicator_value": "ThreatIntelIndicatorValue",
        "resource_container_image_name": "ResourceContainerImageName",
        "malware_type": "MalwareType",
        "threat_intel_indicator_source": "ThreatIntelIndicatorSource",
        "resource_aws_iam_access_key_created_at": "ResourceAwsIamAccessKeyCreatedAt",
        "resource_aws_ec2_instance_type": "ResourceAwsEc2InstanceType",
        "recommendation_text": "RecommendationText",
        "aws_account_name": "AwsAccountName",
        "finding_provider_fields_related_findings_product_arn": "FindingProviderFieldsRelatedFindingsProductArn",
        "aws_account_id": "AwsAccountId",
        "id": "Id",
        "process_parent_pid": "ProcessParentPid",
        "resource_application_name": "ResourceApplicationName",
        "product_arn": "ProductArn",
        "resource_aws_ec2_instance_ip_v6_addresses": "ResourceAwsEc2InstanceIpV6Addresses",
        "malware_name": "MalwareName",
        "description": "Description",
        "resource_container_launched_at": "ResourceContainerLaunchedAt",
        "process_pid": "ProcessPid",
        "note_text": "NoteText",
        "resource_aws_ec2_instance_key_name": "ResourceAwsEc2InstanceKeyName",
        "finding_provider_fields_types": "FindingProviderFieldsTypes",
        "compliance_security_control_id": "ComplianceSecurityControlId",
        "note_updated_by": "NoteUpdatedBy",
        "verification_state": "VerificationState",
        "generator_id": "GeneratorId",
        "resource_type": "ResourceType",
        "network_protocol": "NetworkProtocol",
        "updated_at": "UpdatedAt",
        "process_path": "ProcessPath",
        "workflow_status": "WorkflowStatus",
        "resource_container_name": "ResourceContainerName",
        "type_": "Type",
        "resource_id": "ResourceId",
        "network_destination_domain": "NetworkDestinationDomain",
        "product_name": "ProductName",
        "resource_tags": "ResourceTags",
        "resource_aws_ec2_instance_vpc_id": "ResourceAwsEc2InstanceVpcId",
        "resource_aws_s3_bucket_owner_name": "ResourceAwsS3BucketOwnerName",
        "last_observed_at": "LastObservedAt",
        "compliance_security_control_parameters_name": "ComplianceSecurityControlParametersName",
        "network_source_ip_v4": "NetworkSourceIpV4",
        "process_launched_at": "ProcessLaunchedAt",
        "resource_aws_ec2_instance_launched_at": "ResourceAwsEc2InstanceLaunchedAt",
        "note_updated_at": "NoteUpdatedAt",
        "threat_intel_indicator_type": "ThreatIntelIndicatorType",
        "company_name": "CompanyName",
        "resource_region": "ResourceRegion",
        "resource_aws_iam_access_key_status": "ResourceAwsIamAccessKeyStatus",
        "network_source_ip_v6": "NetworkSourceIpV6",
        "confidence": "Confidence",
        "product_fields": "ProductFields",
        "threat_intel_indicator_last_observed_at": "ThreatIntelIndicatorLastObservedAt",
        "resource_aws_ec2_instance_subnet_id": "ResourceAwsEc2InstanceSubnetId",
        "compliance_associated_standards_id": "ComplianceAssociatedStandardsId",
        "resource_aws_ec2_instance_image_id": "ResourceAwsEc2InstanceImageId",
        "resource_aws_ec2_instance_ip_v4_addresses": "ResourceAwsEc2InstanceIpV4Addresses",
        "related_findings_id": "RelatedFindingsId",
        "process_terminated_at": "ProcessTerminatedAt",
        "resource_container_image_id": "ResourceContainerImageId",
        "network_destination_ip_v4": "NetworkDestinationIpV4",
        "region": "Region",
        "network_destination_ip_v6": "NetworkDestinationIpV6",
        "vulnerabilities_exploit_available": "VulnerabilitiesExploitAvailable",
        "finding_provider_fields_criticality": "FindingProviderFieldsCriticality",
        "network_destination_port": "NetworkDestinationPort",
        "resource_details_other": "ResourceDetailsOther",
        "finding_provider_fields_severity_label": "FindingProviderFieldsSeverityLabel",
        "threat_intel_indicator_source_url": "ThreatIntelIndicatorSourceUrl",
        "finding_provider_fields_severity_original": "FindingProviderFieldsSeverityOriginal",
        "malware_path": "MalwarePath",
        "sample": "Sample",
        "record_state": "RecordState",
        "title": "Title",
        "workflow_state": "WorkflowState",
        "network_source_mac": "NetworkSourceMac",
        "resource_aws_s3_bucket_owner_id": "ResourceAwsS3BucketOwnerId",
        "vulnerabilities_fix_available": "VulnerabilitiesFixAvailable",
    }

    resource_aws_ec2_instance_iam_instance_profile_arn: Optional[list[StringFilter]] = None
    source_url: Optional[list[StringFilter]] = None
    process_name: Optional[list[StringFilter]] = None
    finding_provider_fields_confidence: Optional[list[NumberFilter]] = None
    first_observed_at: Optional[list[DateFilter]] = None
    created_at: Optional[list[DateFilter]] = None
    malware_state: Optional[list[StringFilter]] = None
    user_defined_fields: Optional[list[MapFilter]] = None
    network_source_port: Optional[list[NumberFilter]] = None
    resource_aws_iam_user_user_name: Optional[list[StringFilter]] = None
    network_source_domain: Optional[list[StringFilter]] = None
    resource_partition: Optional[list[StringFilter]] = None
    finding_provider_fields_related_findings_id: Optional[list[StringFilter]] = None
    network_direction: Optional[list[StringFilter]] = None
    criticality: Optional[list[NumberFilter]] = None
    resource_application_arn: Optional[list[StringFilter]] = None
    compliance_security_control_parameters_value: Optional[list[StringFilter]] = None
    severity_label: Optional[list[StringFilter]] = None
    related_findings_product_arn: Optional[list[StringFilter]] = None
    resource_aws_iam_access_key_principal_name: Optional[list[StringFilter]] = None
    threat_intel_indicator_category: Optional[list[StringFilter]] = None
    compliance_status: Optional[list[StringFilter]] = None
    threat_intel_indicator_value: Optional[list[StringFilter]] = None
    resource_container_image_name: Optional[list[StringFilter]] = None
    malware_type: Optional[list[StringFilter]] = None
    threat_intel_indicator_source: Optional[list[StringFilter]] = None
    resource_aws_iam_access_key_created_at: Optional[list[DateFilter]] = None
    resource_aws_ec2_instance_type: Optional[list[StringFilter]] = None
    recommendation_text: Optional[list[StringFilter]] = None
    aws_account_name: Optional[list[StringFilter]] = None
    finding_provider_fields_related_findings_product_arn: Optional[list[StringFilter]] = None
    aws_account_id: Optional[list[StringFilter]] = None
    id: Optional[list[StringFilter]] = None
    process_parent_pid: Optional[list[NumberFilter]] = None
    resource_application_name: Optional[list[StringFilter]] = None
    product_arn: Optional[list[StringFilter]] = None
    resource_aws_ec2_instance_ip_v6_addresses: Optional[list[IpFilter]] = None
    malware_name: Optional[list[StringFilter]] = None
    description: Optional[list[StringFilter]] = None
    resource_container_launched_at: Optional[list[DateFilter]] = None
    process_pid: Optional[list[NumberFilter]] = None
    note_text: Optional[list[StringFilter]] = None
    resource_aws_ec2_instance_key_name: Optional[list[StringFilter]] = None
    finding_provider_fields_types: Optional[list[StringFilter]] = None
    compliance_security_control_id: Optional[list[StringFilter]] = None
    note_updated_by: Optional[list[StringFilter]] = None
    verification_state: Optional[list[StringFilter]] = None
    generator_id: Optional[list[StringFilter]] = None
    resource_type: Optional[list[StringFilter]] = None
    network_protocol: Optional[list[StringFilter]] = None
    updated_at: Optional[list[DateFilter]] = None
    process_path: Optional[list[StringFilter]] = None
    workflow_status: Optional[list[StringFilter]] = None
    resource_container_name: Optional[list[StringFilter]] = None
    type_: Optional[list[StringFilter]] = None
    resource_id: Optional[list[StringFilter]] = None
    network_destination_domain: Optional[list[StringFilter]] = None
    product_name: Optional[list[StringFilter]] = None
    resource_tags: Optional[list[MapFilter]] = None
    resource_aws_ec2_instance_vpc_id: Optional[list[StringFilter]] = None
    resource_aws_s3_bucket_owner_name: Optional[list[StringFilter]] = None
    last_observed_at: Optional[list[DateFilter]] = None
    compliance_security_control_parameters_name: Optional[list[StringFilter]] = None
    network_source_ip_v4: Optional[list[IpFilter]] = None
    process_launched_at: Optional[list[DateFilter]] = None
    resource_aws_ec2_instance_launched_at: Optional[list[DateFilter]] = None
    note_updated_at: Optional[list[DateFilter]] = None
    threat_intel_indicator_type: Optional[list[StringFilter]] = None
    company_name: Optional[list[StringFilter]] = None
    resource_region: Optional[list[StringFilter]] = None
    resource_aws_iam_access_key_status: Optional[list[StringFilter]] = None
    network_source_ip_v6: Optional[list[IpFilter]] = None
    confidence: Optional[list[NumberFilter]] = None
    product_fields: Optional[list[MapFilter]] = None
    threat_intel_indicator_last_observed_at: Optional[list[DateFilter]] = None
    resource_aws_ec2_instance_subnet_id: Optional[list[StringFilter]] = None
    compliance_associated_standards_id: Optional[list[StringFilter]] = None
    resource_aws_ec2_instance_image_id: Optional[list[StringFilter]] = None
    resource_aws_ec2_instance_ip_v4_addresses: Optional[list[IpFilter]] = None
    related_findings_id: Optional[list[StringFilter]] = None
    process_terminated_at: Optional[list[DateFilter]] = None
    resource_container_image_id: Optional[list[StringFilter]] = None
    network_destination_ip_v4: Optional[list[IpFilter]] = None
    region: Optional[list[StringFilter]] = None
    network_destination_ip_v6: Optional[list[IpFilter]] = None
    vulnerabilities_exploit_available: Optional[list[StringFilter]] = None
    finding_provider_fields_criticality: Optional[list[NumberFilter]] = None
    network_destination_port: Optional[list[NumberFilter]] = None
    resource_details_other: Optional[list[MapFilter]] = None
    finding_provider_fields_severity_label: Optional[list[StringFilter]] = None
    threat_intel_indicator_source_url: Optional[list[StringFilter]] = None
    finding_provider_fields_severity_original: Optional[list[StringFilter]] = None
    malware_path: Optional[list[StringFilter]] = None
    sample: Optional[list[BooleanFilter]] = None
    record_state: Optional[list[StringFilter]] = None
    title: Optional[list[StringFilter]] = None
    workflow_state: Optional[list[StringFilter]] = None
    network_source_mac: Optional[list[StringFilter]] = None
    resource_aws_s3_bucket_owner_id: Optional[list[StringFilter]] = None
    vulnerabilities_fix_available: Optional[list[StringFilter]] = None


@dataclass
class BooleanFilter(PropertyType):
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DateFilter(PropertyType):
    DATE_RANGE = "DateRange"
    START = "Start"
    END = "End"

    _property_mappings: ClassVar[dict[str, str]] = {
        "date_range": "DateRange",
        "start": "Start",
        "end": "End",
    }

    date_range: Optional[DateRange] = None
    start: Optional[Union[str, Ref, GetAtt, Sub]] = None
    end: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DateRange(PropertyType):
    VALUE = "Value"
    UNIT = "Unit"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, DateRangeUnit, Ref, GetAtt, Sub]] = None


@dataclass
class IpFilter(PropertyType):
    CIDR = "Cidr"

    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MapFilter(PropertyType):
    COMPARISON = "Comparison"
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison": "Comparison",
        "value": "Value",
        "key": "Key",
    }

    comparison: Optional[Union[str, MapFilterComparison, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NumberFilter(PropertyType):
    GTE = "Gte"
    EQ = "Eq"
    LTE = "Lte"

    _property_mappings: ClassVar[dict[str, str]] = {
        "gte": "Gte",
        "eq": "Eq",
        "lte": "Lte",
    }

    gte: Optional[Union[float, Ref, GetAtt, Sub]] = None
    eq: Optional[Union[float, Ref, GetAtt, Sub]] = None
    lte: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class StringFilter(PropertyType):
    COMPARISON = "Comparison"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison": "Comparison",
        "value": "Value",
    }

    comparison: Optional[Union[str, StringFilterComparison, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None

