from __future__ import annotations

"""VPCFlowLogsToCloudWatch - AWS::EC2::FlowLog resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsToCloudWatchAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'VPC Flow Logs CloudWatch'


@cloudformation_dataclass
class VPCFlowLogsToCloudWatch:
    """AWS::EC2::FlowLog resource."""

    resource: FlowLog
    log_destination_type = 'cloud-watch-logs'
    log_group_name: Ref[VPCFlowLogsLogGroup] = ref()
    deliver_logs_permission_arn: GetAtt[VPCFlowLogsRole] = get_att("Arn")
    log_format = ref(VPCFlowLogsLogFormat)
    max_aggregation_interval = ref(VPCFlowLogsMaxAggregationInterval)
    resource_id = ref(VPCID)
    resource_type = 'VPC'
    traffic_type = ref(VPCFlowLogsTrafficType)
    tags = [VPCFlowLogsToCloudWatchAssociationParameter]
