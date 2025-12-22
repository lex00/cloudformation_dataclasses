"""PropertyTypes for AWS::IoTCoreDeviceAdvisor::SuiteDefinition."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DeviceUnderTest(PropertyType):
    THING_ARN = "ThingArn"
    CERTIFICATE_ARN = "CertificateArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "thing_arn": "ThingArn",
        "certificate_arn": "CertificateArn",
    }

    thing_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    certificate_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SuiteDefinitionConfiguration(PropertyType):
    DEVICE_PERMISSION_ROLE_ARN = "DevicePermissionRoleArn"
    SUITE_DEFINITION_NAME = "SuiteDefinitionName"
    INTENDED_FOR_QUALIFICATION = "IntendedForQualification"
    DEVICES = "Devices"
    ROOT_GROUP = "RootGroup"

    _property_mappings: ClassVar[dict[str, str]] = {
        "device_permission_role_arn": "DevicePermissionRoleArn",
        "suite_definition_name": "SuiteDefinitionName",
        "intended_for_qualification": "IntendedForQualification",
        "devices": "Devices",
        "root_group": "RootGroup",
    }

    device_permission_role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    suite_definition_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    intended_for_qualification: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    devices: Optional[list[DeviceUnderTest]] = None
    root_group: Optional[Union[str, Ref, GetAtt, Sub]] = None

