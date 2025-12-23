"""LinuxInstance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LinuxInstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class LinuxInstanceEbs:
    resource: ec2.instance.Ebs
    volume_type = 'io1'
    iops = '200'
    delete_on_termination = 'true'
    volume_size = '10'


@cloudformation_dataclass
class LinuxInstanceBlockDeviceMapping:
    resource: ec2.instance.BlockDeviceMapping
    device_name = '/dev/sdm'
    ebs = LinuxInstanceEbs


@cloudformation_dataclass
class LinuxInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(LinuxAMIID)
    subnet_id = ref(SubnetId)
    instance_type = ref(InstanceType)
    availability_zone = ref(InstanceAZ)
    iam_instance_profile = ref(InstanceProfile)
    key_name = ref(KeyName)
    user_data = Base64("""AWS_AVAIL_ZONE=$(curl http://169.254.169.254/latest/meta-data/placement/availability-zone)
AWS_REGION="`echo \"$AWS_AVAIL_ZONE\" | sed 's/[a-z]$//'`"
AWS_INSTANCE_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id)
ROOT_VOLUME_IDS=$(aws ec2 describe-instances --region $AWS_REGION --instance-id $AWS_INSTANCE_ID --output text --query Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId)
aws ec2 create-tags --resources $ROOT_VOLUME_IDS --region $AWS_REGION --tags Key=MyRootTag,Value=MyRootVolumesValue
""")
    tags = [LinuxInstanceAssociationParameter]
    block_device_mappings = [LinuxInstanceBlockDeviceMapping]
