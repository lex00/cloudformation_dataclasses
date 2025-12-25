# DirectoryAdClients

Migrated from [DIRECTORY-AD-CLIENTS.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m directory_ad_clients
```

### Validate Template

```bash
python -m directory_ad_clients --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `DomainMember1WithInlineSsmAssociation` | AWS::EC2::Instance |
| `DomainMember2WithSsmAssociationInstance` | AWS::EC2::Instance |
| `DomainMember3WithSsmAssociationTag` | AWS::EC2::Instance |
| `DomainMember4LinuxWithSsmAssociationInstance` | AWS::EC2::Instance |
| `JoinDomainAssociationInstances` | AWS::SSM::Association |
| `JoinDomainAssociationTags` | AWS::SSM::Association |
