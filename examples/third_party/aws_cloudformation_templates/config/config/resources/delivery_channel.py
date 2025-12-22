from __future__ import annotations

"""DeliveryChannel - AWS::Config::DeliveryChannel resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DeliveryChannelConfigSnapshotDeliveryProperties:
    resource: ConfigSnapshotDeliveryProperties
    delivery_frequency = 'Six_Hours'


@cloudformation_dataclass
class DeliveryChannel:
    """AWS::Config::DeliveryChannel resource."""

    resource: config.DeliveryChannel
    config_snapshot_delivery_properties = DeliveryChannelConfigSnapshotDeliveryProperties
    s3_bucket_name = ref(ConfigBucket)
    sns_topic_arn = ref(ConfigTopic)
    condition = 'CreateDeliveryChannel'
