# Elbguidedautoscalingrollingupgrade

Migrated from [ELBGuidedAutoScalingRollingUpgrade.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m elbguidedautoscalingrollingupgrade
```

### Validate Template

```bash
python -m elbguidedautoscalingrollingupgrade --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `WebServerGroup` | AWS::AutoScaling::AutoScalingGroup |
| `LaunchConfig` | AWS::AutoScaling::LaunchConfiguration |
| `ElasticLoadBalancer` | AWS::ElasticLoadBalancing::LoadBalancer |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
| `WebServerInstanceProfile` | AWS::IAM::InstanceProfile |
| `DescribeHealthRole` | AWS::IAM::Role |
