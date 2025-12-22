"""FunctionDefinition - AWS::Greengrass::FunctionDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class FunctionDefinitionExecution:
    resource: greengrass.Execution
    isolation_mode = 'GreengrassContainer'


@cloudformation_dataclass
class FunctionDefinitionDefaultConfig:
    resource: greengrass.DefaultConfig
    execution = FunctionDefinitionExecution


@cloudformation_dataclass
class FunctionDefinitionRunAs:
    resource: greengrass.RunAs
    gid = '10'
    uid = '1'


@cloudformation_dataclass
class FunctionDefinitionExecution1:
    resource: greengrass.Execution
    isolation_mode = 'GreengrassContainer'
    run_as = FunctionDefinitionRunAs


@cloudformation_dataclass
class FunctionDefinitionEnvironment:
    resource: greengrass.Environment
    access_sysfs = 'false'
    execution = FunctionDefinitionExecution1
    variables = {
        'CORE_NAME': ref(CoreName),
    }


@cloudformation_dataclass
class FunctionDefinitionFunctionConfiguration:
    resource: greengrass.FunctionConfiguration
    encoding_type = 'binary'
    environment = FunctionDefinitionEnvironment
    executable = 'index.py'
    memory_size = '65536'
    pinned = 'true'
    timeout = '300'


@cloudformation_dataclass
class FunctionDefinitionFunction:
    resource: greengrass.Function
    function_arn = ref(GGSampleFunctionVersion)
    function_configuration = FunctionDefinitionFunctionConfiguration
    id = Join('_', [
    ref(CoreName),
    'sample',
])


@cloudformation_dataclass
class FunctionDefinitionFunctionDefinitionVersion:
    resource: greengrass.FunctionDefinitionVersion
    default_config = FunctionDefinitionDefaultConfig
    functions = [FunctionDefinitionFunction]


@cloudformation_dataclass
class FunctionDefinition:
    """AWS::Greengrass::FunctionDefinition resource."""

    resource: greengrass.FunctionDefinition
    initial_version = FunctionDefinitionFunctionDefinitionVersion
    name = 'FunctionDefinition'
