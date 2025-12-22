"""GGSampleFunction - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GGSampleFunctionCode:
    resource: lambda_.Code
    zip_file = """import os
from threading import Timer
import greengrasssdk


counter = 0
client = greengrasssdk.client('iot-data')


def telemetry():
    '''Publish incrementing value to telemetry topic every 2 seconds'''
    global counter
    counter += 1
    client.publish(
        topic='{}/telem'.format(os.environ['CORE_NAME']),
        payload='Example telemetry counter, value: {}'.format(counter)
    )
    Timer(5, telemetry).start()
# Call telemetry() to start telemetry publish
telemetry()


def function_handler(event, context):
    '''Echo message on /in topic to /out topic'''
    client.publish(
        topic='{}/out'.format(os.environ['CORE_NAME']),
        payload=event
    )
"""


@cloudformation_dataclass
class GGSampleFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    code = GGSampleFunctionCode
    description = 'Long running lambda that provides telemetry and pub/sub echo'
    function_name = Join('_', [
    ref(CoreName),
    'sample',
])
    handler = 'index.function_handler'
    role = get_att(LambdaExecutionRole, "Arn")
    runtime = 'python3.12'
    timeout = 60
