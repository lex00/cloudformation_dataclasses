from __future__ import annotations

"""loadBalancer - AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class loadBalancerSubnetMapping:
    resource: SubnetMapping
    allocation_id = get_att(EIP1, "AllocationId")
    subnet_id = Select(0, ref(Subnet1))


@cloudformation_dataclass
class loadBalancerSubnetMapping1:
    resource: SubnetMapping
    allocation_id = get_att(EIP2, "AllocationId")
    subnet_id = Select(0, ref(Subnet2))


@cloudformation_dataclass
class loadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: LoadBalancer
    subnet_mappings = [loadBalancerSubnetMapping, loadBalancerSubnetMapping1]
    type_ = ref(ELBType)
    ip_address_type = ref(ELBIpAddressType)
    depends_on = ["EIP2", "EIP1"]
