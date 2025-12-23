"""FunctionDefinition - AWS::Greengrass::FunctionDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class FunctionDefinition:
    """AWS::Greengrass::FunctionDefinition resource."""

    resource: greengrass.FunctionDefinition
    initial_version = {
        'DefaultConfig': {
            'Execution': {
                LambdaLinuxProcessParams.isolation_mode: 'GreengrassContainer',
            },
        },
        'Functions': [{
            'FunctionArn': ref(GGSampleFunctionVersion),
            'FunctionConfiguration': {
                'EncodingType': 'binary',
                'Environment': {
                    'AccessSysfs': 'false',
                    'Execution': {
                        'IsolationMode': 'GreengrassContainer',
                        'RunAs': {
                            'Gid': '10',
                            'Uid': '1',
                        },
                    },
                    'Variables': {
                        'CORE_NAME': ref(CoreName),
                    },
                },
                'Executable': 'index.py',
                'MemorySize': '65536',
                'Pinned': 'true',
                'Timeout': '300',
            },
            'Id': Join('_', [
    ref(CoreName),
    'sample',
]),
        }],
    }
    name = 'FunctionDefinition'
