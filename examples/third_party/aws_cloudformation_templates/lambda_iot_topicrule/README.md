# LambdaIotTopicrule

Imported from `lambda-iot-topicrule.yaml`.

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
uv run python -m lambda_iot_topicrule
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `IoTPolicy` | AWS::IoT::Policy |
| `OpenIoTStarPolicy` | AWS::IoT::Policy |
| `IoTPolicyPrincipalAttachment` | AWS::IoT::PolicyPrincipalAttachment |
| `IoTThing` | AWS::IoT::Thing |
| `IoTThingPrincipalAttachment` | AWS::IoT::ThingPrincipalAttachment |
| `IoTTopicRule` | AWS::IoT::TopicRule |
| `MyLambda` | AWS::Lambda::Function |
| `MyLambdaVersion` | AWS::Lambda::Version |
| `MyLambdaRole` | AWS::IAM::Role |
| `MyLambdaPermission` | AWS::Lambda::Permission |
