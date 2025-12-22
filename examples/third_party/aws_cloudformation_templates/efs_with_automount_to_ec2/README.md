# EfsWithAutomountToEc2

Imported from `efs_with_automount_to_ec2.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Run Tests

```bash
uv run pytest tests/ -v
```

### Generate Template

```bash
uv run python -m efs_with_automount_to_ec2
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `EFSFileSystem` | AWS::EFS::FileSystem |
| `EFSMountTarget1` | AWS::EFS::MountTarget |
| `EFSMountTarget2` | AWS::EFS::MountTarget |
| `EFSMountTarget3` | AWS::EFS::MountTarget |
| `EFSMountTarget4` | AWS::EFS::MountTarget |
| `CPUAlarmHigh` | AWS::CloudWatch::Alarm |
| `CPUAlarmLow` | AWS::CloudWatch::Alarm |
| `AutoScalingGroup` | AWS::AutoScaling::AutoScalingGroup |
| `InstanceProfile` | AWS::IAM::InstanceProfile |
| `ScaleDownPolicy` | AWS::AutoScaling::ScalingPolicy |
| `ScaleUpPolicy` | AWS::AutoScaling::ScalingPolicy |
| `ElasticLoadBalancer` | AWS::ElasticLoadBalancing::LoadBalancer |
| `IAMAssumeInstanceRole` | AWS::IAM::Role |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
| `ELBSecurityGroup` | AWS::EC2::SecurityGroup |
| `EFSSecurityGroup` | AWS::EC2::SecurityGroup |
| `LaunchConfig` | AWS::AutoScaling::LaunchConfiguration |
