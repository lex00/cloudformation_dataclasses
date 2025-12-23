# Autoscalingmultiazwithnotifications

Migrated from [AutoScalingMultiAZWithNotifications.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

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
uv run python -m autoscalingmultiazwithnotifications
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `NotificationTopic` | AWS::SNS::Topic |
| `LaunchTemplate` | AWS::EC2::LaunchTemplate |
| `WebServerGroup` | AWS::AutoScaling::AutoScalingGroup |
| `WebServerScaleUpPolicy` | AWS::AutoScaling::ScalingPolicy |
| `WebServerScaleDownPolicy` | AWS::AutoScaling::ScalingPolicy |
| `CPUAlarmHigh` | AWS::CloudWatch::Alarm |
| `CPUAlarmLow` | AWS::CloudWatch::Alarm |
| `ElasticLoadBalancer` | AWS::ElasticLoadBalancingV2::LoadBalancer |
| `LoadBalancerSecurityGroup` | AWS::EC2::SecurityGroup |
| `LoadBalancerListener` | AWS::ElasticLoadBalancingV2::Listener |
| `TargetGroup` | AWS::ElasticLoadBalancingV2::TargetGroup |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
