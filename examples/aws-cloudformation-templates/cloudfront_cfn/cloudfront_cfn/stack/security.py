"""Security resources: myssmdocument, myInstanceProfile, myEC2SSMRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class myssmdocument:
    """AWS::SSM::Document resource."""

    resource: Document
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
