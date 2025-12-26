# NeptuneCfn

Migrated from [Neptune.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m neptune_cfn
```

### Validate Template

```bash
python -m neptune_cfn --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `NeptuneDBSG` | AWS::EC2::SecurityGroup |
| `NeptuneDBCluster` | AWS::Neptune::DBCluster |
| `NeptuneDBInstance` | AWS::Neptune::DBInstance |
| `NeptuneDBClusterParameterGroup` | AWS::Neptune::DBClusterParameterGroup |
| `NeptuneDBParameterGroup` | AWS::Neptune::DBParameterGroup |
| `NeptuneDBSubnetGroup` | AWS::Neptune::DBSubnetGroup |
| `NeptuneAlarmTopic` | AWS::SNS::Topic |
| `NeptuneAlarmSubscription` | AWS::SNS::Subscription |
| `NeptuneRole` | AWS::IAM::Role |
| `NeptuneCloudWatchPolicy` | AWS::IAM::ManagedPolicy |
| `NeptuneS3Policy` | AWS::IAM::ManagedPolicy |
| `NeptunePrimaryCpuAlarm` | AWS::CloudWatch::Alarm |
| `NeptunePrimaryMemoryAlarm` | AWS::CloudWatch::Alarm |
| `NeptunePrimaryGremlinRequestsPerSecAlarm` | AWS::CloudWatch::Alarm |
| `NeptunePrimarySparqlRequestsPerSecAlarm` | AWS::CloudWatch::Alarm |
