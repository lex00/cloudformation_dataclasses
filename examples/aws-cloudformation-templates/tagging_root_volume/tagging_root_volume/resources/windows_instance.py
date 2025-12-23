"""WindowsInstance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WindowsInstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class WindowsInstanceEbs:
    resource: ec2.instance.Ebs
    volume_type = 'io1'
    iops = '200'
    delete_on_termination = 'true'
    volume_size = '10'


@cloudformation_dataclass
class WindowsInstanceBlockDeviceMapping:
    resource: ec2.instance.BlockDeviceMapping
    device_name = '/dev/sdm'
    ebs = WindowsInstanceEbs


@cloudformation_dataclass
class WindowsInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(WindowsAMIID)
    subnet_id = ref(SubnetId)
    instance_type = ref(InstanceType)
    availability_zone = ref(InstanceAZ)
    iam_instance_profile = ref(InstanceProfile)
    key_name = ref(KeyName)
    user_data = Base64("""<powershell>
  $AWS_AVAIL_ZONE=(curl http://169.254.169.254/latest/meta-data/placement/availability-zone).Content
  $AWS_REGION=$AWS_AVAIL_ZONE.Substring(0,$AWS_AVAIL_ZONE.length-1)
  $AWS_INSTANCE_ID=(curl http://169.254.169.254/latest/meta-data/instance-id).Content
  $ROOT_VOLUME_IDS=((Get-EC2Instance -Region $AWS_REGION -InstanceId $AWS_INSTANCE_ID).Instances.BlockDeviceMappings | where-object DeviceName -match '/dev/sda1').Ebs.VolumeId
  $tag = New-Object Amazon.EC2.Model.Tag
  $tag.key = "MyRootTag"
  $tag.value = "MyRootVolumesValue"
  New-EC2Tag -Resource $ROOT_VOLUME_IDS -Region $AWS_REGION -Tag $tag
</powershell>
""")
    tags = [WindowsInstanceAssociationParameter]
    block_device_mappings = [WindowsInstanceBlockDeviceMapping]
