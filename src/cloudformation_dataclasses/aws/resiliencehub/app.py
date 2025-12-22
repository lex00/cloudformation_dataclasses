"""PropertyTypes for AWS::ResilienceHub::App."""

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
class EventSubscription(PropertyType):
    EVENT_TYPE = "EventType"
    SNS_TOPIC_ARN = "SnsTopicArn"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "event_type": "EventType",
        "sns_topic_arn": "SnsTopicArn",
        "name": "Name",
    }

    event_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sns_topic_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PermissionModel(PropertyType):
    TYPE = "Type"
    CROSS_ACCOUNT_ROLE_ARNS = "CrossAccountRoleArns"
    INVOKER_ROLE_NAME = "InvokerRoleName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "cross_account_role_arns": "CrossAccountRoleArns",
        "invoker_role_name": "InvokerRoleName",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    cross_account_role_arns: Optional[Union[list[str], Ref]] = None
    invoker_role_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class PhysicalResourceId(PropertyType):
    TYPE = "Type"
    IDENTIFIER = "Identifier"
    AWS_REGION = "AwsRegion"
    AWS_ACCOUNT_ID = "AwsAccountId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "identifier": "Identifier",
        "aws_region": "AwsRegion",
        "aws_account_id": "AwsAccountId",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    identifier: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_region: Optional[Union[str, Ref, GetAtt, Sub]] = None
    aws_account_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceMapping(PropertyType):
    MAPPING_TYPE = "MappingType"
    LOGICAL_STACK_NAME = "LogicalStackName"
    RESOURCE_NAME = "ResourceName"
    TERRAFORM_SOURCE_NAME = "TerraformSourceName"
    PHYSICAL_RESOURCE_ID = "PhysicalResourceId"
    EKS_SOURCE_NAME = "EksSourceName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mapping_type": "MappingType",
        "logical_stack_name": "LogicalStackName",
        "resource_name": "ResourceName",
        "terraform_source_name": "TerraformSourceName",
        "physical_resource_id": "PhysicalResourceId",
        "eks_source_name": "EksSourceName",
    }

    mapping_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    logical_stack_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    terraform_source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    physical_resource_id: Optional[PhysicalResourceId] = None
    eks_source_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

