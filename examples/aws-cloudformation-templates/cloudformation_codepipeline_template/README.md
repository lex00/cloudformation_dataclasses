# CloudformationCodepipelineTemplate

Migrated from [cloudformation-codepipeline-template.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m cloudformation_codepipeline_template
```

### Validate Template

```bash
python -m cloudformation_codepipeline_template --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `PipelineRole` | AWS::IAM::Role |
| `EventRole` | AWS::IAM::Role |
| `EventRule` | AWS::Events::Rule |
| `Pipeline` | AWS::CodePipeline::Pipeline |
