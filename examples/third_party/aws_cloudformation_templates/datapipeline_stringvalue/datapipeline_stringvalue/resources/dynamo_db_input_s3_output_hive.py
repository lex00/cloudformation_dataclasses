from __future__ import annotations

"""DynamoDBInputS3OutputHive - AWS::DataPipeline::Pipeline resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField:
    resource: Field
    key = 'releaseLabel'
    string_value = 'emr-4.1.0'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField1:
    resource: Field
    key = 'applications'
    string_value = 'spark'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField2:
    resource: Field
    key = 'applications'
    string_value = 'hive'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField3:
    resource: Field
    key = 'applications'
    string_value = 'pig'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField4:
    resource: Field
    key = 'type'
    string_value = 'EmrCluster'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField5:
    resource: Field
    key = 'configuration'
    ref_value = 'coresite'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject:
    resource: PipelineObject
    id = 'ResourceId_I1mCc'
    name = 'ReleaseLabelCluster'
    fields = [DynamoDBInputS3OutputHiveField, DynamoDBInputS3OutputHiveField1, DynamoDBInputS3OutputHiveField2, DynamoDBInputS3OutputHiveField3, DynamoDBInputS3OutputHiveField4, DynamoDBInputS3OutputHiveField5]


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField6:
    resource: Field
    key = 'type'
    string_value = 'EmrConfiguration'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField7:
    resource: Field
    key = 'classification'
    string_value = 'core-site'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField8:
    resource: Field
    key = 'property'
    ref_value = 'io-file-buffer-size'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField9:
    resource: Field
    key = 'property'
    ref_value = 'fs-s3-block-size'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject1:
    resource: PipelineObject
    id = 'coresite'
    name = 'coresite'
    fields = [DynamoDBInputS3OutputHiveField6, DynamoDBInputS3OutputHiveField7, DynamoDBInputS3OutputHiveField8, DynamoDBInputS3OutputHiveField9]


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField10:
    resource: Field
    key = 'type'
    string_value = 'Property'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField11:
    resource: Field
    key = 'value'
    string_value = '4096'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField12:
    resource: Field
    key = 'key'
    string_value = 'io.file.buffer.size'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject2:
    resource: PipelineObject
    id = 'io-file-buffer-size'
    name = 'io-file-buffer-size'
    fields = [DynamoDBInputS3OutputHiveField10, DynamoDBInputS3OutputHiveField11, DynamoDBInputS3OutputHiveField12]


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField13:
    resource: Field
    key = 'type'
    string_value = 'Property'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField14:
    resource: Field
    key = 'value'
    string_value = '67108864'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField15:
    resource: Field
    key = 'key'
    string_value = 'fs.s3.block.size'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject3:
    resource: PipelineObject
    id = 'fs-s3-block-size'
    name = 'fs-s3-block-size'
    fields = [DynamoDBInputS3OutputHiveField13, DynamoDBInputS3OutputHiveField14, DynamoDBInputS3OutputHiveField15]


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField16:
    resource: Field
    key = 'occurrences'
    string_value = '1'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField17:
    resource: Field
    key = 'startAt'
    string_value = 'FIRST_ACTIVATION_DATE_TIME'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField18:
    resource: Field
    key = 'type'
    string_value = 'Schedule'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField19:
    resource: Field
    key = 'period'
    string_value = '1 Day'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject4:
    resource: PipelineObject
    id = 'DefaultSchedule'
    name = 'RunOnce'
    fields = [DynamoDBInputS3OutputHiveField16, DynamoDBInputS3OutputHiveField17, DynamoDBInputS3OutputHiveField18, DynamoDBInputS3OutputHiveField19]


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField20:
    resource: Field
    key = 'resourceRole'
    string_value = 'DataPipelineDefaultResourceRole'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField21:
    resource: Field
    key = 'role'
    string_value = 'DataPipelineDefaultRole'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField22:
    resource: Field
    key = 'scheduleType'
    string_value = 'cron'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField23:
    resource: Field
    key = 'type'
    string_value = 'Default'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField24:
    resource: Field
    key = 'schedule'
    ref_value = 'DefaultSchedule'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject5:
    resource: PipelineObject
    id = 'Default'
    name = 'Default'
    fields = [DynamoDBInputS3OutputHiveField20, DynamoDBInputS3OutputHiveField21, DynamoDBInputS3OutputHiveField22, DynamoDBInputS3OutputHiveField23, DynamoDBInputS3OutputHiveField24]


@cloudformation_dataclass
class DynamoDBInputS3OutputHive:
    """AWS::DataPipeline::Pipeline resource."""

    resource: Pipeline
    name = 'DynamoDBInputS3OutputHive'
    description = 'Pipeline to backup DynamoDB data to S3'
    activate = 'true'
    pipeline_objects = [DynamoDBInputS3OutputHivePipelineObject, DynamoDBInputS3OutputHivePipelineObject1, DynamoDBInputS3OutputHivePipelineObject2, DynamoDBInputS3OutputHivePipelineObject3, DynamoDBInputS3OutputHivePipelineObject4, DynamoDBInputS3OutputHivePipelineObject5]
