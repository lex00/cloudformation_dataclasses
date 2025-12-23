"""LaunchTemplate - AWS::EC2::LaunchTemplate resource."""

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
