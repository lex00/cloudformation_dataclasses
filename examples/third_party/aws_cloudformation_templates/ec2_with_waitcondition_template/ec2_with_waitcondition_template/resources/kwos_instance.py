"""KWOSInstance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KWOSInstanceAssociationParameter:
    resource: AssociationParameter
    key = 'LaunchPlatform'
    value = ref(LaunchPlatform)


@cloudformation_dataclass
class KWOSInstanceAssociationParameter1:
    resource: AssociationParameter
    key = 'LaunchUser'
    value = ref(LaunchUser)


@cloudformation_dataclass
class KWOSInstanceAssociationParameter2:
    resource: AssociationParameter
    key = 'TestID'
    value = ref(TestID)


@cloudformation_dataclass
class KWOSInstanceAssociationParameter3:
    resource: AssociationParameter
    key = 'Name'
    value = ref(InstanceName)


@cloudformation_dataclass
class KWOSInstanceAssociationParameter4:
    resource: AssociationParameter
    key = 'BudgetCode'
    value = ref(BudgetCode)


@cloudformation_dataclass
class KWOSInstanceAssociationParameter5:
    resource: AssociationParameter
    key = 'TestTarget'
    value = ref(TestTarget)


@cloudformation_dataclass
class KWOSInstanceAssociationParameter6:
    resource: AssociationParameter
    key = 'AgentID'
    value = ref(AgentID)


@cloudformation_dataclass
class KWOSInstanceAssociationParameter7:
    resource: AssociationParameter
    key = 'IsMaster'
    value = ref(IsMaster)


@cloudformation_dataclass
class KWOSInstanceAssociationParameter8:
    resource: AssociationParameter
    key = 'MasterID'
    value = ref(MasterID)


@cloudformation_dataclass
class KWOSInstance:
    """AWS::EC2::Instance resource."""

    resource: Instance
    image_id = ref(ImageId)
    instance_type = ref(InstanceType)
    subnet_id = ref(SubnetId)
    security_group_ids = [ref(KWOSSecurityGroup)]
    key_name = ref(KeyName)
    tags = [KWOSInstanceAssociationParameter, KWOSInstanceAssociationParameter1, KWOSInstanceAssociationParameter2, KWOSInstanceAssociationParameter3, KWOSInstanceAssociationParameter4, KWOSInstanceAssociationParameter5, KWOSInstanceAssociationParameter6, KWOSInstanceAssociationParameter7, KWOSInstanceAssociationParameter8]
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
