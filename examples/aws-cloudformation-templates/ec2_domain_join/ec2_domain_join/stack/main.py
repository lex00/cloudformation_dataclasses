"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class myssmdocument:
    """AWS::SSM::Document resource."""

    resource: ssm.Document
    content = {
        'schemaVersion': '1.2',
        'description': 'Join instances to an AWS Directory Service domain.',
        'parameters': {
            'directoryId': {
                'type': 'String',
                'description': '(Required) The ID of the AWS Directory Service directory.',
            },
            'directoryName': {
                'type': 'String',
                'description': '(Required) The name of the directory; for example, test.example.com',
            },
            'dnsIpAddresses': {
                'type': 'StringList',
                'default': [],
                'description': '(Optional) The IP addresses of the DNS servers in the directory. Required when DHCP is not configured. Learn more at http://docs.aws.amazon.com/directoryservice/latest/simple-ad/join_get_dns_addresses.html',
                'allowedPattern': '((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
            },
        },
        'runtimeConfig': {
            'aws:domainJoin': {
                'properties': {
                    'directoryId': '{{ directoryId }}',
                    'directoryName': '{{ directoryName }}',
                    'dnsIpAddresses': '{{ dnsIpAddresses }}',
                },
            },
        },
    }


@cloudformation_dataclass
class myInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    roles = ['DemoEC2SSMRole']
    instance_profile_name = 'myEC2SSMRole'


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '3389'
    to_port = '3389'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Allow http to client host'
    vpc_id = ref(VPC)
    security_group_ingress = [InstanceSecurityGroupEgress]


@cloudformation_dataclass
class myEC2InstanceSSMAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'directoryId'
    value = [ref(ADDirectoryId)]


@cloudformation_dataclass
class myEC2InstanceSSMAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'directoryName'
    value = [ref(ADDirectoryName)]


@cloudformation_dataclass
class myEC2InstanceSSMAssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'dnsIpAddresses'
    value = [ref(ADDnsIpAddresses1), ref(ADDnsIpAddresses2)]


@cloudformation_dataclass
class myEC2InstanceSSMSsmAssociation:
    resource: ec2.instance.SsmAssociation
    document_name = ref(myssmdocument)
    association_parameters = [myEC2InstanceSSMAssociationParameter, myEC2InstanceSSMAssociationParameter1, myEC2InstanceSSMAssociationParameter2]


@cloudformation_dataclass
class myEC2InstanceSSMAssociationParameter3:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'myEC2InstanceSSM'


@cloudformation_dataclass
class myEC2InstanceSSM:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    iam_instance_profile = ref(myInstanceProfile)
    ssm_associations = [myEC2InstanceSSMSsmAssociation]
    key_name = ref(KeyPair)
    image_id = ref(AMI)
    instance_type = ref(InstanceType)
    tags = [myEC2InstanceSSMAssociationParameter3]
    subnet_id = ref(PublicSubnet)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]


@cloudformation_dataclass
class myEC2SSMRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class myEC2SSMRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [myEC2SSMRoleAllowStatement0]


@cloudformation_dataclass
class myEC2SSMRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = myEC2SSMRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM']
    role_name = 'DemoEC2SSMRole'
