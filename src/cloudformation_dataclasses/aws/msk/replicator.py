"""PropertyTypes for AWS::MSK::Replicator."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AmazonMskCluster(PropertyType):
    MSK_CLUSTER_ARN = "MskClusterArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "msk_cluster_arn": "MskClusterArn",
    }

    msk_cluster_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ConsumerGroupReplication(PropertyType):
    CONSUMER_GROUPS_TO_REPLICATE = "ConsumerGroupsToReplicate"
    CONSUMER_GROUPS_TO_EXCLUDE = "ConsumerGroupsToExclude"
    SYNCHRONISE_CONSUMER_GROUP_OFFSETS = "SynchroniseConsumerGroupOffsets"
    DETECT_AND_COPY_NEW_CONSUMER_GROUPS = "DetectAndCopyNewConsumerGroups"

    _property_mappings: ClassVar[dict[str, str]] = {
        "consumer_groups_to_replicate": "ConsumerGroupsToReplicate",
        "consumer_groups_to_exclude": "ConsumerGroupsToExclude",
        "synchronise_consumer_group_offsets": "SynchroniseConsumerGroupOffsets",
        "detect_and_copy_new_consumer_groups": "DetectAndCopyNewConsumerGroups",
    }

    consumer_groups_to_replicate: Optional[Union[list[str], Ref]] = None
    consumer_groups_to_exclude: Optional[Union[list[str], Ref]] = None
    synchronise_consumer_group_offsets: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    detect_and_copy_new_consumer_groups: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class KafkaCluster(PropertyType):
    VPC_CONFIG = "VpcConfig"
    AMAZON_MSK_CLUSTER = "AmazonMskCluster"

    _property_mappings: ClassVar[dict[str, str]] = {
        "vpc_config": "VpcConfig",
        "amazon_msk_cluster": "AmazonMskCluster",
    }

    vpc_config: Optional[KafkaClusterClientVpcConfig] = None
    amazon_msk_cluster: Optional[AmazonMskCluster] = None


@dataclass
class KafkaClusterClientVpcConfig(PropertyType):
    SECURITY_GROUP_IDS = "SecurityGroupIds"
    SUBNET_IDS = "SubnetIds"

    _property_mappings: ClassVar[dict[str, str]] = {
        "security_group_ids": "SecurityGroupIds",
        "subnet_ids": "SubnetIds",
    }

    security_group_ids: Optional[Union[list[str], Ref]] = None
    subnet_ids: Optional[Union[list[str], Ref]] = None


@dataclass
class ReplicationInfo(PropertyType):
    TARGET_COMPRESSION_TYPE = "TargetCompressionType"
    TOPIC_REPLICATION = "TopicReplication"
    CONSUMER_GROUP_REPLICATION = "ConsumerGroupReplication"
    SOURCE_KAFKA_CLUSTER_ARN = "SourceKafkaClusterArn"
    TARGET_KAFKA_CLUSTER_ARN = "TargetKafkaClusterArn"

    _property_mappings: ClassVar[dict[str, str]] = {
        "target_compression_type": "TargetCompressionType",
        "topic_replication": "TopicReplication",
        "consumer_group_replication": "ConsumerGroupReplication",
        "source_kafka_cluster_arn": "SourceKafkaClusterArn",
        "target_kafka_cluster_arn": "TargetKafkaClusterArn",
    }

    target_compression_type: Optional[Union[str, TargetCompressionType, Ref, GetAtt, Sub]] = None
    topic_replication: Optional[TopicReplication] = None
    consumer_group_replication: Optional[ConsumerGroupReplication] = None
    source_kafka_cluster_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    target_kafka_cluster_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationStartingPosition(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, ReplicationStartingPositionType, Ref, GetAtt, Sub]] = None


@dataclass
class ReplicationTopicNameConfiguration(PropertyType):
    TYPE = "Type"

    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
    }

    type_: Optional[Union[str, ReplicationTopicNameConfigurationType, Ref, GetAtt, Sub]] = None


@dataclass
class TopicReplication(PropertyType):
    STARTING_POSITION = "StartingPosition"
    TOPICS_TO_REPLICATE = "TopicsToReplicate"
    TOPICS_TO_EXCLUDE = "TopicsToExclude"
    TOPIC_NAME_CONFIGURATION = "TopicNameConfiguration"
    COPY_TOPIC_CONFIGURATIONS = "CopyTopicConfigurations"
    DETECT_AND_COPY_NEW_TOPICS = "DetectAndCopyNewTopics"
    COPY_ACCESS_CONTROL_LISTS_FOR_TOPICS = "CopyAccessControlListsForTopics"

    _property_mappings: ClassVar[dict[str, str]] = {
        "starting_position": "StartingPosition",
        "topics_to_replicate": "TopicsToReplicate",
        "topics_to_exclude": "TopicsToExclude",
        "topic_name_configuration": "TopicNameConfiguration",
        "copy_topic_configurations": "CopyTopicConfigurations",
        "detect_and_copy_new_topics": "DetectAndCopyNewTopics",
        "copy_access_control_lists_for_topics": "CopyAccessControlListsForTopics",
    }

    starting_position: Optional[ReplicationStartingPosition] = None
    topics_to_replicate: Optional[Union[list[str], Ref]] = None
    topics_to_exclude: Optional[Union[list[str], Ref]] = None
    topic_name_configuration: Optional[ReplicationTopicNameConfiguration] = None
    copy_topic_configurations: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    detect_and_copy_new_topics: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    copy_access_control_lists_for_topics: Optional[Union[bool, Ref, GetAtt, Sub]] = None

