"""Service - AWS::ECS::Service resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceDeploymentConfiguration:
    resource: ecs.DeploymentConfiguration
    maximum_percent = 200
    minimum_healthy_percent = 75


@cloudformation_dataclass
class ServiceNetworkConfiguration:
    resource: ecs.NetworkConfiguration
    # Unknown CF key: AwsvpcConfiguration = {
    #         AwsVpcConfiguration.assign_public_ip: 'ENABLED',
    #         AwsVpcConfiguration.security_groups: [ImportValue(Join(':', [
    #     ref(StackName),
    #     'FargateContainerSecurityGroup',
    # ]))],
    #         AwsVpcConfiguration.subnets: [
    #             ImportValue(Join(':', [
    #     ref(StackName),
    #     'PublicSubnetOne',
    # ])),
    #             ImportValue(Join(':', [
    #     ref(StackName),
    #     'PublicSubnetTwo',
    # ])),
    #         ],
    #     }


@cloudformation_dataclass
class ServiceLoadBalancer:
    resource: ecs.LoadBalancer
    container_name = ref(ServiceName)
    container_port = ref(ContainerPort)
    target_group_arn = ref(TargetGroup)


@cloudformation_dataclass
class Service:
    """AWS::ECS::Service resource."""

    resource: ecs.Service
    service_name = ref(ServiceName)
    cluster = ImportValue(Join(':', [
    ref(StackName),
    'ClusterName',
]))
    launch_type = 'FARGATE'
    deployment_configuration = ServiceDeploymentConfiguration
    desired_count = ref(DesiredCount)
    network_configuration = ServiceNetworkConfiguration
    task_definition = ref(TaskDefinition)
    load_balancers = [ServiceLoadBalancer]
    depends_on = ["LoadBalancerRule"]
