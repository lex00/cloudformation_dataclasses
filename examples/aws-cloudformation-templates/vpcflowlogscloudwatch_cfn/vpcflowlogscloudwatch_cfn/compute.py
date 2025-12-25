"""Compute resources: VPCFlowLogsToCloudWatch."""

from . import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsToCloudWatchAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'VPC Flow Logs CloudWatch'


@cloudformation_dataclass
class VPCFlowLogsToCloudWatch:
    """AWS::EC2::FlowLog resource."""

    resource: ec2.FlowLog
    log_destination_type = 'cloud-watch-logs'
    log_group_name = ref(VPCFlowLogsLogGroup)
    deliver_logs_permission_arn = get_att(VPCFlowLogsRole, "Arn")
    log_format = ref(VPCFlowLogsLogFormat)
    max_aggregation_interval = ref(VPCFlowLogsMaxAggregationInterval)
    resource_id = ref(VPCID)
    resource_type = 'VPC'
    traffic_type = ref(VPCFlowLogsTrafficType)
    tags = [VPCFlowLogsToCloudWatchAssociationParameter]
