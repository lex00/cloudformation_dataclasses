"""Compute resources: BastionInstance, PrivateInstance."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BastionInstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'Bastion'


@cloudformation_dataclass
class BastionInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    key_name = ref(KeyName)
    instance_type = 't2.micro'
    security_group_ids = [ref(BastionSG)]
    subnet_id = ref(PublicSubnet1)
    image_id = ref(LinuxAMI)
    iam_instance_profile = ref(BastionProfile)
    tags = [BastionInstanceAssociationParameter]


@cloudformation_dataclass
class PrivateInstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'Private'


@cloudformation_dataclass
class PrivateInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    key_name = ref(KeyName)
    instance_type = 't2.micro'
    security_group_ids = [ref(PrivateSG)]
    subnet_id = ref(PrivateSubnet1)
    image_id = ref(LinuxAMI)
    iam_instance_profile = ref(PrivateProfile)
    user_data = Base64(Sub("""#!/bin/bash -x
date > /tmp/datefile
cat /tmp/datefile
# Signal the status from instance
/opt/aws/bin/cfn-signal -e $? -d "This was all private." -r "Build Process Complete" '${PrivateWaitHandle}'
"""))
    tags = [PrivateInstanceAssociationParameter]
    depends_on = ["CfnEndpoint"]
