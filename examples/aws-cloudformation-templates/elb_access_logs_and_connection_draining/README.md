# ElbAccessLogsAndConnectionDraining

Migrated from [ELB_Access_Logs_And_Connection_Draining.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m elb_access_logs_and_connection_draining
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `ElasticLoadBalancer` | AWS::ElasticLoadBalancing::LoadBalancer |
| `LogsBucket` | AWS::S3::Bucket |
| `LogsBucketPolicy` | AWS::S3::BucketPolicy |
| `WebServerGroup` | AWS::AutoScaling::AutoScalingGroup |
| `LaunchConfig` | AWS::AutoScaling::LaunchConfiguration |
| `InstanceSecurityGroup` | AWS::EC2::SecurityGroup |
