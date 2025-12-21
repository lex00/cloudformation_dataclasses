# LogSetupManagementPkg

Migrated from [log-setup-management-pkg.json](https://github.com/aws-cloudformation/aws-cloudformation-templates).

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
uv run python -m log_setup_management_pkg
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `CentralEventBus` | AWS::Events::EventBus |
| `CentralEventBusPolicy` | AWS::Events::EventBusPolicy |
| `CentralEventLog` | AWS::Logs::LogGroup |
| `CentralEventLogKey` | AWS::KMS::Key |
| `CentralEventLogQuery` | AWS::Logs::QueryDefinition |
| `CentralEventLogQueryReason` | AWS::Logs::QueryDefinition |
| `CentralEventLogPolicy` | AWS::Logs::ResourcePolicy |
| `CentralEventRule` | AWS::Events::Rule |
| `DeadLetterQueue` | AWS::SQS::Queue |
| `TargetAccountLogging` | AWS::CloudFormation::StackSet |
