"""DynamoDBInputS3OutputHive - AWS::DataPipeline::Pipeline resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DynamoDBInputS3OutputHive:
    """AWS::DataPipeline::Pipeline resource."""

    resource: datapipeline.Pipeline
    name = 'DynamoDBInputS3OutputHive'
    description = 'Pipeline to backup DynamoDB data to S3'
    activate = 'true'
    pipeline_objects = [{
        'Id': 'ResourceId_I1mCc',
        'Name': 'ReleaseLabelCluster',
        'Fields': [
            {
                'Key': 'releaseLabel',
                'StringValue': 'emr-4.1.0',
            },
            {
                'Key': 'applications',
                'StringValue': 'spark',
            },
            {
                'Key': 'applications',
                'StringValue': 'hive',
            },
            {
                'Key': 'applications',
                'StringValue': 'pig',
            },
            {
                'Key': 'type',
                'StringValue': 'EmrCluster',
            },
            {
                'Key': 'configuration',
                'RefValue': 'coresite',
            },
        ],
    }, {
        'Id': 'coresite',
        'Name': 'coresite',
        'Fields': [
            {
                'Key': 'type',
                'StringValue': 'EmrConfiguration',
            },
            {
                'Key': 'classification',
                'StringValue': 'core-site',
            },
            {
                'Key': 'property',
                'RefValue': 'io-file-buffer-size',
            },
            {
                'Key': 'property',
                'RefValue': 'fs-s3-block-size',
            },
        ],
    }, {
        'Id': 'io-file-buffer-size',
        'Name': 'io-file-buffer-size',
        'Fields': [
            {
                'Key': 'type',
                'StringValue': 'Property',
            },
            {
                'Key': 'value',
                'StringValue': '4096',
            },
            {
                'Key': 'key',
                'StringValue': 'io.file.buffer.size',
            },
        ],
    }, {
        'Id': 'fs-s3-block-size',
        'Name': 'fs-s3-block-size',
        'Fields': [
            {
                'Key': 'type',
                'StringValue': 'Property',
            },
            {
                'Key': 'value',
                'StringValue': '67108864',
            },
            {
                'Key': 'key',
                'StringValue': 'fs.s3.block.size',
            },
        ],
    }, {
        'Id': 'DefaultSchedule',
        'Name': 'RunOnce',
        'Fields': [
            {
                'Key': 'occurrences',
                'StringValue': '1',
            },
            {
                'Key': 'startAt',
                'StringValue': 'FIRST_ACTIVATION_DATE_TIME',
            },
            {
                'Key': 'type',
                'StringValue': 'Schedule',
            },
            {
                'Key': 'period',
                'StringValue': '1 Day',
            },
        ],
    }, {
        'Id': 'Default',
        'Name': 'Default',
        'Fields': [
            {
                'Key': 'resourceRole',
                'StringValue': 'DataPipelineDefaultResourceRole',
            },
            {
                'Key': 'role',
                'StringValue': 'DataPipelineDefaultRole',
            },
            {
                'Key': 'scheduleType',
                'StringValue': 'cron',
            },
            {
                'Key': 'type',
                'StringValue': 'Default',
            },
            {
                'Key': 'schedule',
                'RefValue': 'DefaultSchedule',
            },
        ],
    }]
