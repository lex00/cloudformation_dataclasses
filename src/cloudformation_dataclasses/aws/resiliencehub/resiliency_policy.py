"""PropertyTypes for AWS::ResilienceHub::ResiliencyPolicy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AlarmType:
    """AlarmType enum values."""

    METRIC = "Metric"
    COMPOSITE = "Composite"
    CANARY = "Canary"
    LOGS = "Logs"
    EVENT = "Event"


class AppAssessmentScheduleType:
    """AppAssessmentScheduleType enum values."""

    DISABLED = "Disabled"
    DAILY = "Daily"


class AppComplianceStatusType:
    """AppComplianceStatusType enum values."""

    POLICYBREACHED = "PolicyBreached"
    POLICYMET = "PolicyMet"
    NOTASSESSED = "NotAssessed"
    CHANGESDETECTED = "ChangesDetected"
    NOTAPPLICABLE = "NotApplicable"
    MISSINGPOLICY = "MissingPolicy"


class AppDriftStatusType:
    """AppDriftStatusType enum values."""

    NOTCHECKED = "NotChecked"
    NOTDETECTED = "NotDetected"
    DETECTED = "Detected"


class AppStatusType:
    """AppStatusType enum values."""

    ACTIVE = "Active"
    DELETING = "Deleting"


class AssessmentInvoker:
    """AssessmentInvoker enum values."""

    USER = "User"
    SYSTEM = "System"


class AssessmentStatus:
    """AssessmentStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCESS = "Success"


class ComplianceStatus:
    """ComplianceStatus enum values."""

    POLICYBREACHED = "PolicyBreached"
    POLICYMET = "PolicyMet"
    NOTAPPLICABLE = "NotApplicable"
    MISSINGPOLICY = "MissingPolicy"


class ConditionOperatorType:
    """ConditionOperatorType enum values."""

    EQUALS = "Equals"
    NOTEQUALS = "NotEquals"
    GREATERTHEN = "GreaterThen"
    GREATEROREQUALS = "GreaterOrEquals"
    LESSTHEN = "LessThen"
    LESSOREQUALS = "LessOrEquals"


class ConfigRecommendationOptimizationType:
    """ConfigRecommendationOptimizationType enum values."""

    LEASTCOST = "LeastCost"
    LEASTCHANGE = "LeastChange"
    BESTAZRECOVERY = "BestAZRecovery"
    LEASTERRORS = "LeastErrors"
    BESTATTAINABLE = "BestAttainable"
    BESTREGIONRECOVERY = "BestRegionRecovery"


class CostFrequency:
    """CostFrequency enum values."""

    HOURLY = "Hourly"
    DAILY = "Daily"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"


class DataLocationConstraint:
    """DataLocationConstraint enum values."""

    ANYLOCATION = "AnyLocation"
    SAMECONTINENT = "SameContinent"
    SAMECOUNTRY = "SameCountry"


class DifferenceType:
    """DifferenceType enum values."""

    NOTEQUAL = "NotEqual"
    ADDED = "Added"
    REMOVED = "Removed"


class DisruptionType:
    """DisruptionType enum values."""

    SOFTWARE = "Software"
    HARDWARE = "Hardware"
    AZ = "AZ"
    REGION = "Region"


class DriftStatus:
    """DriftStatus enum values."""

    NOTCHECKED = "NotChecked"
    NOTDETECTED = "NotDetected"
    DETECTED = "Detected"


class DriftType:
    """DriftType enum values."""

    APPLICATIONCOMPLIANCE = "ApplicationCompliance"
    APPCOMPONENTRESILIENCYCOMPLIANCESTATUS = "AppComponentResiliencyComplianceStatus"


class EstimatedCostTier:
    """EstimatedCostTier enum values."""

    L1 = "L1"
    L2 = "L2"
    L3 = "L3"
    L4 = "L4"


class EventType:
    """EventType enum values."""

    SCHEDULEDASSESSMENTFAILURE = "ScheduledAssessmentFailure"
    DRIFTDETECTED = "DriftDetected"


class ExcludeRecommendationReason:
    """ExcludeRecommendationReason enum values."""

    ALREADYIMPLEMENTED = "AlreadyImplemented"
    NOTRELEVANT = "NotRelevant"
    COMPLEXITYOFIMPLEMENTATION = "ComplexityOfImplementation"


class FieldAggregationType:
    """FieldAggregationType enum values."""

    MIN = "Min"
    MAX = "Max"
    SUM = "Sum"
    AVG = "Avg"
    COUNT = "Count"


class GroupingRecommendationConfidenceLevel:
    """GroupingRecommendationConfidenceLevel enum values."""

    HIGH = "High"
    MEDIUM = "Medium"


class GroupingRecommendationRejectionReason:
    """GroupingRecommendationRejectionReason enum values."""

    DISTINCTBUSINESSPURPOSE = "DistinctBusinessPurpose"
    SEPARATEDATACONCERN = "SeparateDataConcern"
    DISTINCTUSERGROUPHANDLING = "DistinctUserGroupHandling"
    OTHER = "Other"


