"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    instance_type = ref(InstanceType)
    iam_instance_profile = ref(IAMRole)
    key_name = ref(KeyName)
    image_id = ref(InstanceAMI)
    subnet_id = ref(SubnetId)
    user_data = Base64(Sub("""<script>
mkdir C:\Downloads\Amazon\AmazonCloudWatchAgent
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://s3.amazonaws.com/amazoncloudwatch-agent/windows/amd64/latest/amazon-cloudwatch-agent.msi','C:\Downloads\Amazon\AmazonCloudWatchAgent\amazon-cloudwatch-agent.msi')"
C:\Downloads\Amazon\AmazonCloudWatchAgent\amazon-cloudwatch-agent.msi
cfn-init.exe -v --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region} --configsets default
cfn-signal.exe -e %errorlevel% --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
</script>"""))
