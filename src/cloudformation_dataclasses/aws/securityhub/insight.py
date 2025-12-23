"""PropertyTypes for AWS::SecurityHub::Insight."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AwsSecurityFindingFilters(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class DateFilter(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "unit": "Unit",
    }

    value: Optional[Union[float, Ref, GetAtt, Sub]] = None
    unit: Optional[Union[str, DateRangeUnit, Ref, GetAtt, Sub]] = None


@dataclass
class IpFilter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cidr": "Cidr",
    }

    cidr: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MapFilter(PropertyType):
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
    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison": "Comparison",
        "value": "Value",
    }

    comparison: Optional[Union[str, StringFilterComparison, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None

