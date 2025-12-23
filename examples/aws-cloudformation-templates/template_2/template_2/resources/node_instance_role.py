"""NodeInstanceRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NodeInstanceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': FindInMap("ServicePrincipalPartitionMap", AWS_PARTITION, 'EC2'),
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class NodeInstanceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [NodeInstanceRoleAllowStatement0]


@cloudformation_dataclass
class NodeInstanceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${AWS::StackName}-eks-node-role')
    assume_role_policy_document = NodeInstanceRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKSWorkerNodePolicy'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKS_CNI_Policy'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMManagedInstanceCore')]
    path = '/'
