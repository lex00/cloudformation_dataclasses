from __future__ import annotations

"""DeliveryStream - AWS::KinesisFirehose::DeliveryStream resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DeliveryStreamDeliveryStreamEncryptionConfigurationInput:
    resource: DeliveryStreamEncryptionConfigurationInput
    key_type = 'AWS_OWNED_CMK'


@cloudformation_dataclass
class DeliveryStreamCloudWatchLoggingOptions:
    resource: CloudWatchLoggingOptions
    enabled = True
    log_group_name = ref(FirehoseLogGroup)
    log_stream_name = ref(FirehoseLogStream)


@cloudformation_dataclass
class DeliveryStreamProcessorParameter:
    resource: ProcessorParameter
    parameter_name = 'Delimiter'
    parameter_value = '\\n'


@cloudformation_dataclass
class DeliveryStreamProcessor:
    resource: Processor
    type_ = 'AppendDelimiterToRecord'
    parameters = [DeliveryStreamProcessorParameter]


@cloudformation_dataclass
class DeliveryStreamProcessingConfiguration:
    resource: ProcessingConfiguration
    enabled = True
    processors = [DeliveryStreamProcessor]


@cloudformation_dataclass
class DeliveryStreamExtendedS3DestinationConfiguration:
    resource: ExtendedS3DestinationConfiguration
    cloud_watch_logging_options = DeliveryStreamCloudWatchLoggingOptions
    role_arn = get_att(DeliveryRole, "Arn")
    bucket_arn = Join('', [
    'arn:aws:s3:::',
    ref(DestinationBucketName),
])
    error_output_prefix = 'errors/'
    processing_configuration = DeliveryStreamProcessingConfiguration


@cloudformation_dataclass
class DeliveryStream:
    """AWS::KinesisFirehose::DeliveryStream resource."""

    resource: kinesisfirehose.DeliveryStream
    delivery_stream_name = ref(DeliveryStreamName)
    delivery_stream_type = 'DirectPut'
    delivery_stream_encryption_configuration_input = DeliveryStreamDeliveryStreamEncryptionConfigurationInput
    extended_s3_destination_configuration = DeliveryStreamExtendedS3DestinationConfiguration
