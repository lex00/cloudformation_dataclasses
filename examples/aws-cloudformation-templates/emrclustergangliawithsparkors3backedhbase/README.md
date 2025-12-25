# Emrclustergangliawithsparkors3backedhbase

Migrated from [EMRCLusterGangliaWithSparkOrS3backedHbase.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m emrclustergangliawithsparkors3backedhbase
```

### Validate Template

```bash
python -m emrclustergangliawithsparkors3backedhbase --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `EMRCluster` | AWS::EMR::Cluster |
| `EMRClusterServiceRole` | AWS::IAM::Role |
| `EMRClusterinstanceProfileRole` | AWS::IAM::Role |
| `EMRClusterinstanceProfile` | AWS::IAM::InstanceProfile |
