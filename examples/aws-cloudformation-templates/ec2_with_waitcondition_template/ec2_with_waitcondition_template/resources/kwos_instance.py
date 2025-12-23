"""KWOSInstance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KWOSInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(ImageId)
    instance_type = ref(InstanceType)
    subnet_id = ref(SubnetId)
    security_group_ids = [ref(KWOSSecurityGroup)]
    key_name = ref(KeyName)
    tags = [{
        'Key': 'LaunchPlatform',
        'Value': ref(LaunchPlatform),
    }, {
        'Key': 'LaunchUser',
        'Value': ref(LaunchUser),
    }, {
        'Key': 'TestID',
        'Value': ref(TestID),
    }, {
        'Key': 'Name',
        'Value': ref(InstanceName),
    }, {
        'Key': 'BudgetCode',
        'Value': ref(BudgetCode),
    }, {
        'Key': 'TestTarget',
        'Value': ref(TestTarget),
    }, {
        'Key': 'AgentID',
        'Value': ref(AgentID),
    }, {
        'Key': 'IsMaster',
        'Value': ref(IsMaster),
    }, {
        'Key': 'MasterID',
        'Value': ref(MasterID),
    }]
    monitoring = False
    user_data = Base64(Join('', [
    """#!/bin/bash
""",
    """apt-get -y install python-pip
""",
    """pip install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-latest.tar.gz
""",
    """# Helper function
""",
    """function error_exit
""",
    """{
""",
    '  /usr/local/bin/cfn-signal -e 1 -r "$1" \'',
    ref(KWOSWaitHandle),
    """'
""",
    """  exit 1
""",
    """}
""",
    """# Install the basic system configuration
""",
    '/usr/local/bin/cfn-init -s ',
    AWS_STACK_ID,
    ' -r KWOSInstance ',
    '         --region ',
    AWS_REGION,
    """ || error_exit 'Failed to run cfn-init'
""",
    """# All done so signal success
""",
    '/usr/local/bin/cfn-signal -e 0 -r "KWOS setup complete" \'',
    ref(KWOSWaitHandle),
    """'
""",
]))
