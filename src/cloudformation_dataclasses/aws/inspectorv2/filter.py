"""PropertyTypes for AWS::InspectorV2::Filter."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DateFilter(PropertyType):
    END_INCLUSIVE = "EndInclusive"
    START_INCLUSIVE = "StartInclusive"

    _property_mappings: ClassVar[dict[str, str]] = {
        "end_inclusive": "EndInclusive",
        "start_inclusive": "StartInclusive",
    }

    end_inclusive: Optional[Union[int, Ref, GetAtt, Sub]] = None
    start_inclusive: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class FilterCriteria(PropertyType):
    RESOURCE_TAGS = "ResourceTags"
    EC2_INSTANCE_IMAGE_ID = "Ec2InstanceImageId"
    FIRST_OBSERVED_AT = "FirstObservedAt"
    INSPECTOR_SCORE = "InspectorScore"
    EC2_INSTANCE_VPC_ID = "Ec2InstanceVpcId"
    LAMBDA_FUNCTION_NAME = "LambdaFunctionName"
    LAMBDA_FUNCTION_RUNTIME = "LambdaFunctionRuntime"
    LAST_OBSERVED_AT = "LastObservedAt"
    ECR_IMAGE_PUSHED_AT = "EcrImagePushedAt"
    LAMBDA_FUNCTION_LAYERS = "LambdaFunctionLayers"
    FIX_AVAILABLE = "FixAvailable"
    EXPLOIT_AVAILABLE = "ExploitAvailable"
    ECR_IMAGE_ARCHITECTURE = "EcrImageArchitecture"
    RELATED_VULNERABILITIES = "RelatedVulnerabilities"
    ECR_IMAGE_TAGS = "EcrImageTags"
    VULNERABILITY_ID = "VulnerabilityId"
    COMPONENT_TYPE = "ComponentType"
    LAMBDA_FUNCTION_EXECUTION_ROLE_ARN = "LambdaFunctionExecutionRoleArn"
    VENDOR_SEVERITY = "VendorSeverity"
    CODE_VULNERABILITY_DETECTOR_TAGS = "CodeVulnerabilityDetectorTags"
    CODE_VULNERABILITY_DETECTOR_NAME = "CodeVulnerabilityDetectorName"
    ECR_IMAGE_REPOSITORY_NAME = "EcrImageRepositoryName"
    TITLE = "Title"
    RESOURCE_TYPE = "ResourceType"
    SEVERITY = "Severity"
    NETWORK_PROTOCOL = "NetworkProtocol"
    UPDATED_AT = "UpdatedAt"
    CODE_VULNERABILITY_FILE_PATH = "CodeVulnerabilityFilePath"
    ECR_IMAGE_HASH = "EcrImageHash"
    LAMBDA_FUNCTION_LAST_MODIFIED_AT = "LambdaFunctionLastModifiedAt"
    PORT_RANGE = "PortRange"
    VULNERABILITY_SOURCE = "VulnerabilitySource"
    EC2_INSTANCE_SUBNET_ID = "Ec2InstanceSubnetId"
    FINDING_ARN = "FindingArn"
    RESOURCE_ID = "ResourceId"
    FINDING_STATUS = "FindingStatus"
    VULNERABLE_PACKAGES = "VulnerablePackages"
    AWS_ACCOUNT_ID = "AwsAccountId"
    EPSS_SCORE = "EpssScore"
    COMPONENT_ID = "ComponentId"
    ECR_IMAGE_REGISTRY = "EcrImageRegistry"
    FINDING_TYPE = "FindingType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_tags": "ResourceTags",
        "ec2_instance_image_id": "Ec2InstanceImageId",
        "first_observed_at": "FirstObservedAt",
        "inspector_score": "InspectorScore",
        "ec2_instance_vpc_id": "Ec2InstanceVpcId",
        "lambda_function_name": "LambdaFunctionName",
        "lambda_function_runtime": "LambdaFunctionRuntime",
        "last_observed_at": "LastObservedAt",
        "ecr_image_pushed_at": "EcrImagePushedAt",
        "lambda_function_layers": "LambdaFunctionLayers",
        "fix_available": "FixAvailable",
        "exploit_available": "ExploitAvailable",
        "ecr_image_architecture": "EcrImageArchitecture",
        "related_vulnerabilities": "RelatedVulnerabilities",
        "ecr_image_tags": "EcrImageTags",
        "vulnerability_id": "VulnerabilityId",
        "component_type": "ComponentType",
        "lambda_function_execution_role_arn": "LambdaFunctionExecutionRoleArn",
        "vendor_severity": "VendorSeverity",
        "code_vulnerability_detector_tags": "CodeVulnerabilityDetectorTags",
        "code_vulnerability_detector_name": "CodeVulnerabilityDetectorName",
        "ecr_image_repository_name": "EcrImageRepositoryName",
        "title": "Title",
        "resource_type": "ResourceType",
        "severity": "Severity",
        "network_protocol": "NetworkProtocol",
        "updated_at": "UpdatedAt",
        "code_vulnerability_file_path": "CodeVulnerabilityFilePath",
        "ecr_image_hash": "EcrImageHash",
        "lambda_function_last_modified_at": "LambdaFunctionLastModifiedAt",
        "port_range": "PortRange",
        "vulnerability_source": "VulnerabilitySource",
        "ec2_instance_subnet_id": "Ec2InstanceSubnetId",
        "finding_arn": "FindingArn",
        "resource_id": "ResourceId",
        "finding_status": "FindingStatus",
        "vulnerable_packages": "VulnerablePackages",
        "aws_account_id": "AwsAccountId",
        "epss_score": "EpssScore",
        "component_id": "ComponentId",
        "ecr_image_registry": "EcrImageRegistry",
        "finding_type": "FindingType",
    }

    resource_tags: Optional[list[MapFilter]] = None
    ec2_instance_image_id: Optional[list[StringFilter]] = None
    first_observed_at: Optional[list[DateFilter]] = None
    inspector_score: Optional[list[NumberFilter]] = None
    ec2_instance_vpc_id: Optional[list[StringFilter]] = None
    lambda_function_name: Optional[list[StringFilter]] = None
    lambda_function_runtime: Optional[list[StringFilter]] = None
    last_observed_at: Optional[list[DateFilter]] = None
    ecr_image_pushed_at: Optional[list[DateFilter]] = None
    lambda_function_layers: Optional[list[StringFilter]] = None
    fix_available: Optional[list[StringFilter]] = None
    exploit_available: Optional[list[StringFilter]] = None
    ecr_image_architecture: Optional[list[StringFilter]] = None
    related_vulnerabilities: Optional[list[StringFilter]] = None
    ecr_image_tags: Optional[list[StringFilter]] = None
    vulnerability_id: Optional[list[StringFilter]] = None
    component_type: Optional[list[StringFilter]] = None
    lambda_function_execution_role_arn: Optional[list[StringFilter]] = None
    vendor_severity: Optional[list[StringFilter]] = None
    code_vulnerability_detector_tags: Optional[list[StringFilter]] = None
    code_vulnerability_detector_name: Optional[list[StringFilter]] = None
    ecr_image_repository_name: Optional[list[StringFilter]] = None
    title: Optional[list[StringFilter]] = None
    resource_type: Optional[list[StringFilter]] = None
    severity: Optional[list[StringFilter]] = None
    network_protocol: Optional[list[StringFilter]] = None
    updated_at: Optional[list[DateFilter]] = None
    code_vulnerability_file_path: Optional[list[StringFilter]] = None
    ecr_image_hash: Optional[list[StringFilter]] = None
    lambda_function_last_modified_at: Optional[list[DateFilter]] = None
    port_range: Optional[list[PortRangeFilter]] = None
    vulnerability_source: Optional[list[StringFilter]] = None
    ec2_instance_subnet_id: Optional[list[StringFilter]] = None
    finding_arn: Optional[list[StringFilter]] = None
    resource_id: Optional[list[StringFilter]] = None
    finding_status: Optional[list[StringFilter]] = None
    vulnerable_packages: Optional[list[PackageFilter]] = None
    aws_account_id: Optional[list[StringFilter]] = None
    epss_score: Optional[list[NumberFilter]] = None
    component_id: Optional[list[StringFilter]] = None
    ecr_image_registry: Optional[list[StringFilter]] = None
    finding_type: Optional[list[StringFilter]] = None


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

    comparison: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class NumberFilter(PropertyType):
    LOWER_INCLUSIVE = "LowerInclusive"
    UPPER_INCLUSIVE = "UpperInclusive"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lower_inclusive": "LowerInclusive",
        "upper_inclusive": "UpperInclusive",
    }

    lower_inclusive: Optional[Union[float, Ref, GetAtt, Sub]] = None
    upper_inclusive: Optional[Union[float, Ref, GetAtt, Sub]] = None


@dataclass
class PackageFilter(PropertyType):
    FILE_PATH = "FilePath"
    ARCHITECTURE = "Architecture"
    VERSION = "Version"
    EPOCH = "Epoch"
    SOURCE_LAYER_HASH = "SourceLayerHash"
    SOURCE_LAMBDA_LAYER_ARN = "SourceLambdaLayerArn"
    RELEASE = "Release"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "file_path": "FilePath",
        "architecture": "Architecture",
        "version": "Version",
        "epoch": "Epoch",
        "source_layer_hash": "SourceLayerHash",
        "source_lambda_layer_arn": "SourceLambdaLayerArn",
        "release": "Release",
        "name": "Name",
    }

    file_path: Optional[StringFilter] = None
    architecture: Optional[StringFilter] = None
    version: Optional[StringFilter] = None
    epoch: Optional[NumberFilter] = None
    source_layer_hash: Optional[StringFilter] = None
    source_lambda_layer_arn: Optional[StringFilter] = None
    release: Optional[StringFilter] = None
    name: Optional[StringFilter] = None


@dataclass
class PortRangeFilter(PropertyType):
    BEGIN_INCLUSIVE = "BeginInclusive"
    END_INCLUSIVE = "EndInclusive"

    _property_mappings: ClassVar[dict[str, str]] = {
        "begin_inclusive": "BeginInclusive",
        "end_inclusive": "EndInclusive",
    }

    begin_inclusive: Optional[Union[int, Ref, GetAtt, Sub]] = None
    end_inclusive: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StringFilter(PropertyType):
    COMPARISON = "Comparison"
    VALUE = "Value"

    _property_mappings: ClassVar[dict[str, str]] = {
        "comparison": "Comparison",
        "value": "Value",
    }

    comparison: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None

