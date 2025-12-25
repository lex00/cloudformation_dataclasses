"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class StackName:
    """The name of the parent cluster stack that you created. Necessary to locate and reference resources created by that stack."""

    resource: Parameter
    type = STRING
    description = 'The name of the parent cluster stack that you created. Necessary to locate and reference resources created by that stack.'
    default = 'production'


@cloudformation_dataclass
class ServiceName:
    """A name for the service"""

    resource: Parameter
    type = STRING
    description = 'A name for the service'
    default = 'nginx'


@cloudformation_dataclass
class ImageUrl:
    """The url of a docker image that contains the application process that will handle the traffic for this service"""

    resource: Parameter
    type = STRING
    description = 'The url of a docker image that contains the application process that will handle the traffic for this service'
    default = 'nginx'


@cloudformation_dataclass
class ContainerPort:
    """What port number the application inside the docker container is binding to"""

    resource: Parameter
    type = NUMBER
    description = 'What port number the application inside the docker container is binding to'
    default = 80


@cloudformation_dataclass
class ContainerCpu:
    """How much CPU to give the container. 1024 is 1 CPU"""

    resource: Parameter
    type = NUMBER
    description = 'How much CPU to give the container. 1024 is 1 CPU'
    default = 256


@cloudformation_dataclass
class ContainerMemory:
    """How much memory in megabytes to give the container"""

    resource: Parameter
    type = NUMBER
    description = 'How much memory in megabytes to give the container'
    default = 512


@cloudformation_dataclass
class Path:
    """A path on the public load balancer that this service should be connected to. Use * to send all load balancer traffic to this service."""

    resource: Parameter
    type = STRING
    description = 'A path on the public load balancer that this service should be connected to. Use * to send all load balancer traffic to this service.'
    default = '*'


@cloudformation_dataclass
class Priority:
    """The priority for the routing rule added to the load balancer. This only applies if your have multiple services which have been assigned to different paths on the load balancer."""

    resource: Parameter
    type = NUMBER
    description = 'The priority for the routing rule added to the load balancer. This only applies if your have multiple services which have been assigned to different paths on the load balancer.'
    default = 1


@cloudformation_dataclass
class DesiredCount:
    """How many copies of the service task to run"""

    resource: Parameter
    type = NUMBER
    description = 'How many copies of the service task to run'
    default = 2


@cloudformation_dataclass
class Role:
    """(Optional) An IAM role to give the service's containers if the code within needs to access other AWS resources like S3 buckets, DynamoDB tables, etc"""

    resource: Parameter
    type = STRING
    description = "(Optional) An IAM role to give the service's containers if the code within needs to access other AWS resources like S3 buckets, DynamoDB tables, etc"
    default = ''


@cloudformation_dataclass
class HasCustomRoleCondition:
    resource: TemplateCondition
    logical_id = 'HasCustomRole'
    expression = Not(Equals(ref(Role), ''))
