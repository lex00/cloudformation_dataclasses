"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ASCPrivateLinkCertificate:
    """AWS::CertificateManager::Certificate resource."""

    # Unknown resource type: AWS::CertificateManager::Certificate
    resource: CloudFormationResource
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
class ASCPrivateLinkLambdaRole:
    """AWS::IAM::Role resource."""

    # Unknown resource type: AWS::IAM::Role
    resource: CloudFormationResource
    assume_role_policy_document = ASCPrivateLinkLambdaRoleAssumeRolePolicyDocument
    path = '/'
    policies = [{
        'PolicyName': 'ASCPrivateLinkLambdaPolicy',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Effect': 'Allow',
                'Action': [
                    'logs:CreateLogGroup',
                    'logs:CreateLogStream',
                    'logs:PutLogEvents',
                    'ec2:DescribeVpcEndpointServiceConfigurations',
                    'ec2:ModifyVpcEndpointServiceConfiguration',
                ],
                'Resource': '*',
            }],
        },
    }]
    depends_on = ["ASCPrivateLinkCertificate"]


@cloudformation_dataclass
class ASCPrivateLinkLambdaFunction:
    """AWS::Lambda::Function resource."""

    # Unknown resource type: AWS::Lambda::Function
    resource: CloudFormationResource
    description = 'Lambda function to help with private link infrastructure setup'
    handler = 'index.handler'
    role = get_att(ASCPrivateLinkLambdaRole, "Arn")
    timeout = 900
    runtime = 'python3.12'
    vpc_config = {
        'SubnetIds': ref(Subnets),
        'SecurityGroupIds': ref(SecurityGroups),
    }
    code = {
        'ZipFile': """import boto3
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
""",
    }


@cloudformation_dataclass
class ASCPrivateLinkNLB:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    # Unknown resource type: AWS::ElasticLoadBalancingV2::LoadBalancer
    resource: CloudFormationResource
    type_ = 'network'
    scheme = 'internal'
    subnets = ref(Subnets)
    load_balancer_attributes = [{
        'Key': 'load_balancing.cross_zone.enabled',
        'Value': True,
    }]
    depends_on = ["ASCPrivateLinkCertificate"]


@cloudformation_dataclass
class ASCPrivateLinkVPCES:
    """AWS::EC2::VPCEndpointService resource."""

    # Unknown resource type: AWS::EC2::VPCEndpointService
    resource: CloudFormationResource
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
class ASCPrivateLinkTargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    # Unknown resource type: AWS::ElasticLoadBalancingV2::TargetGroup
    resource: CloudFormationResource
    vpc_id = ref(VpcId)
    protocol = If("SapUseHttps", 'TLS', 'TCP')
    port = 443
    target_type = 'ip'
    targets = [{
        'AvailabilityZone': If("IpInVpc", AWS_NO_VALUE, 'all'),
        'Id': ref(IP),
        'Port': ref(Port),
    }]
    health_check_path = ref(HealthCheckPath)
    health_check_protocol = ref(Protocol)
    depends_on = ["ASCPrivateLinkCertificate"]


@cloudformation_dataclass
class ASCPrivateLinkListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    # Unknown resource type: AWS::ElasticLoadBalancingV2::Listener
    resource: CloudFormationResource
    load_balancer_arn = ref(ASCPrivateLinkNLB)
    protocol = 'TLS'
    port = 443
    ssl_policy = 'ELBSecurityPolicy-TLS13-1-0-2021-06'
    certificates = [{
        'CertificateArn': ref(ASCPrivateLinkCertificate),
    }]
    default_actions = [{
        'Type': 'forward',
        'TargetGroupArn': ref(ASCPrivateLinkTargetGroup),
    }]


@cloudformation_dataclass
class ASCPrivateLinkVPCESPermission:
    """AWS::EC2::VPCEndpointServicePermissions resource."""

    # Unknown resource type: AWS::EC2::VPCEndpointServicePermissions
    resource: CloudFormationResource
    allowed_principals = ['appflow.amazonaws.com']
    service_id = ref(ASCPrivateLinkVPCES)
