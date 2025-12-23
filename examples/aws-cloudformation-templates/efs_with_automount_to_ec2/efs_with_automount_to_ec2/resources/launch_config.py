"""LaunchConfig - AWS::AutoScaling::LaunchConfiguration resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchConfig:
    """AWS::AutoScaling::LaunchConfiguration resource."""

    resource: autoscaling.LaunchConfiguration
    iam_instance_profile = ref(InstanceProfile)
    image_id = FindInMap("EC2RegionMap", AWS_REGION, '64')
    instance_type = ref(InstanceType)
    key_name = ref(KeyName)
    security_groups = [get_att(InstanceSecurityGroup, "GroupId")]
    user_data = Base64(Sub("""#!/bin/bash -x
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
apt-get update
apt-get install -y curl nfs-common
EC2_REGION=${AWS::Region}
DIR_TGT=/mnt/efs/
EFS_FILE_SYSTEM_ID=${EFSFileSystem}
mkdir -p $DIR_TGT
DIR_SRC=$EFS_FILE_SYSTEM_ID.efs.$EC2_REGION.amazonaws.com
mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 $DIR_SRC:/ $DIR_TGT"""))
