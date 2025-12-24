"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ASCPrivateLinkCertificate:
    """AWS::CertificateManager::Certificate resource."""

    resource: certificatemanager.Certificate
    domain_name = ref(DomainName)
    validation_method = 'DNS'


@cloudformation_dataclass
class ASCPrivateLinkLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ASCPrivateLinkLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ASCPrivateLinkLambdaRoleAllowStatement0]


@cloudformation_dataclass
class ASCPrivateLinkLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'ec2:DescribeVpcEndpointServiceConfigurations',
        'ec2:ModifyVpcEndpointServiceConfiguration',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class ASCPrivateLinkLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ASCPrivateLinkLambdaRoleAllowStatement0_1]


@cloudformation_dataclass
class ASCPrivateLinkLambdaRolePolicy:
    resource: iam.user.Policy
    policy_name = 'ASCPrivateLinkLambdaPolicy'
    policy_document = ASCPrivateLinkLambdaRolePolicies0PolicyDocument


@cloudformation_dataclass
class ASCPrivateLinkLambdaRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ASCPrivateLinkLambdaRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ASCPrivateLinkLambdaRolePolicy]
    depends_on = ["ASCPrivateLinkCertificate"]


@cloudformation_dataclass
class ASCPrivateLinkLambdaFunctionCapacityProviderVpcConfig:
    resource: lambda_.capacity_provider.CapacityProviderVpcConfig
    subnet_ids = ref(Subnets)
    security_group_ids = ref(SecurityGroups)


@cloudformation_dataclass
class ASCPrivateLinkLambdaFunctionCode:
    resource: lambda_.function.Code
    zip_file = """import boto3
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
          ec2Client.modify_vpc_endpoint_service_configuration(ServiceId=serviceId, PrivateDnsName=domainName)
          validationRecord = ec2Client.describe_vpc_endpoint_service_configurations(ServiceIds=[serviceId])['ServiceConfigurations'][0]['PrivateDnsNameConfiguration']
          responseData['validationRecord'] = validationRecord
        case _:
          raise Exception('Unsupported action')
    else:
      print('Skip on resource UPDATE and DELETE')
    cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
  except Exception as e:
    logging.exception(e)
    cfnresponse.send(event, context, cfnresponse.FAILED, responseData)
"""


@cloudformation_dataclass
class ASCPrivateLinkLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    description = 'Lambda function to help with private link infrastructure setup'
    handler = 'index.handler'
    role = get_att(ASCPrivateLinkLambdaRole, "Arn")
    timeout = 900
    runtime = 'python3.12'
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
    depends_on = ["ASCPrivateLinkCertificate"]


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
    depends_on = ["ASCPrivateLinkVPCES"]


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
    depends_on = ["ASCPrivateLinkCertificate"]


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
