"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class InstanceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [InstanceRoleAllowStatement0]


@cloudformation_dataclass
class InstanceRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ec2:Describe*',
        'ec2:CreateTags',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class InstanceRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [InstanceRoleAllowStatement0_1]


@cloudformation_dataclass
class InstanceRolePolicy:
    resource: iam.user.Policy
    policy_name = 'taginstancepolicy'
    policy_document = InstanceRolePolicies0PolicyDocument


@cloudformation_dataclass
class InstanceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = InstanceRoleAssumeRolePolicyDocument
    path = '/'
    policies = [InstanceRolePolicy]


@cloudformation_dataclass
class InstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    path = '/'
    roles = [ref(InstanceRole)]


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
