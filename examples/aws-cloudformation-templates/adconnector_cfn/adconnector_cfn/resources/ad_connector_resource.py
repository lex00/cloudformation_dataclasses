"""ADConnectorResource - Custom::ADConnectorResource resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorResource:
    """Custom::ADConnectorResource resource."""

    # Unknown resource type: Custom::ADConnectorResource
    resource: CloudFormationResource
    service_token = get_att(ADConnectorLambdaFunction, "Arn")
    adconnector_description = ref(ADConnectorDescription)
    adconnector_size = ref(ADConnectorSize)
    adconnector_subnet_id1 = ref(PrivateSubnet1ID)
    adconnector_subnet_id2 = ref(PrivateSubnet2ID)
    adconnector_vpcid = ref(VPCID)
    domain_dns_name = ref(DomainDNSName)
    domain_dns_servers = ref(DomainDNSServers)
    domain_netbios_name = ref(DomainNetBiosName)
    domain_join_secret_id = ref(ADConnectorServiceAccountSecret)
