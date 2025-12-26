"""Compute resources: PrivateInstance."""

from . import *  # noqa: F403


@cloudformation_dataclass
class PrivateInstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'Private'


@cloudformation_dataclass
class PrivateInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    instance_type = 't3.micro'
    security_group_ids = [ref(PrivateSG)]
    subnet_id = ref(PrivateSubnet1)
    image_id = ref(LinuxAMI)
    user_data = Base64(Sub("""#!/bin/bash -x
date > /tmp/datefile
cat /tmp/datefile
# Signal the status from instance
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource PrivateInstance --region ${AWS::Region}
"""))
    tags = [PrivateInstanceAssociationParameter]
    depends_on = [CfnEndpoint]
