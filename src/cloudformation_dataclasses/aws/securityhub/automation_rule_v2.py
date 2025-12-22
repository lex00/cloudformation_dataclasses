"""PropertyTypes for AWS::SecurityHub::AutomationRuleV2."""

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
class AutomationRulesActionV2(PropertyType):
    TYPE = "Type"
    EXTERNAL_INTEGRATION_CONFIGURATION = "ExternalIntegrationConfiguration"
    FINDING_FIELDS_UPDATE = "FindingFieldsUpdate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "external_integration_configuration": "ExternalIntegrationConfiguration",
        "finding_fields_update": "FindingFieldsUpdate",
    }

    type_: Optional[Union[str, AutomationRulesActionTypeV2, Ref, GetAtt, Sub]] = None
    external_integration_configuration: Optional[ExternalIntegrationConfiguration] = None
    finding_fields_update: Optional[AutomationRulesFindingFieldsUpdateV2] = None


@dataclass
class AutomationRulesFindingFieldsUpdateV2(PropertyType):
    COMMENT = "Comment"
    STATUS_ID = "StatusId"
    SEVERITY_ID = "SeverityId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comment": "Comment",
        "status_id": "StatusId",
        "severity_id": "SeverityId",
    }

    comment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    status_id: Optional[Union[int, Ref, GetAtt, Sub]] = None
    severity_id: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class BooleanFilter(PropertyType):
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class CompositeFilter(PropertyType):
    OPERATOR = "Operator"
    STRING_FILTERS = "StringFilters"
    BOOLEAN_FILTERS = "BooleanFilters"
    DATE_FILTERS = "DateFilters"
    NUMBER_FILTERS = "NumberFilters"
    MAP_FILTERS = "MapFilters"

    _property_mappings: ClassVar[dict[str, str]] = {
        "operator": "Operator",
        "string_filters": "StringFilters",
        "boolean_filters": "BooleanFilters",
        "date_filters": "DateFilters",
        "number_filters": "NumberFilters",
        "map_filters": "MapFilters",
    }

    operator: Optional[Union[str, AllowedOperators, Ref, GetAtt, Sub]] = None
    string_filters: Optional[list[OcsfStringFilter]] = None
    boolean_filters: Optional[list[OcsfBooleanFilter]] = None
    date_filters: Optional[list[OcsfDateFilter]] = None
    number_filters: Optional[list[OcsfNumberFilter]] = None
    map_filters: Optional[list[OcsfMapFilter]] = None


@dataclass
class Criteria(PropertyType):
    OCSF_FINDING_CRITERIA = "OcsfFindingCriteria"

    _property_mappings: ClassVar[dict[str, str]] = {
        "ocsf_finding_criteria": "OcsfFindingCriteria",
    }

    ocsf_finding_criteria: Optional[OcsfFindingFilters] = None


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
class ExternalIntegrationConfiguration(PropertyType):
    CONNECTOR_ARN = "ConnectorArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "connector_arn": "ConnectorArn",
    }

    connector_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class OcsfBooleanFilter(PropertyType):
    FILTER = "Filter"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[BooleanFilter] = None
    field_name: Optional[Union[str, OcsfBooleanField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfDateFilter(PropertyType):
    FILTER = "Filter"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[DateFilter] = None
    field_name: Optional[Union[str, OcsfDateField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfFindingFilters(PropertyType):
    COMPOSITE_FILTERS = "CompositeFilters"
    COMPOSITE_OPERATOR = "CompositeOperator"

    _property_mappings: ClassVar[dict[str, str]] = {
        "composite_filters": "CompositeFilters",
        "composite_operator": "CompositeOperator",
    }

    composite_filters: Optional[list[CompositeFilter]] = None
    composite_operator: Optional[Union[str, AllowedOperators, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfMapFilter(PropertyType):
    FILTER = "Filter"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[MapFilter] = None
    field_name: Optional[Union[str, OcsfMapField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfNumberFilter(PropertyType):
    FILTER = "Filter"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[NumberFilter] = None
    field_name: Optional[Union[str, OcsfNumberField, Ref, GetAtt, Sub]] = None


@dataclass
class OcsfStringFilter(PropertyType):
    FILTER = "Filter"
    FIELD_NAME = "FieldName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "field_name": "FieldName",
    }

    filter: Optional[StringFilter] = None
    field_name: Optional[Union[str, OcsfStringField, Ref, GetAtt, Sub]] = None


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

