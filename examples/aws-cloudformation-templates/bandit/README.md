# Bandit

Imported from `AutoScalingScheduledAction.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m bandit
```

### Validate Template

```bash
python -m bandit --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `WebServerGroup` | AWS::AutoScaling::AutoScalingGroup |
| `ScheduledActionUp` | AWS::AutoScaling::ScheduledAction |
| `ScheduledActionDown` | AWS::AutoScaling::ScheduledAction |
| `LaunchTemplate` | AWS::EC2::LaunchTemplate |
| `ElasticLoadBalancer` | AWS::ElasticLoadBalancing::LoadBalancer |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
