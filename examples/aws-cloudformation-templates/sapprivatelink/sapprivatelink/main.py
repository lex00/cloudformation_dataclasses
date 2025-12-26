"""Stack resources."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.lambda_ import Runtime


@cloudformation_dataclass
class ASCPrivateLinkCertificateDomainValidationOption:
    resource: certificatemanager.certificate.DomainValidationOption
    domain_name = ref(DomainName)
    hosted_zone_id = ref(HostedZone)


@cloudformation_dataclass
class ASCPrivateLinkCertificate:
    """AWS::CertificateManager::Certificate resource."""

    resource: certificatemanager.Certificate
    domain_name = ref(DomainName)
    validation_method = 'DNS'
    domain_validation_options = [ASCPrivateLinkCertificateDomainValidationOption]


@cloudformation_dataclass
class ASCPrivateLinkLambdaFunctionCapacityProviderVpcConfig:
    resource: lambda_.capacity_provider.CapacityProviderVpcConfig
    subnet_ids = ref(Subnets)
    security_group_ids = ref(SecurityGroups)


@cloudformation_dataclass
class ASCPrivateLinkLambdaFunctionCode:
    resource: lambda_.function.Code
    zip_file = Sub("""import boto3
import cfnresponse
import logging
def handler(event, context):
  print('Receive event: {} and context: {}'.format(str(event), str(context)))
  responseData = {}
  eventType = event['RequestType'].strip()
  props = event['ResourceProperties']
  try:
    if eventType in ('Create'):
      match props['Action']:
        case 'EnablePrivateDNS':
          dnsClient = boto3.client('route53')
          ec2Client = boto3.client('ec2')
          serviceId = props['ServiceId']
          domainName = props['DomainName']
          hostedZoneId = props['HostedZoneId']
          ec2Client.modify_vpc_endpoint_service_configuration(ServiceId=serviceId, PrivateDnsName=domainName)
          validationRecord = ec2Client.describe_vpc_endpoint_service_configurations(ServiceIds=[serviceId])['ServiceConfigurations'][0]['PrivateDnsNameConfiguration']
          dnsClient.change_resource_record_sets(
            HostedZoneId=hostedZoneId,
            ChangeBatch={
              'Changes': [
                {
                  'Action': 'UPSERT',
                  'ResourceRecordSet': {
                    'Type': validationRecord['Type'],
                    'Name': '{}.{}'.format(validationRecord['Name'], domainName[2:] if domainName.startswith('*') else domainName),
                    'ResourceRecords': [{'Value': '"{}"'.format(validationRecord['Value'])}],
                    'TTL': 300
                  }
                }
              ]
            }
          )
        case _:
          raise Exception('Unsupported action')
    else:
      print('Skip on resource UPDATE and DELETE')
    cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
  except Exception as e:
    logging.exception(e)
    cfnresponse.send(event, context, cfnresponse.FAILED, responseData)
""", {
    'Region': AWS_REGION,
})


@cloudformation_dataclass
class ASCPrivateLinkLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    description = 'Lambda function to help with private link infrastructure setup'
    handler = 'index.handler'
    role = get_att(ASCPrivateLinkLambdaRole, "Arn")
    timeout = 900
    runtime = Runtime.PYTHON3_12
    vpc_config = ASCPrivateLinkLambdaFunctionCapacityProviderVpcConfig
    code = ASCPrivateLinkLambdaFunctionCode


@cloudformation_dataclass
class ASCPrivateLinkNLBLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'load_balancing.cross_zone.enabled'
    value = True


@cloudformation_dataclass
class ASCPrivateLinkNLB:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    type_ = 'network'
    scheme = 'internal'
    subnets = ref(Subnets)
    load_balancer_attributes = [ASCPrivateLinkNLBLoadBalancerAttribute]


@cloudformation_dataclass
class ASCPrivateLinkVPCES:
    """AWS::EC2::VPCEndpointService resource."""

    resource: ec2.VPCEndpointService
    acceptance_required = False
    network_load_balancer_arns = [ref(ASCPrivateLinkNLB)]


@cloudformation_dataclass
class ASCPrivateLinkEnablePrivateDNS:
    """Custom::CustomResource resource."""

    # Unknown resource type: Custom::CustomResource
    resource: CloudFormationResource
    service_token = get_att(ASCPrivateLinkLambdaFunction, "Arn")
    action = 'EnablePrivateDNS'
    service_id = ref(ASCPrivateLinkVPCES)
    domain_name = ref(DomainName)
    hosted_zone_id = ref(HostedZone)
    depends_on = [ASCPrivateLinkVPCES]


@cloudformation_dataclass
class ASCPrivateLinkTargetGroupTargetDescription:
    resource: elasticloadbalancingv2.target_group.TargetDescription
    availability_zone = If("IpInVpc", AWS_NO_VALUE, 'all')
    id = ref(IP)
    port = ref(Port)


@cloudformation_dataclass
class ASCPrivateLinkTargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    vpc_id = ref(VpcId)
    protocol = If("SapUseHttps", 'TLS', 'TCP')
    port = 443
    target_type = 'ip'
    targets = [ASCPrivateLinkTargetGroupTargetDescription]
    health_check_path = ref(HealthCheckPath)
    health_check_protocol = ref(Protocol)


@cloudformation_dataclass
class ASCPrivateLinkListenerCertificate:
    resource: elasticloadbalancingv2.listener_certificate.Certificate
    certificate_arn = ref(ASCPrivateLinkCertificate)


@cloudformation_dataclass
class ASCPrivateLinkListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    type_ = 'forward'
    target_group_arn = ref(ASCPrivateLinkTargetGroup)


@cloudformation_dataclass
class ASCPrivateLinkListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    load_balancer_arn = ref(ASCPrivateLinkNLB)
    protocol = 'TLS'
    port = 443
    ssl_policy = 'ELBSecurityPolicy-TLS13-1-0-2021-06'
    certificates = [ASCPrivateLinkListenerCertificate]
    default_actions = [ASCPrivateLinkListenerAction]


@cloudformation_dataclass
class ASCPrivateLinkVPCESPermission:
    """AWS::EC2::VPCEndpointServicePermissions resource."""

    resource: ec2.VPCEndpointServicePermissions
    allowed_principals = ['appflow.amazonaws.com']
    service_id = ref(ASCPrivateLinkVPCES)
