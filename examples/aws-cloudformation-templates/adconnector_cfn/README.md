# AdconnectorCfn

Migrated from [ADCONNECTOR.cfn.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates).

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
uv run python -m adconnector_cfn
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `ADConnectorDomainMembersSG` | AWS::EC2::SecurityGroup |
| `ADConnectorLambdaFunction` | AWS::Lambda::Function |
| `ADConnectorLambdaLogsLogGroup` | AWS::Logs::LogGroup |
| `ADConnectorLambdaRole` | AWS::IAM::Role |
| `ADConnectorLinuxEC2DomainJoinInstanceProfile` | AWS::IAM::InstanceProfile |
| `ADConnectorLinuxEC2DomainJoinRole` | AWS::IAM::Role |
| `ADConnectorLinuxEC2SeamlessDomainJoinSecret` | AWS::SecretsManager::Secret |
| `ADConnectorResource` | Custom::ADConnectorResource |
| `ADConnectorServiceAccountSecret` | AWS::SecretsManager::Secret |
| `ADConnectorWindowsEC2DomainJoinInstanceProfile` | AWS::IAM::InstanceProfile |
| `ADConnectorWindowsEC2DomainJoinRole` | AWS::IAM::Role |
| `DHCPOptions` | AWS::EC2::DHCPOptions |
| `DHCPOptionsVPCAssociation` | AWS::EC2::VPCDHCPOptionsAssociation |
