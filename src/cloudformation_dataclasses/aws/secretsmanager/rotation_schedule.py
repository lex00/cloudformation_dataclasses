"""PropertyTypes for AWS::SecretsManager::RotationSchedule."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ExternalSecretRotationMetadataItem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HostedRotationLambda(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "runtime": "Runtime",
        "kms_key_arn": "KmsKeyArn",
        "master_secret_arn": "MasterSecretArn",
        "rotation_lambda_name": "RotationLambdaName",
        "rotation_type": "RotationType",
        "exclude_characters": "ExcludeCharacters",
        "vpc_security_group_ids": "VpcSecurityGroupIds",
        "master_secret_kms_key_arn": "MasterSecretKmsKeyArn",
        "superuser_secret_arn": "SuperuserSecretArn",
        "superuser_secret_kms_key_arn": "SuperuserSecretKmsKeyArn",
        "vpc_subnet_ids": "VpcSubnetIds",
    }

    runtime: Optional[Union[str, Ref, GetAtt, Sub]] = None
    kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    master_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rotation_lambda_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    rotation_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    exclude_characters: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_security_group_ids: Optional[Union[str, Ref, GetAtt, Sub]] = None
    master_secret_kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    superuser_secret_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    superuser_secret_kms_key_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_subnet_ids: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RotationRules(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "schedule_expression": "ScheduleExpression",
        "duration": "Duration",
        "automatically_after_days": "AutomaticallyAfterDays",
    }

    schedule_expression: Optional[Union[str, Ref, GetAtt, Sub]] = None
    duration: Optional[Union[str, Ref, GetAtt, Sub]] = None
    automatically_after_days: Optional[Union[int, Ref, GetAtt, Sub]] = None

