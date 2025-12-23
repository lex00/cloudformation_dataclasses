# LogSetupTargetAccounts

Migrated from [log-setup-target-accounts.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates).

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
uv run python -m log_setup_target_accounts
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `CloudFormationEventRule` | AWS::Events::Rule |
| `DeadLetterQueue` | AWS::SQS::Queue |
| `DeadLetterQueuePolicy` | AWS::SQS::QueuePolicy |
| `EventBridgeRole` | AWS::IAM::Role |
| `EventBridgeRolePolicy` | AWS::IAM::RolePolicy |
