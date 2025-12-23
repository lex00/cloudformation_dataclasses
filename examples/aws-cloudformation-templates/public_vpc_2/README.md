# PublicVpc2

Migrated from [public-vpc_2.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m public_vpc_2
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPC` | AWS::EC2::VPC |
| `PublicSubnetOne` | AWS::EC2::Subnet |
| `PublicSubnetTwo` | AWS::EC2::Subnet |
| `InternetGateway` | AWS::EC2::InternetGateway |
| `GatewayAttachement` | AWS::EC2::VPCGatewayAttachment |
| `PublicRouteTable` | AWS::EC2::RouteTable |
| `PublicRoute` | AWS::EC2::Route |
| `PublicSubnetOneRouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicSubnetTwoRouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `ECSCluster` | AWS::ECS::Cluster |
| `FargateContainerSecurityGroup` | AWS::EC2::SecurityGroup |
| `EcsSecurityGroupIngressFromPublicALB` | AWS::EC2::SecurityGroupIngress |
| `EcsSecurityGroupIngressFromSelf` | AWS::EC2::SecurityGroupIngress |
| `PublicLoadBalancerSG` | AWS::EC2::SecurityGroup |
| `PublicLoadBalancer` | AWS::ElasticLoadBalancingV2::LoadBalancer |
| `DummyTargetGroupPublic` | AWS::ElasticLoadBalancingV2::TargetGroup |
| `PublicLoadBalancerListener` | AWS::ElasticLoadBalancingV2::Listener |
| `ECSRole` | AWS::IAM::Role |
| `ECSTaskExecutionRole` | AWS::IAM::Role |
