# Config

Migrated from [Config.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates).

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
uv run python -m config
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `Ec2Volume` | AWS::EC2::Volume |
| `ConfigRecorder` | AWS::Config::ConfigurationRecorder |
| `DeliveryChannel` | AWS::Config::DeliveryChannel |
| `ConfigBucket` | AWS::S3::Bucket |
| `ConfigTopic` | AWS::SNS::Topic |
| `ConfigTopicPolicy` | AWS::SNS::TopicPolicy |
| `ConfigRuleForVolumeTags` | AWS::Config::ConfigRule |
| `ConfigRuleForVolumeAutoEnableIO` | AWS::Config::ConfigRule |
| `ConfigPermissionToCallLambda` | AWS::Lambda::Permission |
| `VolumeAutoEnableIOComplianceCheck` | AWS::Lambda::Function |
| `LambdaExecutionRole` | AWS::IAM::Role |
| `ConfigRole` | AWS::IAM::Role |
