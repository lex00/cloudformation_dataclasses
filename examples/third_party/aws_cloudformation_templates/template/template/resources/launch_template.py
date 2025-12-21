from __future__ import annotations

"""LaunchTemplate - AWS::EC2::LaunchTemplate resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchTemplateEbsBlockDevice:
    resource: EbsBlockDevice
    iops = 3000
    # Unknown CF key: Throughput = 125
    volume_size = 80
    volume_type = 'gp3'


@cloudformation_dataclass
class LaunchTemplateBlockDeviceMapping:
    resource: BlockDeviceMapping
    device_name = '/dev/xvda'
    ebs = LaunchTemplateEbsBlockDevice


@cloudformation_dataclass
class LaunchTemplateMetadataOptions:
    resource: MetadataOptions
    http_put_response_hop_limit = 2
    http_tokens = 'optional'


@cloudformation_dataclass
class LaunchTemplateAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('ekshandson-ng-${AWS::StackName}-Node')


@cloudformation_dataclass
class LaunchTemplateAssociationParameter1:
    resource: AssociationParameter
    key = 'alpha.eksctl.io/nodegroup-name'
    value = Sub('ng-${AWS::StackName}')


@cloudformation_dataclass
class LaunchTemplateAssociationParameter2:
    resource: AssociationParameter
    key = 'alpha.eksctl.io/nodegroup-type'
    value = 'managed'


@cloudformation_dataclass
class LaunchTemplateTagSpecification:
    resource: TagSpecification
    resource_type = 'instance'
    tags = [LaunchTemplateAssociationParameter, LaunchTemplateAssociationParameter1, LaunchTemplateAssociationParameter2]


@cloudformation_dataclass
class LaunchTemplateAssociationParameter3:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('ekshandson-ng-${AWS::StackName}-Node')


@cloudformation_dataclass
class LaunchTemplateAssociationParameter4:
    resource: AssociationParameter
    key = 'alpha.eksctl.io/nodegroup-name'
    value = Sub('ng-${AWS::StackName}')


@cloudformation_dataclass
class LaunchTemplateAssociationParameter5:
    resource: AssociationParameter
    key = 'alpha.eksctl.io/nodegroup-type'
    value = 'managed'


@cloudformation_dataclass
class LaunchTemplateTagSpecification1:
    resource: TagSpecification
    resource_type = 'volume'
    tags = [LaunchTemplateAssociationParameter3, LaunchTemplateAssociationParameter4, LaunchTemplateAssociationParameter5]


@cloudformation_dataclass
class LaunchTemplateAssociationParameter6:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('ekshandson-ng-${AWS::StackName}-Node')


@cloudformation_dataclass
class LaunchTemplateAssociationParameter7:
    resource: AssociationParameter
    key = 'alpha.eksctl.io/nodegroup-name'
    value = Sub('ng-${AWS::StackName}')


@cloudformation_dataclass
class LaunchTemplateAssociationParameter8:
    resource: AssociationParameter
    key = 'alpha.eksctl.io/nodegroup-type'
    value = 'managed'


@cloudformation_dataclass
class LaunchTemplateTagSpecification2:
    resource: TagSpecification
    resource_type = 'network-interface'
    tags = [LaunchTemplateAssociationParameter6, LaunchTemplateAssociationParameter7, LaunchTemplateAssociationParameter8]


@cloudformation_dataclass
class LaunchTemplateLaunchTemplateData:
    resource: LaunchTemplateData
    block_device_mappings = [LaunchTemplateBlockDeviceMapping]
    metadata_options = LaunchTemplateMetadataOptions
    security_group_ids = [ref("ControlPlaneSecurityGroup")]
    tag_specifications = [LaunchTemplateTagSpecification, LaunchTemplateTagSpecification1, LaunchTemplateTagSpecification2]


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = LaunchTemplateLaunchTemplateData
    launch_template_name = Sub('${AWS::StackName}-LaunchTemplate')
