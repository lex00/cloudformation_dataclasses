from __future__ import annotations

"""PrivateInstance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateInstanceAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'Private'


@cloudformation_dataclass
class PrivateInstance:
    """AWS::EC2::Instance resource."""

    resource: Instance
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
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource PrivateInstance --region ${AWS::Region}
"""))
    tags = [PrivateInstanceAssociationParameter]
    depends_on = ["CfnEndpoint"]
