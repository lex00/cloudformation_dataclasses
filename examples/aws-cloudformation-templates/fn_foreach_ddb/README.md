# FnForeachDdb

Imported from `Config.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m fn_foreach_ddb
```

### Validate Template

```bash
python -m fn_foreach_ddb --validate
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
