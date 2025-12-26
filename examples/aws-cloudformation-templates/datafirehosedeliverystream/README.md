# Datafirehosedeliverystream

Migrated from [DataFirehoseDeliveryStream.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m datafirehosedeliverystream
```

### Validate Template

```bash
python -m datafirehosedeliverystream --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `DeliveryStream` | AWS::KinesisFirehose::DeliveryStream |
| `FirehoseLogGroup` | AWS::Logs::LogGroup |
| `FirehoseLogStream` | AWS::Logs::LogStream |
| `DeliveryRole` | AWS::IAM::Role |
