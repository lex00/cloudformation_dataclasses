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
    instance_type = 't3.micro'
    security_group_ids = [ref(PrivateSG)]
    subnet_id = ref(PrivateSubnet1)
    image_id = ref(LinuxAMI)
    user_data = Base64(Sub("""#!/bin/bash -x
date > /tmp/datefile
cat /tmp/datefile
# Signal the status from instance
/opt/aws/bin/cfn-signal -e $? -d "This was all private." -r "Build Process Complete" '${PrivateWaitHandle}'
"""))
    tags = [PrivateInstanceAssociationParameter]
    depends_on = ["CfnEndpoint"]
