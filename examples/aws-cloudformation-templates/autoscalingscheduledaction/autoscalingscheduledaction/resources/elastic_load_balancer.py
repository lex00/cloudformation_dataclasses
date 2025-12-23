"""ElasticLoadBalancer - AWS::ElasticLoadBalancing::LoadBalancer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancing::LoadBalancer resource."""

    # Unknown resource type: AWS::ElasticLoadBalancing::LoadBalancer
    resource: CloudFormationResource
    availability_zones = GetAZs()
    cross_zone = 'true'
    listeners = [{
        'LoadBalancerPort': '80',
        'InstancePort': '80',
        'Protocol': 'HTTP',
    }]
    health_check = {
        'Target': 'HTTP:80/',
        'HealthyThreshold': '3',
        'UnhealthyThreshold': '5',
        'Interval': '30',
        'Timeout': '5',
    }
