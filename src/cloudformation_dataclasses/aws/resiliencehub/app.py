"""PropertyTypes for AWS::ResilienceHub::App."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


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

