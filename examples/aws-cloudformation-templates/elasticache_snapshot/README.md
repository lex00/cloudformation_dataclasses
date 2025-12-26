# ElasticacheSnapshot

Migrated from [Elasticache-snapshot.json](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m elasticache_snapshot
```

### Validate Template

```bash
python -m elasticache_snapshot --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `VPC` | AWS::EC2::VPC |
| `InternetGateway` | AWS::EC2::InternetGateway |
| `PublicInternetRoute` | AWS::EC2::Route |
| `VPCGatewayAttachment` | AWS::EC2::VPCGatewayAttachment |
| `PublicInternetRouteTable` | AWS::EC2::RouteTable |
| `PublicSubnetA` | AWS::EC2::Subnet |
| `PublicSubnetB` | AWS::EC2::Subnet |
| `PublicSubnetARouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `PublicSubnetBRouteTableAssociation` | AWS::EC2::SubnetRouteTableAssociation |
| `RedisParameterGroup` | AWS::ElastiCache::ParameterGroup |
| `RedisSubnetGroup` | AWS::ElastiCache::SubnetGroup |
| `RedisSecurityGroup` | AWS::EC2::SecurityGroup |
| `RedisReplicationGroup` | AWS::ElastiCache::ReplicationGroup |
| `IamRoleLambda` | AWS::IAM::Role |
| `LambdaExecutePermission` | AWS::Lambda::Permission |
| `EnableShapshotTrigger` | Custom::Region |
| `EnableShapshot` | AWS::Lambda::Function |
