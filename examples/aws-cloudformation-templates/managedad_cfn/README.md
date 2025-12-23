# ManagedadCfn

Migrated from [MANAGEDAD.cfn.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m managedad_cfn
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `AWSManagedAD` | AWS::DirectoryService::MicrosoftAD |
| `AWSManagedADDomainMembersSG` | AWS::EC2::SecurityGroup |
| `AWSManagedADLinuxEC2DomainJoinInstanceProfile` | AWS::IAM::InstanceProfile |
| `AWSManagedADLinuxEC2DomainJoinRole` | AWS::IAM::Role |
| `AWSManagedADLinuxEC2SeamlessDomainJoinSecret` | AWS::SecretsManager::Secret |
| `AWSManagedADWindowsEC2DomainJoinInstanceProfile` | AWS::IAM::InstanceProfile |
| `AWSManagedADWindowsEC2DomainJoinRole` | AWS::IAM::Role |
| `DHCPOptions` | AWS::EC2::DHCPOptions |
| `DHCPOptionsVPCAssociation` | AWS::EC2::VPCDHCPOptionsAssociation |
