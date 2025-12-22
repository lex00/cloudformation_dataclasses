"""VPCFlowLogstoS3 - AWS::EC2::FlowLog resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogstoS3AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'VPC Flow Logs S3'


@cloudformation_dataclass
class VPCFlowLogstoS3:
    """AWS::EC2::FlowLog resource."""

    resource: FlowLog
    log_destination_type = 's3'
    log_destination = If("VPCFlowLogsNewBucketCondition", get_att(VPCFlowLogsBucket, "Arn"), Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucketName}'))
    log_format = ref(VPCFlowLogsLogFormat)
    max_aggregation_interval = ref(VPCFlowLogsMaxAggregationInterval)
    resource_id = ref(VPCID)
    resource_type = 'VPC'
    traffic_type = ref(VPCFlowLogsTrafficType)
    tags = [VPCFlowLogstoS3AssociationParameter]
