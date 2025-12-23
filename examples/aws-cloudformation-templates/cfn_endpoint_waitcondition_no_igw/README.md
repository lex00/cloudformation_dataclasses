# CfnEndpointWaitconditionNoIgw

Migrated from [cfn-endpoint-waitcondition-no-igw.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m cfn_endpoint_waitcondition_no_igw
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPC` | AWS::EC2::VPC |
| `CfnEndpoint` | AWS::EC2::VPCEndpoint |
| `S3Endpoint` | AWS::EC2::VPCEndpoint |
| `PrivateSubnet1` | AWS::EC2::Subnet |
| `PrivateSubnet2` | AWS::EC2::Subnet |
| `PrivateRouteTable1` | AWS::EC2::RouteTable |
| `PrivateSubnet1RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateRouteTable2` | AWS::EC2::RouteTable |
| `PrivateSubnet2RouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PrivateInstance` | AWS::EC2::Instance |
| `PrivateSG` | AWS::EC2::SecurityGroup |
| `EndpointSG` | AWS::EC2::SecurityGroup |
| `PrivateWaitHandle` | AWS::CloudFormation::WaitConditionHandle |
| `PrivateWaitCondition` | AWS::CloudFormation::WaitCondition |
