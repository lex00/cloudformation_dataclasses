"""DeliveryStream - AWS::KinesisFirehose::DeliveryStream resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DeliveryStream:
    """AWS::KinesisFirehose::DeliveryStream resource."""

    resource: kinesisfirehose.DeliveryStream
    delivery_stream_name = ref(DeliveryStreamName)
    delivery_stream_type = 'DirectPut'
    delivery_stream_encryption_configuration_input = {
        'KeyType': 'AWS_OWNED_CMK',
    }
    extended_s3_destination_configuration = {
        'CloudWatchLoggingOptions': {
            'Enabled': True,
            'LogGroupName': ref(FirehoseLogGroup),
            'LogStreamName': ref(FirehoseLogStream),
        },
        'RoleARN': get_att(DeliveryRole, "Arn"),
        'BucketARN': Join('', [
    'arn:aws:s3:::',
    ref(DestinationBucketName),
]),
        'ErrorOutputPrefix': 'errors/',
        'ProcessingConfiguration': {
            'Enabled': True,
            'Processors': [{
                'Type': 'AppendDelimiterToRecord',
                'Parameters': [{
                    'ParameterName': 'Delimiter',
                    'ParameterValue': '\\n',
                }],
            }],
        },
    }
