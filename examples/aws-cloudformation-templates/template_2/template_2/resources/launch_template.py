"""LaunchTemplate - AWS::EC2::LaunchTemplate resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = {
        'BlockDeviceMappings': [{
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'Iops': 3000,
                'Throughput': 125,
                'VolumeSize': 80,
                'VolumeType': 'gp3',
            },
        }],
        'MetadataOptions': {
            'HttpPutResponseHopLimit': 2,
            'HttpTokens': 'optional',
        },
        'SecurityGroupIds': [ref(ControlPlaneSecurityGroup)],
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-name',
                        'Value': Sub('ng-${AWS::StackName}'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-type',
                        'Value': 'managed',
                    },
                ],
            },
            {
                'ResourceType': 'volume',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-name',
                        'Value': Sub('ng-${AWS::StackName}'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-type',
                        'Value': 'managed',
                    },
                ],
            },
            {
                'ResourceType': 'network-interface',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': Sub('ekshandson-ng-${AWS::StackName}-Node'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-name',
                        'Value': Sub('ng-${AWS::StackName}'),
                    },
                    {
                        'Key': 'alpha.eksctl.io/nodegroup-type',
                        'Value': 'managed',
                    },
                ],
            },
        ],
    }
    launch_template_name = Sub('${AWS::StackName}-LaunchTemplate')
