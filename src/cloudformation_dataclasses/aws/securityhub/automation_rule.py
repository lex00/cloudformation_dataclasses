"""PropertyTypes for AWS::SecurityHub::AutomationRule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AutomationRulesAction(PropertyType):
    TYPE = "Type"
    FINDING_FIELDS_UPDATE = "FindingFieldsUpdate"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "finding_fields_update": "FindingFieldsUpdate",
    }

    type_: Optional[Union[str, AutomationRulesActionType, Ref, GetAtt, Sub]] = None
    finding_fields_update: Optional[AutomationRulesFindingFieldsUpdate] = None


@dataclass
class AutomationRulesFindingFieldsUpdate(PropertyType):
    TYPES = "Types"
    CONFIDENCE = "Confidence"
    NOTE = "Note"
    VERIFICATION_STATE = "VerificationState"
    RELATED_FINDINGS = "RelatedFindings"
    WORKFLOW = "Workflow"
    SEVERITY = "Severity"
    USER_DEFINED_FIELDS = "UserDefinedFields"
    CRITICALITY = "Criticality"

    _property_mappings: ClassVar[dict[str, str]] = {
        "types": "Types",
        "confidence": "Confidence",
        "note": "Note",
        "verification_state": "VerificationState",
        "related_findings": "RelatedFindings",
        "workflow": "Workflow",
        "severity": "Severity",
        "user_defined_fields": "UserDefinedFields",
        "criticality": "Criticality",
    }

    types: Optional[Union[list[str], Ref]] = None
    confidence: Optional[Union[int, Ref, GetAtt, Sub]] = None
    note: Optional[NoteUpdate] = None
    verification_state: Optional[Union[str, VerificationState, Ref, GetAtt, Sub]] = None
    related_findings: Optional[list[RelatedFinding]] = None
    workflow: Optional[WorkflowUpdate] = None
    severity: Optional[SeverityUpdate] = None
    user_defined_fields: Optional[dict[str, str]] = None
    criticality: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class AutomationRulesFindingFilters(PropertyType):
    PRODUCT_ARN = "ProductArn"
    SOURCE_URL = "SourceUrl"
    RESOURCE_DETAILS_OTHER = "ResourceDetailsOther"
    DESCRIPTION = "Description"
    PRODUCT_NAME = "ProductName"
    RESOURCE_TAGS = "ResourceTags"
    FIRST_OBSERVED_AT = "FirstObservedAt"
    CREATED_AT = "CreatedAt"
    NOTE_TEXT = "NoteText"
    LAST_OBSERVED_AT = "LastObservedAt"
    USER_DEFINED_FIELDS = "UserDefinedFields"
    NOTE_UPDATED_AT = "NoteUpdatedAt"
    COMPLIANCE_SECURITY_CONTROL_ID = "ComplianceSecurityControlId"
    COMPANY_NAME = "CompanyName"
    RESOURCE_REGION = "ResourceRegion"
    NOTE_UPDATED_BY = "NoteUpdatedBy"
    CONFIDENCE = "Confidence"
    RESOURCE_PARTITION = "ResourcePartition"
    VERIFICATION_STATE = "VerificationState"
    CRITICALITY = "Criticality"
    SEVERITY_LABEL = "SeverityLabel"
    RELATED_FINDINGS_PRODUCT_ARN = "RelatedFindingsProductArn"
    COMPLIANCE_STATUS = "ComplianceStatus"
    GENERATOR_ID = "GeneratorId"
    RECORD_STATE = "RecordState"
    TITLE = "Title"
    RESOURCE_TYPE = "ResourceType"
    COMPLIANCE_ASSOCIATED_STANDARDS_ID = "ComplianceAssociatedStandardsId"
    UPDATED_AT = "UpdatedAt"
    RELATED_FINDINGS_ID = "RelatedFindingsId"
    WORKFLOW_STATUS = "WorkflowStatus"
    TYPE = "Type"
    RESOURCE_ID = "ResourceId"
    AWS_ACCOUNT_ID = "AwsAccountId"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "product_arn": "ProductArn",
        "source_url": "SourceUrl",
        "resource_details_other": "ResourceDetailsOther",
        "description": "Description",
        "product_name": "ProductName",
        "resource_tags": "ResourceTags",
        "first_observed_at": "FirstObservedAt",
        "created_at": "CreatedAt",
        "note_text": "NoteText",
        "last_observed_at": "LastObservedAt",
        "user_defined_fields": "UserDefinedFields",
        "note_updated_at": "NoteUpdatedAt",
        "compliance_security_control_id": "ComplianceSecurityControlId",
        "company_name": "CompanyName",
        "resource_region": "ResourceRegion",
        "note_updated_by": "NoteUpdatedBy",
        "confidence": "Confidence",
        "resource_partition": "ResourcePartition",
        "verification_state": "VerificationState",
        "criticality": "Criticality",
        "severity_label": "SeverityLabel",
        "related_findings_product_arn": "RelatedFindingsProductArn",
        "compliance_status": "ComplianceStatus",
        "generator_id": "GeneratorId",
        "record_state": "RecordState",
        "title": "Title",
        "resource_type": "ResourceType",
        "compliance_associated_standards_id": "ComplianceAssociatedStandardsId",
        "updated_at": "UpdatedAt",
        "related_findings_id": "RelatedFindingsId",
        "workflow_status": "WorkflowStatus",
        "type_": "Type",
        "resource_id": "ResourceId",
        "aws_account_id": "AwsAccountId",
        "id": "Id",
    }

    product_arn: Optional[list[StringFilter]] = None
    source_url: Optional[list[StringFilter]] = None
    resource_details_other: Optional[list[MapFilter]] = None
    description: Optional[list[StringFilter]] = None
    product_name: Optional[list[StringFilter]] = None
    resource_tags: Optional[list[MapFilter]] = None
    first_observed_at: Optional[list[DateFilter]] = None
    created_at: Optional[list[DateFilter]] = None
    note_text: Optional[list[StringFilter]] = None
    last_observed_at: Optional[list[DateFilter]] = None
    user_defined_fields: Optional[list[MapFilter]] = None
    note_updated_at: Optional[list[DateFilter]] = None
    compliance_security_control_id: Optional[list[StringFilter]] = None
    company_name: Optional[list[StringFilter]] = None
    resource_region: Optional[list[StringFilter]] = None
    note_updated_by: Optional[list[StringFilter]] = None
    confidence: Optional[list[NumberFilter]] = None
    resource_partition: Optional[list[StringFilter]] = None
    verification_state: Optional[list[StringFilter]] = None
    criticality: Optional[list[NumberFilter]] = None
    severity_label: Optional[list[StringFilter]] = None
    related_findings_product_arn: Optional[list[StringFilter]] = None
    compliance_status: Optional[list[StringFilter]] = None
    generator_id: Optional[list[StringFilter]] = None
    record_state: Optional[list[StringFilter]] = None
    title: Optional[list[StringFilter]] = None
    resource_type: Optional[list[StringFilter]] = None
    compliance_associated_standards_id: Optional[list[StringFilter]] = None
    updated_at: Optional[list[DateFilter]] = None
    related_findings_id: Optional[list[StringFilter]] = None
    workflow_status: Optional[list[StringFilter]] = None
    type_: Optional[list[StringFilter]] = None
    resource_id: Optional[list[StringFilter]] = None
    aws_account_id: Optional[list[StringFilter]] = None
    id: Optional[list[StringFilter]] = None


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
class NoteUpdate(PropertyType):
    UPDATED_BY = "UpdatedBy"
    TEXT = "Text"

    _property_mappings: ClassVar[dict[str, str]] = {
        "updated_by": "UpdatedBy",
        "text": "Text",
    }

    updated_by: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None


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
class RelatedFinding(PropertyType):
    PRODUCT_ARN = "ProductArn"
    ID = "Id"

    _property_mappings: ClassVar[dict[str, str]] = {
        "product_arn": "ProductArn",
        "id": "Id",
    }

    product_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    id: Optional[Union[dict[str, Any], Ref, GetAtt, Sub]] = None


@dataclass
class SeverityUpdate(PropertyType):
    NORMALIZED = "Normalized"
    LABEL = "Label"
    PRODUCT = "Product"

    _property_mappings: ClassVar[dict[str, str]] = {
        "normalized": "Normalized",
        "label": "Label",
        "product": "Product",
    }

    normalized: Optional[Union[int, Ref, GetAtt, Sub]] = None
    label: Optional[Union[str, SeverityLabel, Ref, GetAtt, Sub]] = None
    product: Optional[Union[float, Ref, GetAtt, Sub]] = None


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


@dataclass
class WorkflowUpdate(PropertyType):
    STATUS = "Status"

    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
    }

    status: Optional[Union[str, WorkflowStatus, Ref, GetAtt, Sub]] = None

