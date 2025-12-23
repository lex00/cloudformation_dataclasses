# EcsScheduleExample

Migrated from [ECS_Schedule_Example.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m ecs_schedule_example
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `ECSCluster` | AWS::ECS::Cluster |
| `EcsSecurityGroup` | AWS::EC2::SecurityGroup |
| `EcsSecurityGroupHTTPinbound` | AWS::EC2::SecurityGroupIngress |
| `EcsSecurityGroupSSHinbound` | AWS::EC2::SecurityGroupIngress |
| `EcsSecurityGroupALBports` | AWS::EC2::SecurityGroupIngress |
| `LogsKmsKey` | AWS::KMS::Key |
| `CloudwatchLogsGroup` | AWS::Logs::LogGroup |
| `TaskDefinition` | AWS::ECS::TaskDefinition |
| `ECSALB` | AWS::ElasticLoadBalancingV2::LoadBalancer |
| `ALBListener` | AWS::ElasticLoadBalancingV2::Listener |
| `ECSALBListenerRule` | AWS::ElasticLoadBalancingV2::ListenerRule |
| `ECSTG` | AWS::ElasticLoadBalancingV2::TargetGroup |
| `ECSAutoScalingGroup` | AWS::AutoScaling::AutoScalingGroup |
| `ContainerInstances` | AWS::AutoScaling::LaunchConfiguration |
| `Service` | AWS::ECS::Service |
| `ECSScheduledTask` | AWS::Events::Rule |
| `ECSEventRole` | AWS::IAM::Role |
| `ECSServiceRole` | AWS::IAM::Role |
| `ServiceScalingTarget` | AWS::ApplicationAutoScaling::ScalableTarget |
| `ServiceScalingPolicy` | AWS::ApplicationAutoScaling::ScalingPolicy |
| `ALB500sAlarmScaleUp` | AWS::CloudWatch::Alarm |
| `EC2Role` | AWS::IAM::Role |
| `AutoscalingRole` | AWS::IAM::Role |
| `EC2InstanceProfile` | AWS::IAM::InstanceProfile |
