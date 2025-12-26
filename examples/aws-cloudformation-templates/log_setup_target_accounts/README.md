# LogSetupTargetAccounts

Migrated from [log-setup-target-accounts.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m log_setup_target_accounts
```

### Validate Template

```bash
python -m log_setup_target_accounts --validate
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
