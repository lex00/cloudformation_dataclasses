"""Messaging resources: EventRule."""

from . import *  # noqa: F403


@cloudformation_dataclass
class EventRuleTarget:
    resource: events.rule.Target
    arn = Join('', [
    'arn:aws:codepipeline:',
    AWS_REGION,
    ':',
    AWS_ACCOUNT_ID,
    ':',
    ref(Pipeline),
])
    role_arn = get_att(EventRole, "Arn")
    id = 'codepipeline-Pipeline'


@cloudformation_dataclass
class EventRule:
    """AWS::Events::Rule resource."""

    resource: events.Rule
    event_pattern = {
        'source': ['aws.codecommit'],
        'detail-type': ['CodeCommit Repository State Change'],
        'resources': [ImportValue(Sub('${CodeBuildStack}-CodeCommitArn'))],
        'detail': {
            'event': [
                'referenceCreated',
                'referenceUpdated',
            ],
            'referenceType': ['branch'],
            'referenceName': ['main'],
        },
    }
    targets = [EventRuleTarget]
