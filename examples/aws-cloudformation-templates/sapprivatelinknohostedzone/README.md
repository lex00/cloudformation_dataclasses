# Sapprivatelinknohostedzone

Migrated from [SapPrivateLinkNoHostedZone.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m sapprivatelinknohostedzone
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `ASCPrivateLinkCertificate` | AWS::CertificateManager::Certificate |
| `ASCPrivateLinkLambdaRole` | AWS::IAM::Role |
| `ASCPrivateLinkLambdaFunction` | AWS::Lambda::Function |
| `ASCPrivateLinkEnablePrivateDNS` | Custom::CustomResource |
| `ASCPrivateLinkNLB` | AWS::ElasticLoadBalancingV2::LoadBalancer |
| `ASCPrivateLinkTargetGroup` | AWS::ElasticLoadBalancingV2::TargetGroup |
| `ASCPrivateLinkListener` | AWS::ElasticLoadBalancingV2::Listener |
| `ASCPrivateLinkVPCES` | AWS::EC2::VPCEndpointService |
| `ASCPrivateLinkVPCESPermission` | AWS::EC2::VPCEndpointServicePermissions |