class GroupingRecommendationStatusType:
    """GroupingRecommendationStatusType enum values."""

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    PENDINGDECISION = "PendingDecision"


class HaArchitecture:
    """HaArchitecture enum values."""

    MULTISITE = "MultiSite"
    WARMSTANDBY = "WarmStandby"
    PILOTLIGHT = "PilotLight"
    BACKUPANDRESTORE = "BackupAndRestore"
    NORECOVERYPLAN = "NoRecoveryPlan"


class MetricsExportStatusType:
    """MetricsExportStatusType enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCESS = "Success"


class PermissionModelType:
    """PermissionModelType enum values."""

    LEGACYIAMUSER = "LegacyIAMUser"
    ROLEBASED = "RoleBased"


class PhysicalIdentifierType:
    """PhysicalIdentifierType enum values."""

    ARN = "Arn"
    NATIVE = "Native"


class RecommendationComplianceStatus:
    """RecommendationComplianceStatus enum values."""

    BREACHEDUNATTAINABLE = "BreachedUnattainable"
    BREACHEDCANMEET = "BreachedCanMeet"
    METCANIMPROVE = "MetCanImprove"
    MISSINGPOLICY = "MissingPolicy"


class RecommendationStatus:
    """RecommendationStatus enum values."""

    IMPLEMENTED = "Implemented"
    INACTIVE = "Inactive"
    NOTIMPLEMENTED = "NotImplemented"
    EXCLUDED = "Excluded"


class RecommendationTemplateStatus:
    """RecommendationTemplateStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCESS = "Success"


class RenderRecommendationType:
    """RenderRecommendationType enum values."""

    ALARM = "Alarm"
    SOP = "Sop"
    TEST = "Test"


class ResiliencyPolicyTier:
    """ResiliencyPolicyTier enum values."""

    MISSIONCRITICAL = "MissionCritical"
    CRITICAL = "Critical"
    IMPORTANT = "Important"
    CORESERVICES = "CoreServices"
    NONCRITICAL = "NonCritical"
    NOTAPPLICABLE = "NotApplicable"


class ResiliencyScoreType:
    """ResiliencyScoreType enum values."""

    COMPLIANCE = "Compliance"
    TEST = "Test"
    ALARM = "Alarm"
    SOP = "Sop"


class ResourceImportStatusType:
    """ResourceImportStatusType enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCESS = "Success"


class ResourceImportStrategyType:
    """ResourceImportStrategyType enum values."""

    ADDONLY = "AddOnly"
    REPLACEALL = "ReplaceAll"


class ResourceMappingType:
    """ResourceMappingType enum values."""

    CFNSTACK = "CfnStack"
    RESOURCE = "Resource"
    APPREGISTRYAPP = "AppRegistryApp"
    RESOURCEGROUP = "ResourceGroup"
    TERRAFORM = "Terraform"
    EKS = "EKS"


class ResourceResolutionStatusType:
    """ResourceResolutionStatusType enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCESS = "Success"


class ResourceSourceType:
    """ResourceSourceType enum values."""

    APPTEMPLATE = "AppTemplate"
    DISCOVERED = "Discovered"


class ResourcesGroupingRecGenStatusType:
    """ResourcesGroupingRecGenStatusType enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCESS = "Success"


class SopServiceType:
    """SopServiceType enum values."""

    SSM = "SSM"


class TemplateFormat:
    """TemplateFormat enum values."""

    CFNYAML = "CfnYaml"
    CFNJSON = "CfnJson"


class TestRisk:
    """TestRisk enum values."""

    SMALL = "Small"
    MEDIUM = "Medium"
    HIGH = "High"


class TestType:
    """TestType enum values."""

    SOFTWARE = "Software"
    HARDWARE = "Hardware"
    AZ = "AZ"
    REGION = "Region"


@dataclass
class FailurePolicy(PropertyType):
    RPO_IN_SECS = "RpoInSecs"
    RTO_IN_SECS = "RtoInSecs"

    _property_mappings: ClassVar[dict[str, str]] = {
        "rpo_in_secs": "RpoInSecs",
        "rto_in_secs": "RtoInSecs",
    }

    rpo_in_secs: Optional[Union[int, Ref, GetAtt, Sub]] = None
    rto_in_secs: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class PolicyMap(PropertyType):
    AZ = "AZ"
    REGION = "Region"
    HARDWARE = "Hardware"
    SOFTWARE = "Software"

    _property_mappings: ClassVar[dict[str, str]] = {
        "az": "AZ",
        "region": "Region",
        "hardware": "Hardware",
        "software": "Software",
    }

    az: Optional[FailurePolicy] = None
    region: Optional[FailurePolicy] = None
    hardware: Optional[FailurePolicy] = None
    software: Optional[FailurePolicy] = None

