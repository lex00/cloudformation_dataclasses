from __future__ import annotations

"""EMRCluster - AWS::EMR::Cluster resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EMRClusterApplication:
    resource: Application
    name = 'Ganglia'


@cloudformation_dataclass
class EMRClusterConfiguration:
    resource: Configuration
    classification = 'hbase-site'
    configuration_properties = {
        'hbase.rootdir': ref(S3DataUri),
    }


@cloudformation_dataclass
class EMRClusterConfiguration1:
    resource: Configuration
    classification = 'hbase'
    configuration_properties = {
        'hbase.emr.storageMode': 's3',
    }


@cloudformation_dataclass
class EMRClusterInstanceGroupConfig:
    resource: InstanceGroupConfig
    instance_count = 1
    instance_type = ref(MasterInstanceType)
    market = 'ON_DEMAND'
    name = 'Master'


@cloudformation_dataclass
class EMRClusterInstanceGroupConfig1:
    resource: InstanceGroupConfig
    instance_count = ref(NumberOfCoreInstances)
    instance_type = ref(CoreInstanceType)
    market = 'ON_DEMAND'
    name = 'Core'


@cloudformation_dataclass
class EMRClusterJobFlowInstancesConfig:
    resource: JobFlowInstancesConfig
    ec2_key_name = ref(KeyName)
    ec2_subnet_id = ref(SubnetID)
    master_instance_group = EMRClusterInstanceGroupConfig
    core_instance_group = EMRClusterInstanceGroupConfig1
    termination_protected = False


@cloudformation_dataclass
class EMRCluster:
    """AWS::EMR::Cluster resource."""

    resource: Cluster
    applications = [EMRClusterApplication, If("Spark", {
    BootstrapActionConfig.name: 'Spark',
}, AWS_NO_VALUE), If("Hbase", {
    BootstrapActionConfig.name: 'Hbase',
}, AWS_NO_VALUE)]
    configurations = [EMRClusterConfiguration, EMRClusterConfiguration1]
    instances = EMRClusterJobFlowInstancesConfig
    visible_to_all_users = True
    job_flow_role = ref(EMRClusterinstanceProfile)
    release_label = ref(ReleaseLabel)
    log_uri = ref(LogUri)
    name = ref(EMRClusterName)
    auto_scaling_role = 'EMR_AutoScaling_DefaultRole'
    service_role = ref(EMRClusterServiceRole)
    depends_on = ["EMRClusterServiceRole", "EMRClusterinstanceProfileRole", "EMRClusterinstanceProfile"]
