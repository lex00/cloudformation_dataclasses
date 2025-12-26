# Sapprivatelink

Migrated from [SapPrivateLink.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m sapprivatelink
```

### Validate Template

```bash
python -m sapprivatelink --validate
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
