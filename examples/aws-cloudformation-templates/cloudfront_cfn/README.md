# CloudfrontCfn

Migrated from [CloudFront.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m cloudfront_cfn
```

### Validate Template

```bash
python -m cloudfront_cfn --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `AdministratorAccessIAMRole` | AWS::IAM::Role |
| `LambdaEdgeIAMRole` | AWS::IAM::Role |
| `LoggingBucketKMSKey` | AWS::KMS::Key |
| `LoggingBucketKMSKeyAlias` | AWS::KMS::Alias |
| `LoggingBucket` | AWS::S3::Bucket |
| `LoggingBucketPolicy` | AWS::S3::BucketPolicy |
| `EC2Instance` | AWS::EC2::Instance |
| `EC2InstanceSG` | AWS::EC2::SecurityGroup |
| `Tcp8080In` | AWS::EC2::SecurityGroupIngress |
| `OriginALB` | AWS::ElasticLoadBalancingV2::LoadBalancer |
| `OriginALBTG` | AWS::ElasticLoadBalancingV2::TargetGroup |
| `OriginALBHttpsListener` | AWS::ElasticLoadBalancingV2::Listener |
| `OriginALBHttpsListenerRule` | AWS::ElasticLoadBalancingV2::ListenerRule |
| `ALBExternalAccessSG` | AWS::EC2::SecurityGroup |
| `HTTPSTcpIn` | AWS::EC2::SecurityGroupIngress |
| `HTTPTcpIn` | AWS::EC2::SecurityGroupIngress |
| `Tcp8080Out` | AWS::EC2::SecurityGroupEgress |
| `CloudFrontDistribution` | AWS::CloudFront::Distribution |
| `LambdaEdgeFunction` | AWS::Lambda::Function |
| `LambdaEdgeVersion` | AWS::Lambda::Version |
