"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField:
    resource: datapipeline.pipeline.Field
    key = 'releaseLabel'
    string_value = 'emr-4.1.0'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField1:
    resource: datapipeline.pipeline.Field
    key = 'applications'
    string_value = 'spark'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField2:
    resource: datapipeline.pipeline.Field
    key = 'applications'
    string_value = 'hive'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField3:
    resource: datapipeline.pipeline.Field
    key = 'applications'
    string_value = 'pig'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField4:
    resource: datapipeline.pipeline.Field
    key = 'type'
    string_value = 'EmrCluster'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField5:
    resource: datapipeline.pipeline.Field
    key = 'configuration'
    ref_value = 'coresite'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject:
    resource: datapipeline.pipeline.PipelineObject
    id = 'ResourceId_I1mCc'
    name = 'ReleaseLabelCluster'
    fields = [DynamoDBInputS3OutputHiveField, DynamoDBInputS3OutputHiveField1, DynamoDBInputS3OutputHiveField2, DynamoDBInputS3OutputHiveField3, DynamoDBInputS3OutputHiveField4, DynamoDBInputS3OutputHiveField5]


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField6:
    resource: datapipeline.pipeline.Field
    key = 'type'
    string_value = 'EmrConfiguration'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField7:
    resource: datapipeline.pipeline.Field
    key = 'classification'
    string_value = 'core-site'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField8:
    resource: datapipeline.pipeline.Field
    key = 'property'
    ref_value = 'io-file-buffer-size'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField9:
    resource: datapipeline.pipeline.Field
    key = 'property'
    ref_value = 'fs-s3-block-size'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject1:
    resource: datapipeline.pipeline.PipelineObject
    id = 'coresite'
    name = 'coresite'
    fields = [DynamoDBInputS3OutputHiveField6, DynamoDBInputS3OutputHiveField7, DynamoDBInputS3OutputHiveField8, DynamoDBInputS3OutputHiveField9]


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField10:
    resource: datapipeline.pipeline.Field
    key = 'type'
    string_value = 'Property'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField11:
    resource: datapipeline.pipeline.Field
    key = 'value'
    string_value = '4096'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField12:
    resource: datapipeline.pipeline.Field
    key = 'key'
    string_value = 'io.file.buffer.size'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject2:
    resource: datapipeline.pipeline.PipelineObject
    id = 'io-file-buffer-size'
    name = 'io-file-buffer-size'
    fields = [DynamoDBInputS3OutputHiveField10, DynamoDBInputS3OutputHiveField11, DynamoDBInputS3OutputHiveField12]


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField13:
    resource: datapipeline.pipeline.Field
    key = 'type'
    string_value = 'Property'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField14:
    resource: datapipeline.pipeline.Field
    key = 'value'
    string_value = '67108864'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField15:
    resource: datapipeline.pipeline.Field
    key = 'key'
    string_value = 'fs.s3.block.size'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject3:
    resource: datapipeline.pipeline.PipelineObject
    id = 'fs-s3-block-size'
    name = 'fs-s3-block-size'
    fields = [DynamoDBInputS3OutputHiveField13, DynamoDBInputS3OutputHiveField14, DynamoDBInputS3OutputHiveField15]


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField16:
    resource: datapipeline.pipeline.Field
    key = 'occurrences'
    string_value = '1'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField17:
    resource: datapipeline.pipeline.Field
    key = 'startAt'
    string_value = 'FIRST_ACTIVATION_DATE_TIME'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField18:
    resource: datapipeline.pipeline.Field
    key = 'type'
    string_value = 'Schedule'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField19:
    resource: datapipeline.pipeline.Field
    key = 'period'
    string_value = '1 Day'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject4:
    resource: datapipeline.pipeline.PipelineObject
    id = 'DefaultSchedule'
    name = 'RunOnce'
    fields = [DynamoDBInputS3OutputHiveField16, DynamoDBInputS3OutputHiveField17, DynamoDBInputS3OutputHiveField18, DynamoDBInputS3OutputHiveField19]


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField20:
    resource: datapipeline.pipeline.Field
    key = 'resourceRole'
    string_value = 'DataPipelineDefaultResourceRole'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField21:
    resource: datapipeline.pipeline.Field
    key = 'role'
    string_value = 'DataPipelineDefaultRole'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField22:
    resource: datapipeline.pipeline.Field
    key = 'scheduleType'
    string_value = 'cron'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField23:
    resource: datapipeline.pipeline.Field
    key = 'type'
    string_value = 'Default'


@cloudformation_dataclass
class DynamoDBInputS3OutputHiveField24:
    resource: datapipeline.pipeline.Field
    key = 'schedule'
    ref_value = 'DefaultSchedule'


@cloudformation_dataclass
class DynamoDBInputS3OutputHivePipelineObject5:
    resource: datapipeline.pipeline.PipelineObject
    id = 'Default'
    name = 'Default'
    fields = [DynamoDBInputS3OutputHiveField20, DynamoDBInputS3OutputHiveField21, DynamoDBInputS3OutputHiveField22, DynamoDBInputS3OutputHiveField23, DynamoDBInputS3OutputHiveField24]


@cloudformation_dataclass
class DynamoDBInputS3OutputHive:
    """AWS::DataPipeline::Pipeline resource."""

    resource: datapipeline.Pipeline
    name = 'DynamoDBInputS3OutputHive'
    description = 'Pipeline to backup DynamoDB data to S3'
    activate = 'true'
    pipeline_objects = [DynamoDBInputS3OutputHivePipelineObject, DynamoDBInputS3OutputHivePipelineObject1, DynamoDBInputS3OutputHivePipelineObject2, DynamoDBInputS3OutputHivePipelineObject3, DynamoDBInputS3OutputHivePipelineObject4, DynamoDBInputS3OutputHivePipelineObject5]
