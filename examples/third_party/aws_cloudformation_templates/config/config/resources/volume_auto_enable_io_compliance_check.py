"""VolumeAutoEnableIOComplianceCheck - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VolumeAutoEnableIOComplianceCheckCode:
    resource: Code
    zip_file = """var aws  = require('aws-sdk');
var config = new aws.ConfigService();
var ec2 = new aws.EC2();
exports.handler = function(event, context) {
    var compliance = evaluateCompliance(event, function(compliance, event) {
        var configurationItem = JSON.parse(event.invokingEvent).configurationItem;
        var putEvaluationsRequest = {
            Evaluations: [{
                ComplianceResourceType: configurationItem.resourceType,
                ComplianceResourceId: configurationItem.resourceId,
                ComplianceType: compliance,
                OrderingTimestamp: configurationItem.configurationItemCaptureTime
            }],
            ResultToken: event.resultToken
        };
        config.putEvaluations(putEvaluationsRequest, function(err, data) {
            if (err) context.fail(err);
            else context.succeed(data);
        });
    });
};
function evaluateCompliance(event, doReturn) {
    var configurationItem = JSON.parse(event.invokingEvent).configurationItem;
    var status = configurationItem.configurationItemStatus;
    if (configurationItem.resourceType !== 'AWS::EC2::Volume' || event.eventLeftScope || (status !== 'OK' && status !== 'ResourceDiscovered'))
        doReturn('NOT_APPLICABLE', event);
    else ec2.describeVolumeAttribute({VolumeId: configurationItem.resourceId, Attribute: 'autoEnableIO'}, function(err, data) {
        if (err) context.fail(err);
        else if (data.AutoEnableIO.Value) doReturn('COMPLIANT', event);
        else doReturn('NON_COMPLIANT', event);
    });
}
"""


@cloudformation_dataclass
class VolumeAutoEnableIOComplianceCheck:
    """AWS::Lambda::Function resource."""

    resource: Function
    code = VolumeAutoEnableIOComplianceCheckCode
    handler = 'index.handler'
    runtime = 'nodejs20.x'
    timeout = '30'
    role = get_att(LambdaExecutionRole, "Arn")
