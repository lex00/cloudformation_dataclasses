"""PropertyTypes for AWS::AppTest::TestCase."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Batch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "batch_job_name": "BatchJobName",
        "export_data_set_names": "ExportDataSetNames",
        "batch_job_parameters": "BatchJobParameters",
    }

    batch_job_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    export_data_set_names: Optional[Union[list[str], Ref]] = None
    batch_job_parameters: Optional[dict[str, str]] = None


@dataclass
class CloudFormationAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action_type": "ActionType",
        "resource": "Resource",
    }

    action_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class CompareAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input": "Input",
        "output": "Output",
    }

    input: Optional[Input] = None
    output: Optional[Output] = None


@dataclass
class DataSet(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ccsid": "Ccsid",
        "type_": "Type",
        "format": "Format",
        "length": "Length",
        "name": "Name",
    }

    ccsid: Optional[Union[str, Ref, GetAtt, Sub]] = None
    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    format: Optional[Union[str, Ref, GetAtt, Sub]] = None
    length: Optional[Union[float, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DatabaseCDC(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_metadata": "SourceMetadata",
        "target_metadata": "TargetMetadata",
    }

    source_metadata: Optional[SourceDatabaseMetadata] = None
    target_metadata: Optional[TargetDatabaseMetadata] = None


@dataclass
class FileMetadata(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "database_cdc": "DatabaseCDC",
        "data_sets": "DataSets",
    }

    database_cdc: Optional[DatabaseCDC] = None
    data_sets: Optional[list[DataSet]] = None


@dataclass
class Input(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file": "File",
    }

    file: Optional[InputFile] = None


@dataclass
class InputFile(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_location": "SourceLocation",
        "target_location": "TargetLocation",
        "file_metadata": "FileMetadata",
    }

    source_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_metadata: Optional[FileMetadata] = None


@dataclass
class M2ManagedActionProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "import_data_set_location": "ImportDataSetLocation",
        "force_stop": "ForceStop",
    }

    import_data_set_location: Optional[Union[str, Ref, GetAtt, Sub]] = None
    force_stop: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class M2ManagedApplicationAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action_type": "ActionType",
        "resource": "Resource",
        "properties": "Properties",
    }

    action_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource: Optional[Union[str, Ref, GetAtt, Sub]] = None
    properties: Optional[M2ManagedActionProperties] = None


@dataclass
class M2NonManagedApplicationAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action_type": "ActionType",
        "resource": "Resource",
    }

    action_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MainframeAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action_type": "ActionType",
        "resource": "Resource",
        "properties": "Properties",
    }

    action_type: Optional[MainframeActionType] = None
    resource: Optional[Union[str, Ref, GetAtt, Sub]] = None
    properties: Optional[MainframeActionProperties] = None


@dataclass
class MainframeActionProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dms_task_arn": "DmsTaskArn",
    }

    dms_task_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class MainframeActionType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "batch": "Batch",
        "tn3270": "Tn3270",
    }

    batch: Optional[Batch] = None
    tn3270: Optional[TN3270] = None


@dataclass
class Output(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file": "File",
    }

    file: Optional[OutputFile] = None


@dataclass
class OutputFile(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "file_location": "FileLocation",
    }

    file_location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ResourceAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_formation_action": "CloudFormationAction",
        "m2_managed_application_action": "M2ManagedApplicationAction",
        "m2_non_managed_application_action": "M2NonManagedApplicationAction",
    }

    cloud_formation_action: Optional[CloudFormationAction] = None
    m2_managed_application_action: Optional[M2ManagedApplicationAction] = None
    m2_non_managed_application_action: Optional[M2NonManagedApplicationAction] = None


@dataclass
class Script(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "script_location": "ScriptLocation",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    script_location: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SourceDatabaseMetadata(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "capture_tool": "CaptureTool",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    capture_tool: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Step(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "description": "Description",
        "name": "Name",
    }

    action: Optional[StepAction] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class StepAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "compare_action": "CompareAction",
        "mainframe_action": "MainframeAction",
        "resource_action": "ResourceAction",
    }

    compare_action: Optional[CompareAction] = None
    mainframe_action: Optional[MainframeAction] = None
    resource_action: Optional[ResourceAction] = None


@dataclass
class TN3270(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "script": "Script",
        "export_data_set_names": "ExportDataSetNames",
    }

    script: Optional[Script] = None
    export_data_set_names: Optional[Union[list[str], Ref]] = None


@dataclass
class TargetDatabaseMetadata(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "capture_tool": "CaptureTool",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    capture_tool: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class TestCaseLatestVersion(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "status": "Status",
        "version": "Version",
    }

    status: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[float, Ref, GetAtt, Sub]] = None

