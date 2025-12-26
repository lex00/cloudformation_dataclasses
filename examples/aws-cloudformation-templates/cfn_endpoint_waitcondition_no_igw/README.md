# CfnEndpointWaitconditionNoIgw

Imported from `DIRECTORY_SETTINGS.cfn.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m cfn_endpoint_waitcondition_no_igw
```

### Validate Template

```bash
python -m cfn_endpoint_waitcondition_no_igw --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `DirectoryConsoleDelegatedAccessEC2ReadOnlyRole` | AWS::IAM::Role |
| `DirectoryConsoleDelegatedAccessSecurityAuditRole` | AWS::IAM::Role |
| `DirectoryMonitoringTopic` | AWS::SNS::Topic |
| `DirectorySettingsLambdaFunction` | AWS::Lambda::Function |
| `DirectorySettingsLambdaLogsLogGroup` | AWS::Logs::LogGroup |
| `DirectorySettingsLambdaRole` | AWS::IAM::Role |
| `DirectorySettingsResource` | Custom::DirectorySettingsResource |
