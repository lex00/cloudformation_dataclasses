"""Compute resources: LaunchTemplate, WebServerGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    # Unknown resource type: AWS::EC2::LaunchTemplate
    resource: CloudFormationResource
    launch_template_data = {
        'KeyName': ref(KeyName),
        'ImageId': FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", ref(InstanceType), 'Arch')),
        'InstanceType': ref(InstanceType),
        'SecurityGroups': [ref(InstanceSecurityGroup)],
        'IamInstanceProfile': {
            'Name': ref(WebServerInstanceProfile),
        },
        'UserData': Base64(Sub("""#!/bin/bash -xe
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource LaunchTemplate --configsets full_install --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource WebServerGroup --region ${AWS::Region}
""")),
    }


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    # Unknown resource type: AWS::AutoScaling::AutoScalingGroup
    resource: CloudFormationResource
    availability_zones = GetAZs()
    launch_template = {
        'LaunchTemplateId': ref(LaunchTemplate),
        'Version': get_att(LaunchTemplate, "LatestVersionNumber"),
    }
    min_size = 2
    max_size = 4
    load_balancer_names = [ref(ElasticLoadBalancer)]
