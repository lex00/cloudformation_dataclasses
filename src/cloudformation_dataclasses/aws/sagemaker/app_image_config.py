"""PropertyTypes for AWS::SageMaker::AppImageConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


# Service Constants (auto-generated from botocore)
class AccountDefaultStatus:
    """AccountDefaultStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class ActionStatus:
    """ActionStatus enum values."""

    UNKNOWN = "Unknown"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"


class ActivationState:
    """ActivationState enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ActiveClusterOperationName:
    """ActiveClusterOperationName enum values."""

    SCALING = "Scaling"


class AdditionalS3DataSourceDataType:
    """AdditionalS3DataSourceDataType enum values."""

    S3OBJECT = "S3Object"
    S3PREFIX = "S3Prefix"


class AggregationTransformationValue:
    """AggregationTransformationValue enum values."""

    SUM = "sum"
    AVG = "avg"
    FIRST = "first"
    MIN = "min"
    MAX = "max"


class AlgorithmSortBy:
    """AlgorithmSortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class AlgorithmStatus:
    """AlgorithmStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    DELETING = "Deleting"


class AppImageConfigSortKey:
    """AppImageConfigSortKey enum values."""

    CREATIONTIME = "CreationTime"
    LASTMODIFIEDTIME = "LastModifiedTime"
    NAME = "Name"


class AppInstanceType:
    """AppInstanceType enum values."""

    SYSTEM = "system"
    ML_T3_MICRO = "ml.t3.micro"
    ML_T3_SMALL = "ml.t3.small"
    ML_T3_MEDIUM = "ml.t3.medium"
    ML_T3_LARGE = "ml.t3.large"
    ML_T3_XLARGE = "ml.t3.xlarge"
    ML_T3_2XLARGE = "ml.t3.2xlarge"
    ML_M5_LARGE = "ml.m5.large"
    ML_M5_XLARGE = "ml.m5.xlarge"
    ML_M5_2XLARGE = "ml.m5.2xlarge"
    ML_M5_4XLARGE = "ml.m5.4xlarge"
    ML_M5_8XLARGE = "ml.m5.8xlarge"
    ML_M5_12XLARGE = "ml.m5.12xlarge"
    ML_M5_16XLARGE = "ml.m5.16xlarge"
    ML_M5_24XLARGE = "ml.m5.24xlarge"
    ML_M5D_LARGE = "ml.m5d.large"
    ML_M5D_XLARGE = "ml.m5d.xlarge"
    ML_M5D_2XLARGE = "ml.m5d.2xlarge"
    ML_M5D_4XLARGE = "ml.m5d.4xlarge"
    ML_M5D_8XLARGE = "ml.m5d.8xlarge"
    ML_M5D_12XLARGE = "ml.m5d.12xlarge"
    ML_M5D_16XLARGE = "ml.m5d.16xlarge"
    ML_M5D_24XLARGE = "ml.m5d.24xlarge"
    ML_C5_LARGE = "ml.c5.large"
    ML_C5_XLARGE = "ml.c5.xlarge"
    ML_C5_2XLARGE = "ml.c5.2xlarge"
    ML_C5_4XLARGE = "ml.c5.4xlarge"
    ML_C5_9XLARGE = "ml.c5.9xlarge"
    ML_C5_12XLARGE = "ml.c5.12xlarge"
    ML_C5_18XLARGE = "ml.c5.18xlarge"
    ML_C5_24XLARGE = "ml.c5.24xlarge"
    ML_P3_2XLARGE = "ml.p3.2xlarge"
    ML_P3_8XLARGE = "ml.p3.8xlarge"
    ML_P3_16XLARGE = "ml.p3.16xlarge"
    ML_P3DN_24XLARGE = "ml.p3dn.24xlarge"
    ML_G4DN_XLARGE = "ml.g4dn.xlarge"
    ML_G4DN_2XLARGE = "ml.g4dn.2xlarge"
    ML_G4DN_4XLARGE = "ml.g4dn.4xlarge"
    ML_G4DN_8XLARGE = "ml.g4dn.8xlarge"
    ML_G4DN_12XLARGE = "ml.g4dn.12xlarge"
    ML_G4DN_16XLARGE = "ml.g4dn.16xlarge"
    ML_R5_LARGE = "ml.r5.large"
    ML_R5_XLARGE = "ml.r5.xlarge"
    ML_R5_2XLARGE = "ml.r5.2xlarge"
    ML_R5_4XLARGE = "ml.r5.4xlarge"
    ML_R5_8XLARGE = "ml.r5.8xlarge"
    ML_R5_12XLARGE = "ml.r5.12xlarge"
    ML_R5_16XLARGE = "ml.r5.16xlarge"
    ML_R5_24XLARGE = "ml.r5.24xlarge"
    ML_G5_XLARGE = "ml.g5.xlarge"
    ML_G5_2XLARGE = "ml.g5.2xlarge"
    ML_G5_4XLARGE = "ml.g5.4xlarge"
    ML_G5_8XLARGE = "ml.g5.8xlarge"
    ML_G5_16XLARGE = "ml.g5.16xlarge"
    ML_G5_12XLARGE = "ml.g5.12xlarge"
    ML_G5_24XLARGE = "ml.g5.24xlarge"
    ML_G5_48XLARGE = "ml.g5.48xlarge"
    ML_G6_XLARGE = "ml.g6.xlarge"
    ML_G6_2XLARGE = "ml.g6.2xlarge"
    ML_G6_4XLARGE = "ml.g6.4xlarge"
    ML_G6_8XLARGE = "ml.g6.8xlarge"
    ML_G6_12XLARGE = "ml.g6.12xlarge"
    ML_G6_16XLARGE = "ml.g6.16xlarge"
    ML_G6_24XLARGE = "ml.g6.24xlarge"
    ML_G6_48XLARGE = "ml.g6.48xlarge"
    ML_G6E_XLARGE = "ml.g6e.xlarge"
    ML_G6E_2XLARGE = "ml.g6e.2xlarge"
    ML_G6E_4XLARGE = "ml.g6e.4xlarge"
    ML_G6E_8XLARGE = "ml.g6e.8xlarge"
    ML_G6E_12XLARGE = "ml.g6e.12xlarge"
    ML_G6E_16XLARGE = "ml.g6e.16xlarge"
    ML_G6E_24XLARGE = "ml.g6e.24xlarge"
    ML_G6E_48XLARGE = "ml.g6e.48xlarge"
    ML_GEOSPATIAL_INTERACTIVE = "ml.geospatial.interactive"
    ML_P4D_24XLARGE = "ml.p4d.24xlarge"
    ML_P4DE_24XLARGE = "ml.p4de.24xlarge"
    ML_TRN1_2XLARGE = "ml.trn1.2xlarge"
    ML_TRN1_32XLARGE = "ml.trn1.32xlarge"
    ML_TRN1N_32XLARGE = "ml.trn1n.32xlarge"
    ML_P5_48XLARGE = "ml.p5.48xlarge"
    ML_P5EN_48XLARGE = "ml.p5en.48xlarge"
    ML_P6_B200_48XLARGE = "ml.p6-b200.48xlarge"
    ML_M6I_LARGE = "ml.m6i.large"
    ML_M6I_XLARGE = "ml.m6i.xlarge"
    ML_M6I_2XLARGE = "ml.m6i.2xlarge"
    ML_M6I_4XLARGE = "ml.m6i.4xlarge"
    ML_M6I_8XLARGE = "ml.m6i.8xlarge"
    ML_M6I_12XLARGE = "ml.m6i.12xlarge"
    ML_M6I_16XLARGE = "ml.m6i.16xlarge"
    ML_M6I_24XLARGE = "ml.m6i.24xlarge"
    ML_M6I_32XLARGE = "ml.m6i.32xlarge"
    ML_M7I_LARGE = "ml.m7i.large"
    ML_M7I_XLARGE = "ml.m7i.xlarge"
    ML_M7I_2XLARGE = "ml.m7i.2xlarge"
    ML_M7I_4XLARGE = "ml.m7i.4xlarge"
    ML_M7I_8XLARGE = "ml.m7i.8xlarge"
    ML_M7I_12XLARGE = "ml.m7i.12xlarge"
    ML_M7I_16XLARGE = "ml.m7i.16xlarge"
    ML_M7I_24XLARGE = "ml.m7i.24xlarge"
    ML_M7I_48XLARGE = "ml.m7i.48xlarge"
    ML_C6I_LARGE = "ml.c6i.large"
    ML_C6I_XLARGE = "ml.c6i.xlarge"
    ML_C6I_2XLARGE = "ml.c6i.2xlarge"
    ML_C6I_4XLARGE = "ml.c6i.4xlarge"
    ML_C6I_8XLARGE = "ml.c6i.8xlarge"
    ML_C6I_12XLARGE = "ml.c6i.12xlarge"
    ML_C6I_16XLARGE = "ml.c6i.16xlarge"
    ML_C6I_24XLARGE = "ml.c6i.24xlarge"
    ML_C6I_32XLARGE = "ml.c6i.32xlarge"
    ML_C7I_LARGE = "ml.c7i.large"
    ML_C7I_XLARGE = "ml.c7i.xlarge"
    ML_C7I_2XLARGE = "ml.c7i.2xlarge"
    ML_C7I_4XLARGE = "ml.c7i.4xlarge"
    ML_C7I_8XLARGE = "ml.c7i.8xlarge"
    ML_C7I_12XLARGE = "ml.c7i.12xlarge"
    ML_C7I_16XLARGE = "ml.c7i.16xlarge"
    ML_C7I_24XLARGE = "ml.c7i.24xlarge"
    ML_C7I_48XLARGE = "ml.c7i.48xlarge"
    ML_R6I_LARGE = "ml.r6i.large"
    ML_R6I_XLARGE = "ml.r6i.xlarge"
    ML_R6I_2XLARGE = "ml.r6i.2xlarge"
    ML_R6I_4XLARGE = "ml.r6i.4xlarge"
    ML_R6I_8XLARGE = "ml.r6i.8xlarge"
    ML_R6I_12XLARGE = "ml.r6i.12xlarge"
    ML_R6I_16XLARGE = "ml.r6i.16xlarge"
    ML_R6I_24XLARGE = "ml.r6i.24xlarge"
    ML_R6I_32XLARGE = "ml.r6i.32xlarge"
    ML_R7I_LARGE = "ml.r7i.large"
    ML_R7I_XLARGE = "ml.r7i.xlarge"
    ML_R7I_2XLARGE = "ml.r7i.2xlarge"
    ML_R7I_4XLARGE = "ml.r7i.4xlarge"
    ML_R7I_8XLARGE = "ml.r7i.8xlarge"
    ML_R7I_12XLARGE = "ml.r7i.12xlarge"
    ML_R7I_16XLARGE = "ml.r7i.16xlarge"
    ML_R7I_24XLARGE = "ml.r7i.24xlarge"
    ML_R7I_48XLARGE = "ml.r7i.48xlarge"
    ML_M6ID_LARGE = "ml.m6id.large"
    ML_M6ID_XLARGE = "ml.m6id.xlarge"
    ML_M6ID_2XLARGE = "ml.m6id.2xlarge"
    ML_M6ID_4XLARGE = "ml.m6id.4xlarge"
    ML_M6ID_8XLARGE = "ml.m6id.8xlarge"
    ML_M6ID_12XLARGE = "ml.m6id.12xlarge"
    ML_M6ID_16XLARGE = "ml.m6id.16xlarge"
    ML_M6ID_24XLARGE = "ml.m6id.24xlarge"
    ML_M6ID_32XLARGE = "ml.m6id.32xlarge"
    ML_C6ID_LARGE = "ml.c6id.large"
    ML_C6ID_XLARGE = "ml.c6id.xlarge"
    ML_C6ID_2XLARGE = "ml.c6id.2xlarge"
    ML_C6ID_4XLARGE = "ml.c6id.4xlarge"
    ML_C6ID_8XLARGE = "ml.c6id.8xlarge"
    ML_C6ID_12XLARGE = "ml.c6id.12xlarge"
    ML_C6ID_16XLARGE = "ml.c6id.16xlarge"
    ML_C6ID_24XLARGE = "ml.c6id.24xlarge"
    ML_C6ID_32XLARGE = "ml.c6id.32xlarge"
    ML_R6ID_LARGE = "ml.r6id.large"
    ML_R6ID_XLARGE = "ml.r6id.xlarge"
    ML_R6ID_2XLARGE = "ml.r6id.2xlarge"
    ML_R6ID_4XLARGE = "ml.r6id.4xlarge"
    ML_R6ID_8XLARGE = "ml.r6id.8xlarge"
    ML_R6ID_12XLARGE = "ml.r6id.12xlarge"
    ML_R6ID_16XLARGE = "ml.r6id.16xlarge"
    ML_R6ID_24XLARGE = "ml.r6id.24xlarge"
    ML_R6ID_32XLARGE = "ml.r6id.32xlarge"


class AppNetworkAccessType:
    """AppNetworkAccessType enum values."""

    PUBLICINTERNETONLY = "PublicInternetOnly"
    VPCONLY = "VpcOnly"


class AppSecurityGroupManagement:
    """AppSecurityGroupManagement enum values."""

    SERVICE = "Service"
    CUSTOMER = "Customer"


class AppSortKey:
    """AppSortKey enum values."""

    CREATIONTIME = "CreationTime"


class AppStatus:
    """AppStatus enum values."""

    DELETED = "Deleted"
    DELETING = "Deleting"
    FAILED = "Failed"
    INSERVICE = "InService"
    PENDING = "Pending"


class AppType:
    """AppType enum values."""

    JUPYTERSERVER = "JupyterServer"
    KERNELGATEWAY = "KernelGateway"
    DETAILEDPROFILER = "DetailedProfiler"
    TENSORBOARD = "TensorBoard"
    CODEEDITOR = "CodeEditor"
    JUPYTERLAB = "JupyterLab"
    RSTUDIOSERVERPRO = "RStudioServerPro"
    RSESSIONGATEWAY = "RSessionGateway"
    CANVAS = "Canvas"


class ArtifactSourceIdType:
    """ArtifactSourceIdType enum values."""

    MD5HASH = "MD5Hash"
    S3ETAG = "S3ETag"
    S3VERSION = "S3Version"
    CUSTOM = "Custom"


class AssemblyType:
    """AssemblyType enum values."""

    NONE = "None"
    LINE = "Line"


class AssociationEdgeType:
    """AssociationEdgeType enum values."""

    CONTRIBUTEDTO = "ContributedTo"
    ASSOCIATEDWITH = "AssociatedWith"
    DERIVEDFROM = "DerivedFrom"
    PRODUCED = "Produced"
    SAMEAS = "SameAs"


class AsyncNotificationTopicTypes:
    """AsyncNotificationTopicTypes enum values."""

    SUCCESS_NOTIFICATION_TOPIC = "SUCCESS_NOTIFICATION_TOPIC"
    ERROR_NOTIFICATION_TOPIC = "ERROR_NOTIFICATION_TOPIC"


class AthenaResultCompressionType:
    """AthenaResultCompressionType enum values."""

    GZIP = "GZIP"
    SNAPPY = "SNAPPY"
    ZLIB = "ZLIB"


class AthenaResultFormat:
    """AthenaResultFormat enum values."""

    PARQUET = "PARQUET"
    ORC = "ORC"
    AVRO = "AVRO"
    JSON = "JSON"
    TEXTFILE = "TEXTFILE"


class AuthMode:
    """AuthMode enum values."""

    SSO = "SSO"
    IAM = "IAM"


class AutoMLAlgorithm:
    """AutoMLAlgorithm enum values."""

    XGBOOST = "xgboost"
    LINEAR_LEARNER = "linear-learner"
    MLP = "mlp"
    LIGHTGBM = "lightgbm"
    CATBOOST = "catboost"
    RANDOMFOREST = "randomforest"
    EXTRA_TREES = "extra-trees"
    NN_TORCH = "nn-torch"
    FASTAI = "fastai"
    CNN_QR = "cnn-qr"
    DEEPAR = "deepar"
    PROPHET = "prophet"
    NPTS = "npts"
    ARIMA = "arima"
    ETS = "ets"


class AutoMLChannelType:
    """AutoMLChannelType enum values."""

    TRAINING = "training"
    VALIDATION = "validation"


class AutoMLJobObjectiveType:
    """AutoMLJobObjectiveType enum values."""

    MAXIMIZE = "Maximize"
    MINIMIZE = "Minimize"


class AutoMLJobSecondaryStatus:
    """AutoMLJobSecondaryStatus enum values."""

    STARTING = "Starting"
    MAXCANDIDATESREACHED = "MaxCandidatesReached"
    FAILED = "Failed"
    STOPPED = "Stopped"
    MAXAUTOMLJOBRUNTIMEREACHED = "MaxAutoMLJobRuntimeReached"
    STOPPING = "Stopping"
    CANDIDATEDEFINITIONSGENERATED = "CandidateDefinitionsGenerated"
    COMPLETED = "Completed"
    EXPLAINABILITYERROR = "ExplainabilityError"
    DEPLOYINGMODEL = "DeployingModel"
    MODELDEPLOYMENTERROR = "ModelDeploymentError"
    GENERATINGMODELINSIGHTSREPORT = "GeneratingModelInsightsReport"
    MODELINSIGHTSERROR = "ModelInsightsError"
    ANALYZINGDATA = "AnalyzingData"
    FEATUREENGINEERING = "FeatureEngineering"
    MODELTUNING = "ModelTuning"
    GENERATINGEXPLAINABILITYREPORT = "GeneratingExplainabilityReport"
    TRAININGMODELS = "TrainingModels"
    PRETRAINING = "PreTraining"


class AutoMLJobStatus:
    """AutoMLJobStatus enum values."""

    COMPLETED = "Completed"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    STOPPED = "Stopped"
    STOPPING = "Stopping"


class AutoMLMetricEnum:
    """AutoMLMetricEnum enum values."""

    ACCURACY = "Accuracy"
    MSE = "MSE"
    F1 = "F1"
    F1MACRO = "F1macro"
    AUC = "AUC"
    RMSE = "RMSE"
    BALANCEDACCURACY = "BalancedAccuracy"
    R2 = "R2"
    RECALL = "Recall"
    RECALLMACRO = "RecallMacro"
    PRECISION = "Precision"
    PRECISIONMACRO = "PrecisionMacro"
    MAE = "MAE"
    MAPE = "MAPE"
    MASE = "MASE"
    WAPE = "WAPE"
    AVERAGEWEIGHTEDQUANTILELOSS = "AverageWeightedQuantileLoss"


class AutoMLMetricExtendedEnum:
    """AutoMLMetricExtendedEnum enum values."""

    ACCURACY = "Accuracy"
    MSE = "MSE"
    F1 = "F1"
    F1MACRO = "F1macro"
    AUC = "AUC"
    RMSE = "RMSE"
    MAE = "MAE"
    R2 = "R2"
    BALANCEDACCURACY = "BalancedAccuracy"
    PRECISION = "Precision"
    PRECISIONMACRO = "PrecisionMacro"
    RECALL = "Recall"
    RECALLMACRO = "RecallMacro"
    LOGLOSS = "LogLoss"
    INFERENCELATENCY = "InferenceLatency"
    MAPE = "MAPE"
    MASE = "MASE"
    WAPE = "WAPE"
    AVERAGEWEIGHTEDQUANTILELOSS = "AverageWeightedQuantileLoss"
    ROUGE1 = "Rouge1"
    ROUGE2 = "Rouge2"
    ROUGEL = "RougeL"
    ROUGELSUM = "RougeLSum"
    PERPLEXITY = "Perplexity"
    VALIDATIONLOSS = "ValidationLoss"
    TRAININGLOSS = "TrainingLoss"


class AutoMLMode:
    """AutoMLMode enum values."""

    AUTO = "AUTO"
    ENSEMBLING = "ENSEMBLING"
    HYPERPARAMETER_TUNING = "HYPERPARAMETER_TUNING"


class AutoMLProblemTypeConfigName:
    """AutoMLProblemTypeConfigName enum values."""

    IMAGECLASSIFICATION = "ImageClassification"
    TEXTCLASSIFICATION = "TextClassification"
    TIMESERIESFORECASTING = "TimeSeriesForecasting"
    TABULAR = "Tabular"
    TEXTGENERATION = "TextGeneration"


class AutoMLProcessingUnit:
    """AutoMLProcessingUnit enum values."""

    CPU = "CPU"
    GPU = "GPU"


class AutoMLS3DataType:
    """AutoMLS3DataType enum values."""

    MANIFESTFILE = "ManifestFile"
    S3PREFIX = "S3Prefix"
    AUGMENTEDMANIFESTFILE = "AugmentedManifestFile"


class AutoMLSortBy:
    """AutoMLSortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class AutoMLSortOrder:
    """AutoMLSortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class AutoMountHomeEFS:
    """AutoMountHomeEFS enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    DEFAULTASDOMAIN = "DefaultAsDomain"


class AutotuneMode:
    """AutotuneMode enum values."""

    ENABLED = "Enabled"


class AwsManagedHumanLoopRequestSource:
    """AwsManagedHumanLoopRequestSource enum values."""

    AWS_REKOGNITION_DETECTMODERATIONLABELS_IMAGE_V3 = "AWS/Rekognition/DetectModerationLabels/Image/V3"
    AWS_TEXTRACT_ANALYZEDOCUMENT_FORMS_V1 = "AWS/Textract/AnalyzeDocument/Forms/V1"


class BatchAddClusterNodesErrorCode:
    """BatchAddClusterNodesErrorCode enum values."""

    INSTANCEGROUPNOTFOUND = "InstanceGroupNotFound"
    INVALIDINSTANCEGROUPSTATUS = "InvalidInstanceGroupStatus"


class BatchDeleteClusterNodesErrorCode:
    """BatchDeleteClusterNodesErrorCode enum values."""

    NODEIDNOTFOUND = "NodeIdNotFound"
    INVALIDNODESTATUS = "InvalidNodeStatus"
    NODEIDINUSE = "NodeIdInUse"


class BatchRebootClusterNodesErrorCode:
    """BatchRebootClusterNodesErrorCode enum values."""

    INSTANCEIDNOTFOUND = "InstanceIdNotFound"
    INVALIDINSTANCESTATUS = "InvalidInstanceStatus"
    INSTANCEIDINUSE = "InstanceIdInUse"
    INTERNALSERVERERROR = "InternalServerError"


class BatchReplaceClusterNodesErrorCode:
    """BatchReplaceClusterNodesErrorCode enum values."""

    INSTANCEIDNOTFOUND = "InstanceIdNotFound"
    INVALIDINSTANCESTATUS = "InvalidInstanceStatus"
    INSTANCEIDINUSE = "InstanceIdInUse"
    INTERNALSERVERERROR = "InternalServerError"


class BatchStrategy:
    """BatchStrategy enum values."""

    MULTIRECORD = "MultiRecord"
    SINGLERECORD = "SingleRecord"


class BooleanOperator:
    """BooleanOperator enum values."""

    AND = "And"
    OR = "Or"


class CandidateSortBy:
    """CandidateSortBy enum values."""

    CREATIONTIME = "CreationTime"
    STATUS = "Status"
    FINALOBJECTIVEMETRICVALUE = "FinalObjectiveMetricValue"


class CandidateStatus:
    """CandidateStatus enum values."""

    COMPLETED = "Completed"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    STOPPED = "Stopped"
    STOPPING = "Stopping"


class CandidateStepType:
    """CandidateStepType enum values."""

    AWS_SAGEMAKER_TRAININGJOB = "AWS::SageMaker::TrainingJob"
    AWS_SAGEMAKER_TRANSFORMJOB = "AWS::SageMaker::TransformJob"
    AWS_SAGEMAKER_PROCESSINGJOB = "AWS::SageMaker::ProcessingJob"


class CapacityReservationPreference:
    """CapacityReservationPreference enum values."""

    CAPACITY_RESERVATIONS_ONLY = "capacity-reservations-only"


class CapacityReservationType:
    """CapacityReservationType enum values."""

    ODCR = "ODCR"
    CRG = "CRG"


class CapacitySizeType:
    """CapacitySizeType enum values."""

    INSTANCE_COUNT = "INSTANCE_COUNT"
    CAPACITY_PERCENT = "CAPACITY_PERCENT"


class CaptureMode:
    """CaptureMode enum values."""

    INPUT = "Input"
    OUTPUT = "Output"
    INPUTANDOUTPUT = "InputAndOutput"


class CaptureStatus:
    """CaptureStatus enum values."""

    STARTED = "Started"
    STOPPED = "Stopped"


class ClarifyFeatureType:
    """ClarifyFeatureType enum values."""

    NUMERICAL = "numerical"
    CATEGORICAL = "categorical"
    TEXT = "text"


class ClarifyTextGranularity:
    """ClarifyTextGranularity enum values."""

    TOKEN = "token"
    SENTENCE = "sentence"
    PARAGRAPH = "paragraph"


class ClarifyTextLanguage:
    """ClarifyTextLanguage enum values."""

    AF = "af"
    SQ = "sq"
    AR = "ar"
    HY = "hy"
    EU = "eu"
    BN = "bn"
    BG = "bg"
    CA = "ca"
    ZH = "zh"
    HR = "hr"
    CS = "cs"
    DA = "da"
    NL = "nl"
    EN = "en"
    ET = "et"
    FI = "fi"
    FR = "fr"
    DE = "de"
    EL = "el"
    GU = "gu"
    HE = "he"
    HI = "hi"
    HU = "hu"
    IS = "is"
    ID = "id"
    GA = "ga"
    IT = "it"
    KN = "kn"
    KY = "ky"
    LV = "lv"
    LT = "lt"
    LB = "lb"
    MK = "mk"
    ML = "ml"
    MR = "mr"
    NE = "ne"
    NB = "nb"
    FA = "fa"
    PL = "pl"
    PT = "pt"
    RO = "ro"
    RU = "ru"
    SA = "sa"
    SR = "sr"
    TN = "tn"
    SI = "si"
    SK = "sk"
    SL = "sl"
    ES = "es"
    SV = "sv"
    TL = "tl"
    TA = "ta"
    TT = "tt"
    TE = "te"
    TR = "tr"
    UK = "uk"
    UR = "ur"
    YO = "yo"
    LIJ = "lij"
    XX = "xx"


class ClusterAutoScalerType:
    """ClusterAutoScalerType enum values."""

    KARPENTER = "Karpenter"


class ClusterAutoScalingMode:
    """ClusterAutoScalingMode enum values."""

    ENABLE = "Enable"
    DISABLE = "Disable"


class ClusterAutoScalingStatus:
    """ClusterAutoScalingStatus enum values."""

    INSERVICE = "InService"
    FAILED = "Failed"
    CREATING = "Creating"
    DELETING = "Deleting"


class ClusterCapacityType:
    """ClusterCapacityType enum values."""

    SPOT = "Spot"
    ONDEMAND = "OnDemand"


class ClusterConfigMode:
    """ClusterConfigMode enum values."""

    ENABLE = "Enable"
    DISABLE = "Disable"


class ClusterEventResourceType:
    """ClusterEventResourceType enum values."""

    CLUSTER = "Cluster"
    INSTANCEGROUP = "InstanceGroup"
    INSTANCE = "Instance"


class ClusterInstanceStatus:
    """ClusterInstanceStatus enum values."""

    RUNNING = "Running"
    FAILURE = "Failure"
    PENDING = "Pending"
    SHUTTINGDOWN = "ShuttingDown"
    SYSTEMUPDATING = "SystemUpdating"
    DEEPHEALTHCHECKINPROGRESS = "DeepHealthCheckInProgress"
    NOTFOUND = "NotFound"


class ClusterInstanceType:
    """ClusterInstanceType enum values."""

    ML_P4D_24XLARGE = "ml.p4d.24xlarge"
    ML_P4DE_24XLARGE = "ml.p4de.24xlarge"
    ML_P5_48XLARGE = "ml.p5.48xlarge"
    ML_P5_4XLARGE = "ml.p5.4xlarge"
    ML_P6E_GB200_36XLARGE = "ml.p6e-gb200.36xlarge"
    ML_TRN1_32XLARGE = "ml.trn1.32xlarge"
    ML_TRN1N_32XLARGE = "ml.trn1n.32xlarge"
    ML_G5_XLARGE = "ml.g5.xlarge"
    ML_G5_2XLARGE = "ml.g5.2xlarge"
    ML_G5_4XLARGE = "ml.g5.4xlarge"
    ML_G5_8XLARGE = "ml.g5.8xlarge"
    ML_G5_12XLARGE = "ml.g5.12xlarge"
    ML_G5_16XLARGE = "ml.g5.16xlarge"
    ML_G5_24XLARGE = "ml.g5.24xlarge"
    ML_G5_48XLARGE = "ml.g5.48xlarge"
    ML_C5_LARGE = "ml.c5.large"
    ML_C5_XLARGE = "ml.c5.xlarge"
    ML_C5_2XLARGE = "ml.c5.2xlarge"
    ML_C5_4XLARGE = "ml.c5.4xlarge"
    ML_C5_9XLARGE = "ml.c5.9xlarge"
    ML_C5_12XLARGE = "ml.c5.12xlarge"
    ML_C5_18XLARGE = "ml.c5.18xlarge"
    ML_C5_24XLARGE = "ml.c5.24xlarge"
    ML_C5N_LARGE = "ml.c5n.large"
    ML_C5N_2XLARGE = "ml.c5n.2xlarge"
    ML_C5N_4XLARGE = "ml.c5n.4xlarge"
    ML_C5N_9XLARGE = "ml.c5n.9xlarge"
    ML_C5N_18XLARGE = "ml.c5n.18xlarge"
    ML_M5_LARGE = "ml.m5.large"
    ML_M5_XLARGE = "ml.m5.xlarge"
    ML_M5_2XLARGE = "ml.m5.2xlarge"
    ML_M5_4XLARGE = "ml.m5.4xlarge"
    ML_M5_8XLARGE = "ml.m5.8xlarge"
    ML_M5_12XLARGE = "ml.m5.12xlarge"
    ML_M5_16XLARGE = "ml.m5.16xlarge"
    ML_M5_24XLARGE = "ml.m5.24xlarge"
    ML_T3_MEDIUM = "ml.t3.medium"
    ML_T3_LARGE = "ml.t3.large"
    ML_T3_XLARGE = "ml.t3.xlarge"
    ML_T3_2XLARGE = "ml.t3.2xlarge"
    ML_G6_XLARGE = "ml.g6.xlarge"
    ML_G6_2XLARGE = "ml.g6.2xlarge"
    ML_G6_4XLARGE = "ml.g6.4xlarge"
    ML_G6_8XLARGE = "ml.g6.8xlarge"
    ML_G6_16XLARGE = "ml.g6.16xlarge"
    ML_G6_12XLARGE = "ml.g6.12xlarge"
    ML_G6_24XLARGE = "ml.g6.24xlarge"
    ML_G6_48XLARGE = "ml.g6.48xlarge"
    ML_GR6_4XLARGE = "ml.gr6.4xlarge"
    ML_GR6_8XLARGE = "ml.gr6.8xlarge"
    ML_G6E_XLARGE = "ml.g6e.xlarge"
    ML_G6E_2XLARGE = "ml.g6e.2xlarge"
    ML_G6E_4XLARGE = "ml.g6e.4xlarge"
    ML_G6E_8XLARGE = "ml.g6e.8xlarge"
    ML_G6E_16XLARGE = "ml.g6e.16xlarge"
    ML_G6E_12XLARGE = "ml.g6e.12xlarge"
    ML_G6E_24XLARGE = "ml.g6e.24xlarge"
    ML_G6E_48XLARGE = "ml.g6e.48xlarge"
    ML_P5E_48XLARGE = "ml.p5e.48xlarge"
    ML_P5EN_48XLARGE = "ml.p5en.48xlarge"
    ML_P6_B200_48XLARGE = "ml.p6-b200.48xlarge"
    ML_TRN2_3XLARGE = "ml.trn2.3xlarge"
    ML_TRN2_48XLARGE = "ml.trn2.48xlarge"
    ML_C6I_LARGE = "ml.c6i.large"
    ML_C6I_XLARGE = "ml.c6i.xlarge"
    ML_C6I_2XLARGE = "ml.c6i.2xlarge"
    ML_C6I_4XLARGE = "ml.c6i.4xlarge"
    ML_C6I_8XLARGE = "ml.c6i.8xlarge"
    ML_C6I_12XLARGE = "ml.c6i.12xlarge"
    ML_C6I_16XLARGE = "ml.c6i.16xlarge"
    ML_C6I_24XLARGE = "ml.c6i.24xlarge"
    ML_C6I_32XLARGE = "ml.c6i.32xlarge"
    ML_M6I_LARGE = "ml.m6i.large"
    ML_M6I_XLARGE = "ml.m6i.xlarge"
    ML_M6I_2XLARGE = "ml.m6i.2xlarge"
    ML_M6I_4XLARGE = "ml.m6i.4xlarge"
    ML_M6I_8XLARGE = "ml.m6i.8xlarge"
    ML_M6I_12XLARGE = "ml.m6i.12xlarge"
    ML_M6I_16XLARGE = "ml.m6i.16xlarge"
    ML_M6I_24XLARGE = "ml.m6i.24xlarge"
    ML_M6I_32XLARGE = "ml.m6i.32xlarge"
    ML_R6I_LARGE = "ml.r6i.large"
    ML_R6I_XLARGE = "ml.r6i.xlarge"
    ML_R6I_2XLARGE = "ml.r6i.2xlarge"
    ML_R6I_4XLARGE = "ml.r6i.4xlarge"
    ML_R6I_8XLARGE = "ml.r6i.8xlarge"
    ML_R6I_12XLARGE = "ml.r6i.12xlarge"
    ML_R6I_16XLARGE = "ml.r6i.16xlarge"
    ML_R6I_24XLARGE = "ml.r6i.24xlarge"
    ML_R6I_32XLARGE = "ml.r6i.32xlarge"
    ML_I3EN_LARGE = "ml.i3en.large"
    ML_I3EN_XLARGE = "ml.i3en.xlarge"
    ML_I3EN_2XLARGE = "ml.i3en.2xlarge"
    ML_I3EN_3XLARGE = "ml.i3en.3xlarge"
    ML_I3EN_6XLARGE = "ml.i3en.6xlarge"
    ML_I3EN_12XLARGE = "ml.i3en.12xlarge"
    ML_I3EN_24XLARGE = "ml.i3en.24xlarge"
    ML_M7I_LARGE = "ml.m7i.large"
    ML_M7I_XLARGE = "ml.m7i.xlarge"
    ML_M7I_2XLARGE = "ml.m7i.2xlarge"
    ML_M7I_4XLARGE = "ml.m7i.4xlarge"
    ML_M7I_8XLARGE = "ml.m7i.8xlarge"
    ML_M7I_12XLARGE = "ml.m7i.12xlarge"
    ML_M7I_16XLARGE = "ml.m7i.16xlarge"
    ML_M7I_24XLARGE = "ml.m7i.24xlarge"
    ML_M7I_48XLARGE = "ml.m7i.48xlarge"
    ML_R7I_LARGE = "ml.r7i.large"
    ML_R7I_XLARGE = "ml.r7i.xlarge"
    ML_R7I_2XLARGE = "ml.r7i.2xlarge"
    ML_R7I_4XLARGE = "ml.r7i.4xlarge"
    ML_R7I_8XLARGE = "ml.r7i.8xlarge"
    ML_R7I_12XLARGE = "ml.r7i.12xlarge"
    ML_R7I_16XLARGE = "ml.r7i.16xlarge"
    ML_R7I_24XLARGE = "ml.r7i.24xlarge"
    ML_R7I_48XLARGE = "ml.r7i.48xlarge"
    ML_P6_B300_48XLARGE = "ml.p6-b300.48xlarge"


class ClusterKubernetesTaintEffect:
    """ClusterKubernetesTaintEffect enum values."""

    NOSCHEDULE = "NoSchedule"
    PREFERNOSCHEDULE = "PreferNoSchedule"
    NOEXECUTE = "NoExecute"


class ClusterNodeProvisioningMode:
    """ClusterNodeProvisioningMode enum values."""

    CONTINUOUS = "Continuous"


class ClusterNodeRecovery:
    """ClusterNodeRecovery enum values."""

    AUTOMATIC = "Automatic"
    NONE = "None"


class ClusterSortBy:
    """ClusterSortBy enum values."""

    CREATION_TIME = "CREATION_TIME"
    NAME = "NAME"


class ClusterStatus:
    """ClusterStatus enum values."""

    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"
    INSERVICE = "InService"
    ROLLINGBACK = "RollingBack"
    SYSTEMUPDATING = "SystemUpdating"
    UPDATING = "Updating"


class CodeRepositorySortBy:
    """CodeRepositorySortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    LASTMODIFIEDTIME = "LastModifiedTime"


class CodeRepositorySortOrder:
    """CodeRepositorySortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class CollectionType:
    """CollectionType enum values."""

    LIST = "List"
    SET = "Set"
    VECTOR = "Vector"


class CompilationJobStatus:
    """CompilationJobStatus enum values."""

    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class CompleteOnConvergence:
    """CompleteOnConvergence enum values."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class CompressionType:
    """CompressionType enum values."""

    NONE = "None"
    GZIP = "Gzip"


class ConditionOutcome:
    """ConditionOutcome enum values."""

    TRUE = "True"
    FALSE = "False"


class ContainerMode:
    """ContainerMode enum values."""

    SINGLEMODEL = "SingleModel"
    MULTIMODEL = "MultiModel"


class ContentClassifier:
    """ContentClassifier enum values."""

    FREEOFPERSONALLYIDENTIFIABLEINFORMATION = "FreeOfPersonallyIdentifiableInformation"
    FREEOFADULTCONTENT = "FreeOfAdultContent"


class CrossAccountFilterOption:
    """CrossAccountFilterOption enum values."""

    SAMEACCOUNT = "SameAccount"
    CROSSACCOUNT = "CrossAccount"


class CustomizationTechnique:
    """CustomizationTechnique enum values."""

    SFT = "SFT"
    DPO = "DPO"
    RLVR = "RLVR"
    RLAIF = "RLAIF"


class DataDistributionType:
    """DataDistributionType enum values."""

    FULLYREPLICATED = "FullyReplicated"
    SHARDEDBYS3KEY = "ShardedByS3Key"


class DataSourceName:
    """DataSourceName enum values."""

    SALESFORCEGENIE = "SalesforceGenie"
    SNOWFLAKE = "Snowflake"


class DeepHealthCheckType:
    """DeepHealthCheckType enum values."""

    INSTANCESTRESS = "InstanceStress"
    INSTANCECONNECTIVITY = "InstanceConnectivity"


class DetailedAlgorithmStatus:
    """DetailedAlgorithmStatus enum values."""

    NOTSTARTED = "NotStarted"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class DetailedModelPackageStatus:
    """DetailedModelPackageStatus enum values."""

    NOTSTARTED = "NotStarted"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class DeviceDeploymentStatus:
    """DeviceDeploymentStatus enum values."""

    READYTODEPLOY = "READYTODEPLOY"
    INPROGRESS = "INPROGRESS"
    DEPLOYED = "DEPLOYED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class DeviceSubsetType:
    """DeviceSubsetType enum values."""

    PERCENTAGE = "PERCENTAGE"
    SELECTION = "SELECTION"
    NAMECONTAINS = "NAMECONTAINS"


class DirectInternetAccess:
    """DirectInternetAccess enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class Direction:
    """Direction enum values."""

    BOTH = "Both"
    ASCENDANTS = "Ascendants"
    DESCENDANTS = "Descendants"


class DomainStatus:
    """DomainStatus enum values."""

    DELETING = "Deleting"
    FAILED = "Failed"
    INSERVICE = "InService"
    PENDING = "Pending"
    UPDATING = "Updating"
    UPDATE_FAILED = "Update_Failed"
    DELETE_FAILED = "Delete_Failed"


class EdgePackagingJobStatus:
    """EdgePackagingJobStatus enum values."""

    STARTING = "STARTING"
    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class EdgePresetDeploymentStatus:
    """EdgePresetDeploymentStatus enum values."""

    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class EdgePresetDeploymentType:
    """EdgePresetDeploymentType enum values."""

    GREENGRASSV2COMPONENT = "GreengrassV2Component"


class EnabledOrDisabled:
    """EnabledOrDisabled enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class EndpointConfigSortKey:
    """EndpointConfigSortKey enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class EndpointSortKey:
    """EndpointSortKey enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class EndpointStatus:
    """EndpointStatus enum values."""

    OUTOFSERVICE = "OutOfService"
    CREATING = "Creating"
    UPDATING = "Updating"
    SYSTEMUPDATING = "SystemUpdating"
    ROLLINGBACK = "RollingBack"
    INSERVICE = "InService"
    DELETING = "Deleting"
    FAILED = "Failed"
    UPDATEROLLBACKFAILED = "UpdateRollbackFailed"


class EvaluationType:
    """EvaluationType enum values."""

    LLMAJEVALUATION = "LLMAJEvaluation"
    CUSTOMSCOREREVALUATION = "CustomScorerEvaluation"
    BENCHMARKEVALUATION = "BenchmarkEvaluation"


class EventSortBy:
    """EventSortBy enum values."""

    EVENTTIME = "EventTime"


class ExecutionRoleIdentityConfig:
    """ExecutionRoleIdentityConfig enum values."""

    USER_PROFILE_NAME = "USER_PROFILE_NAME"
    DISABLED = "DISABLED"


class ExecutionStatus:
    """ExecutionStatus enum values."""

    PENDING = "Pending"
    COMPLETED = "Completed"
    COMPLETEDWITHVIOLATIONS = "CompletedWithViolations"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"


class FailureHandlingPolicy:
    """FailureHandlingPolicy enum values."""

    ROLLBACK_ON_FAILURE = "ROLLBACK_ON_FAILURE"
    DO_NOTHING = "DO_NOTHING"


class FairShare:
    """FairShare enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class FeatureGroupSortBy:
    """FeatureGroupSortBy enum values."""

    NAME = "Name"
    FEATUREGROUPSTATUS = "FeatureGroupStatus"
    OFFLINESTORESTATUS = "OfflineStoreStatus"
    CREATIONTIME = "CreationTime"


class FeatureGroupSortOrder:
    """FeatureGroupSortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class FeatureGroupStatus:
    """FeatureGroupStatus enum values."""

    CREATING = "Creating"
    CREATED = "Created"
    CREATEFAILED = "CreateFailed"
    DELETING = "Deleting"
    DELETEFAILED = "DeleteFailed"


class FeatureStatus:
    """FeatureStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FeatureType:
    """FeatureType enum values."""

    INTEGRAL = "Integral"
    FRACTIONAL = "Fractional"
    STRING = "String"


class FileSystemAccessMode:
    """FileSystemAccessMode enum values."""

    RW = "rw"
    RO = "ro"


class FileSystemType:
    """FileSystemType enum values."""

    EFS = "EFS"
    FSXLUSTRE = "FSxLustre"


class FillingType:
    """FillingType enum values."""

    FRONTFILL = "frontfill"
    MIDDLEFILL = "middlefill"
    BACKFILL = "backfill"
    FUTUREFILL = "futurefill"
    FRONTFILL_VALUE = "frontfill_value"
    MIDDLEFILL_VALUE = "middlefill_value"
    BACKFILL_VALUE = "backfill_value"
    FUTUREFILL_VALUE = "futurefill_value"


class FlatInvocations:
    """FlatInvocations enum values."""

    CONTINUE = "Continue"
    STOP = "Stop"


class FlowDefinitionStatus:
    """FlowDefinitionStatus enum values."""

    INITIALIZING = "Initializing"
    ACTIVE = "Active"
    FAILED = "Failed"
    DELETING = "Deleting"


class Framework:
    """Framework enum values."""

    TENSORFLOW = "TENSORFLOW"
    KERAS = "KERAS"
    MXNET = "MXNET"
    ONNX = "ONNX"
    PYTORCH = "PYTORCH"
    XGBOOST = "XGBOOST"
    TFLITE = "TFLITE"
    DARKNET = "DARKNET"
    SKLEARN = "SKLEARN"


class HubContentSortBy:
    """HubContentSortBy enum values."""

    HUBCONTENTNAME = "HubContentName"
    CREATIONTIME = "CreationTime"
    HUBCONTENTSTATUS = "HubContentStatus"


class HubContentStatus:
    """HubContentStatus enum values."""

    AVAILABLE = "Available"
    IMPORTING = "Importing"
    DELETING = "Deleting"
    IMPORTFAILED = "ImportFailed"
    DELETEFAILED = "DeleteFailed"
    PENDINGIMPORT = "PendingImport"
    PENDINGDELETE = "PendingDelete"


class HubContentSupportStatus:
    """HubContentSupportStatus enum values."""

    SUPPORTED = "Supported"
    DEPRECATED = "Deprecated"
    RESTRICTED = "Restricted"


class HubContentType:
    """HubContentType enum values."""

    MODEL = "Model"
    NOTEBOOK = "Notebook"
    MODELREFERENCE = "ModelReference"
    DATASET = "DataSet"
    JSONDOC = "JsonDoc"


class HubSortBy:
    """HubSortBy enum values."""

    HUBNAME = "HubName"
    CREATIONTIME = "CreationTime"
    HUBSTATUS = "HubStatus"
    ACCOUNTIDOWNER = "AccountIdOwner"


class HubStatus:
    """HubStatus enum values."""

    INSERVICE = "InService"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    CREATEFAILED = "CreateFailed"
    UPDATEFAILED = "UpdateFailed"
    DELETEFAILED = "DeleteFailed"


class HumanTaskUiStatus:
    """HumanTaskUiStatus enum values."""

    ACTIVE = "Active"
    DELETING = "Deleting"


class HyperParameterScalingType:
    """HyperParameterScalingType enum values."""

    AUTO = "Auto"
    LINEAR = "Linear"
    LOGARITHMIC = "Logarithmic"
    REVERSELOGARITHMIC = "ReverseLogarithmic"


class HyperParameterTuningAllocationStrategy:
    """HyperParameterTuningAllocationStrategy enum values."""

    PRIORITIZED = "Prioritized"


class HyperParameterTuningJobObjectiveType:
    """HyperParameterTuningJobObjectiveType enum values."""

    MAXIMIZE = "Maximize"
    MINIMIZE = "Minimize"


class HyperParameterTuningJobSortByOptions:
    """HyperParameterTuningJobSortByOptions enum values."""

    NAME = "Name"
    STATUS = "Status"
    CREATIONTIME = "CreationTime"


class HyperParameterTuningJobStatus:
    """HyperParameterTuningJobStatus enum values."""

    COMPLETED = "Completed"
    INPROGRESS = "InProgress"
    FAILED = "Failed"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    DELETING = "Deleting"
    DELETEFAILED = "DeleteFailed"


class HyperParameterTuningJobStrategyType:
    """HyperParameterTuningJobStrategyType enum values."""

    BAYESIAN = "Bayesian"
    RANDOM = "Random"
    HYPERBAND = "Hyperband"
    GRID = "Grid"


class HyperParameterTuningJobWarmStartType:
    """HyperParameterTuningJobWarmStartType enum values."""

    IDENTICALDATAANDALGORITHM = "IdenticalDataAndAlgorithm"
    TRANSFERLEARNING = "TransferLearning"


class IPAddressType:
    """IPAddressType enum values."""

    IPV4 = "ipv4"
    DUALSTACK = "dualstack"


class ImageSortBy:
    """ImageSortBy enum values."""

    CREATION_TIME = "CREATION_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"
    IMAGE_NAME = "IMAGE_NAME"


class ImageSortOrder:
    """ImageSortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class ImageStatus:
    """ImageStatus enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATING = "UPDATING"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"


class ImageVersionSortBy:
    """ImageVersionSortBy enum values."""

    CREATION_TIME = "CREATION_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"
    VERSION = "VERSION"


class ImageVersionSortOrder:
    """ImageVersionSortOrder enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class ImageVersionStatus:
    """ImageVersionStatus enum values."""

    CREATING = "CREATING"
    CREATED = "CREATED"
    CREATE_FAILED = "CREATE_FAILED"
    DELETING = "DELETING"
    DELETE_FAILED = "DELETE_FAILED"


class InferenceComponentCapacitySizeType:
    """InferenceComponentCapacitySizeType enum values."""

    COPY_COUNT = "COPY_COUNT"
    CAPACITY_PERCENT = "CAPACITY_PERCENT"


class InferenceComponentSortKey:
    """InferenceComponentSortKey enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class InferenceComponentStatus:
    """InferenceComponentStatus enum values."""

    INSERVICE = "InService"
    CREATING = "Creating"
    UPDATING = "Updating"
    FAILED = "Failed"
    DELETING = "Deleting"


class InferenceExecutionMode:
    """InferenceExecutionMode enum values."""

    SERIAL = "Serial"
    DIRECT = "Direct"


class InferenceExperimentStatus:
    """InferenceExperimentStatus enum values."""

    CREATING = "Creating"
    CREATED = "Created"
    UPDATING = "Updating"
    RUNNING = "Running"
    STARTING = "Starting"
    STOPPING = "Stopping"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class InferenceExperimentStopDesiredState:
    """InferenceExperimentStopDesiredState enum values."""

    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class InferenceExperimentType:
    """InferenceExperimentType enum values."""

    SHADOWMODE = "ShadowMode"


class InputMode:
    """InputMode enum values."""

    PIPE = "Pipe"
    FILE = "File"


class InstanceGroupStatus:
    """InstanceGroupStatus enum values."""

    INSERVICE = "InService"
    CREATING = "Creating"
    UPDATING = "Updating"
    FAILED = "Failed"
    DEGRADED = "Degraded"
    SYSTEMUPDATING = "SystemUpdating"
    DELETING = "Deleting"


class InstanceType:
    """InstanceType enum values."""

    ML_T2_MEDIUM = "ml.t2.medium"
    ML_T2_LARGE = "ml.t2.large"
    ML_T2_XLARGE = "ml.t2.xlarge"
    ML_T2_2XLARGE = "ml.t2.2xlarge"
    ML_T3_MEDIUM = "ml.t3.medium"
    ML_T3_LARGE = "ml.t3.large"
    ML_T3_XLARGE = "ml.t3.xlarge"
    ML_T3_2XLARGE = "ml.t3.2xlarge"
    ML_M4_XLARGE = "ml.m4.xlarge"
    ML_M4_2XLARGE = "ml.m4.2xlarge"
    ML_M4_4XLARGE = "ml.m4.4xlarge"
    ML_M4_10XLARGE = "ml.m4.10xlarge"
    ML_M4_16XLARGE = "ml.m4.16xlarge"
    ML_M5_XLARGE = "ml.m5.xlarge"
    ML_M5_2XLARGE = "ml.m5.2xlarge"
    ML_M5_4XLARGE = "ml.m5.4xlarge"
    ML_M5_12XLARGE = "ml.m5.12xlarge"
    ML_M5_24XLARGE = "ml.m5.24xlarge"
    ML_M5D_LARGE = "ml.m5d.large"
    ML_M5D_XLARGE = "ml.m5d.xlarge"
    ML_M5D_2XLARGE = "ml.m5d.2xlarge"
    ML_M5D_4XLARGE = "ml.m5d.4xlarge"
    ML_M5D_8XLARGE = "ml.m5d.8xlarge"
    ML_M5D_12XLARGE = "ml.m5d.12xlarge"
    ML_M5D_16XLARGE = "ml.m5d.16xlarge"
    ML_M5D_24XLARGE = "ml.m5d.24xlarge"
    ML_C4_XLARGE = "ml.c4.xlarge"
    ML_C4_2XLARGE = "ml.c4.2xlarge"
    ML_C4_4XLARGE = "ml.c4.4xlarge"
    ML_C4_8XLARGE = "ml.c4.8xlarge"
    ML_C5_XLARGE = "ml.c5.xlarge"
    ML_C5_2XLARGE = "ml.c5.2xlarge"
    ML_C5_4XLARGE = "ml.c5.4xlarge"
    ML_C5_9XLARGE = "ml.c5.9xlarge"
    ML_C5_18XLARGE = "ml.c5.18xlarge"
    ML_C5D_XLARGE = "ml.c5d.xlarge"
    ML_C5D_2XLARGE = "ml.c5d.2xlarge"
    ML_C5D_4XLARGE = "ml.c5d.4xlarge"
    ML_C5D_9XLARGE = "ml.c5d.9xlarge"
    ML_C5D_18XLARGE = "ml.c5d.18xlarge"
    ML_P2_XLARGE = "ml.p2.xlarge"
    ML_P2_8XLARGE = "ml.p2.8xlarge"
    ML_P2_16XLARGE = "ml.p2.16xlarge"
    ML_P3_2XLARGE = "ml.p3.2xlarge"
    ML_P3_8XLARGE = "ml.p3.8xlarge"
    ML_P3_16XLARGE = "ml.p3.16xlarge"
    ML_P3DN_24XLARGE = "ml.p3dn.24xlarge"
    ML_G4DN_XLARGE = "ml.g4dn.xlarge"
    ML_G4DN_2XLARGE = "ml.g4dn.2xlarge"
    ML_G4DN_4XLARGE = "ml.g4dn.4xlarge"
    ML_G4DN_8XLARGE = "ml.g4dn.8xlarge"
    ML_G4DN_12XLARGE = "ml.g4dn.12xlarge"
    ML_G4DN_16XLARGE = "ml.g4dn.16xlarge"
    ML_R5_LARGE = "ml.r5.large"
    ML_R5_XLARGE = "ml.r5.xlarge"
    ML_R5_2XLARGE = "ml.r5.2xlarge"
    ML_R5_4XLARGE = "ml.r5.4xlarge"
    ML_R5_8XLARGE = "ml.r5.8xlarge"
    ML_R5_12XLARGE = "ml.r5.12xlarge"
    ML_R5_16XLARGE = "ml.r5.16xlarge"
    ML_R5_24XLARGE = "ml.r5.24xlarge"
    ML_G5_XLARGE = "ml.g5.xlarge"
    ML_G5_2XLARGE = "ml.g5.2xlarge"
    ML_G5_4XLARGE = "ml.g5.4xlarge"
    ML_G5_8XLARGE = "ml.g5.8xlarge"
    ML_G5_16XLARGE = "ml.g5.16xlarge"
    ML_G5_12XLARGE = "ml.g5.12xlarge"
    ML_G5_24XLARGE = "ml.g5.24xlarge"
    ML_G5_48XLARGE = "ml.g5.48xlarge"
    ML_INF1_XLARGE = "ml.inf1.xlarge"
    ML_INF1_2XLARGE = "ml.inf1.2xlarge"
    ML_INF1_6XLARGE = "ml.inf1.6xlarge"
    ML_INF1_24XLARGE = "ml.inf1.24xlarge"
    ML_TRN1_2XLARGE = "ml.trn1.2xlarge"
    ML_TRN1_32XLARGE = "ml.trn1.32xlarge"
    ML_TRN1N_32XLARGE = "ml.trn1n.32xlarge"
    ML_INF2_XLARGE = "ml.inf2.xlarge"
    ML_INF2_8XLARGE = "ml.inf2.8xlarge"
    ML_INF2_24XLARGE = "ml.inf2.24xlarge"
    ML_INF2_48XLARGE = "ml.inf2.48xlarge"
    ML_P4D_24XLARGE = "ml.p4d.24xlarge"
    ML_P4DE_24XLARGE = "ml.p4de.24xlarge"
    ML_P5_48XLARGE = "ml.p5.48xlarge"
    ML_P6_B200_48XLARGE = "ml.p6-b200.48xlarge"
    ML_M6I_LARGE = "ml.m6i.large"
    ML_M6I_XLARGE = "ml.m6i.xlarge"
    ML_M6I_2XLARGE = "ml.m6i.2xlarge"
    ML_M6I_4XLARGE = "ml.m6i.4xlarge"
    ML_M6I_8XLARGE = "ml.m6i.8xlarge"
    ML_M6I_12XLARGE = "ml.m6i.12xlarge"
    ML_M6I_16XLARGE = "ml.m6i.16xlarge"
    ML_M6I_24XLARGE = "ml.m6i.24xlarge"
    ML_M6I_32XLARGE = "ml.m6i.32xlarge"
    ML_M7I_LARGE = "ml.m7i.large"
    ML_M7I_XLARGE = "ml.m7i.xlarge"
    ML_M7I_2XLARGE = "ml.m7i.2xlarge"
    ML_M7I_4XLARGE = "ml.m7i.4xlarge"
    ML_M7I_8XLARGE = "ml.m7i.8xlarge"
    ML_M7I_12XLARGE = "ml.m7i.12xlarge"
    ML_M7I_16XLARGE = "ml.m7i.16xlarge"
    ML_M7I_24XLARGE = "ml.m7i.24xlarge"
    ML_M7I_48XLARGE = "ml.m7i.48xlarge"
    ML_C6I_LARGE = "ml.c6i.large"
    ML_C6I_XLARGE = "ml.c6i.xlarge"
    ML_C6I_2XLARGE = "ml.c6i.2xlarge"
    ML_C6I_4XLARGE = "ml.c6i.4xlarge"
    ML_C6I_8XLARGE = "ml.c6i.8xlarge"
    ML_C6I_12XLARGE = "ml.c6i.12xlarge"
    ML_C6I_16XLARGE = "ml.c6i.16xlarge"
    ML_C6I_24XLARGE = "ml.c6i.24xlarge"
    ML_C6I_32XLARGE = "ml.c6i.32xlarge"
    ML_C7I_LARGE = "ml.c7i.large"
    ML_C7I_XLARGE = "ml.c7i.xlarge"
    ML_C7I_2XLARGE = "ml.c7i.2xlarge"
    ML_C7I_4XLARGE = "ml.c7i.4xlarge"
    ML_C7I_8XLARGE = "ml.c7i.8xlarge"
    ML_C7I_12XLARGE = "ml.c7i.12xlarge"
    ML_C7I_16XLARGE = "ml.c7i.16xlarge"
    ML_C7I_24XLARGE = "ml.c7i.24xlarge"
    ML_C7I_48XLARGE = "ml.c7i.48xlarge"
    ML_R6I_LARGE = "ml.r6i.large"
    ML_R6I_XLARGE = "ml.r6i.xlarge"
    ML_R6I_2XLARGE = "ml.r6i.2xlarge"
    ML_R6I_4XLARGE = "ml.r6i.4xlarge"
    ML_R6I_8XLARGE = "ml.r6i.8xlarge"
    ML_R6I_12XLARGE = "ml.r6i.12xlarge"
    ML_R6I_16XLARGE = "ml.r6i.16xlarge"
    ML_R6I_24XLARGE = "ml.r6i.24xlarge"
    ML_R6I_32XLARGE = "ml.r6i.32xlarge"
    ML_R7I_LARGE = "ml.r7i.large"
    ML_R7I_XLARGE = "ml.r7i.xlarge"
    ML_R7I_2XLARGE = "ml.r7i.2xlarge"
    ML_R7I_4XLARGE = "ml.r7i.4xlarge"
    ML_R7I_8XLARGE = "ml.r7i.8xlarge"
    ML_R7I_12XLARGE = "ml.r7i.12xlarge"
    ML_R7I_16XLARGE = "ml.r7i.16xlarge"
    ML_R7I_24XLARGE = "ml.r7i.24xlarge"
    ML_R7I_48XLARGE = "ml.r7i.48xlarge"
    ML_M6ID_LARGE = "ml.m6id.large"
    ML_M6ID_XLARGE = "ml.m6id.xlarge"
    ML_M6ID_2XLARGE = "ml.m6id.2xlarge"
    ML_M6ID_4XLARGE = "ml.m6id.4xlarge"
    ML_M6ID_8XLARGE = "ml.m6id.8xlarge"
    ML_M6ID_12XLARGE = "ml.m6id.12xlarge"
    ML_M6ID_16XLARGE = "ml.m6id.16xlarge"
    ML_M6ID_24XLARGE = "ml.m6id.24xlarge"
    ML_M6ID_32XLARGE = "ml.m6id.32xlarge"
    ML_C6ID_LARGE = "ml.c6id.large"
    ML_C6ID_XLARGE = "ml.c6id.xlarge"
    ML_C6ID_2XLARGE = "ml.c6id.2xlarge"
    ML_C6ID_4XLARGE = "ml.c6id.4xlarge"
    ML_C6ID_8XLARGE = "ml.c6id.8xlarge"
    ML_C6ID_12XLARGE = "ml.c6id.12xlarge"
    ML_C6ID_16XLARGE = "ml.c6id.16xlarge"
    ML_C6ID_24XLARGE = "ml.c6id.24xlarge"
    ML_C6ID_32XLARGE = "ml.c6id.32xlarge"
    ML_R6ID_LARGE = "ml.r6id.large"
    ML_R6ID_XLARGE = "ml.r6id.xlarge"
    ML_R6ID_2XLARGE = "ml.r6id.2xlarge"
    ML_R6ID_4XLARGE = "ml.r6id.4xlarge"
    ML_R6ID_8XLARGE = "ml.r6id.8xlarge"
    ML_R6ID_12XLARGE = "ml.r6id.12xlarge"
    ML_R6ID_16XLARGE = "ml.r6id.16xlarge"
    ML_R6ID_24XLARGE = "ml.r6id.24xlarge"
    ML_R6ID_32XLARGE = "ml.r6id.32xlarge"
    ML_G6_XLARGE = "ml.g6.xlarge"
    ML_G6_2XLARGE = "ml.g6.2xlarge"
    ML_G6_4XLARGE = "ml.g6.4xlarge"
    ML_G6_8XLARGE = "ml.g6.8xlarge"
    ML_G6_12XLARGE = "ml.g6.12xlarge"
    ML_G6_16XLARGE = "ml.g6.16xlarge"
    ML_G6_24XLARGE = "ml.g6.24xlarge"
    ML_G6_48XLARGE = "ml.g6.48xlarge"


class IsTrackingServerActive:
    """IsTrackingServerActive enum values."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"


class JobType:
    """JobType enum values."""

    TRAINING = "TRAINING"
    INFERENCE = "INFERENCE"
    NOTEBOOK_KERNEL = "NOTEBOOK_KERNEL"


class JoinSource:
    """JoinSource enum values."""

    INPUT = "Input"
    NONE = "None"


class LabelingJobStatus:
    """LabelingJobStatus enum values."""

    INITIALIZING = "Initializing"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"


class LastUpdateStatusValue:
    """LastUpdateStatusValue enum values."""

    SUCCESSFUL = "Successful"
    FAILED = "Failed"
    INPROGRESS = "InProgress"


class LifecycleManagement:
    """LifecycleManagement enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class LineageType:
    """LineageType enum values."""

    TRIALCOMPONENT = "TrialComponent"
    ARTIFACT = "Artifact"
    CONTEXT = "Context"
    ACTION = "Action"


class ListCompilationJobsSortBy:
    """ListCompilationJobsSortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class ListDeviceFleetsSortBy:
    """ListDeviceFleetsSortBy enum values."""

    NAME = "NAME"
    CREATION_TIME = "CREATION_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class ListEdgeDeploymentPlansSortBy:
    """ListEdgeDeploymentPlansSortBy enum values."""

    NAME = "NAME"
    DEVICE_FLEET_NAME = "DEVICE_FLEET_NAME"
    CREATION_TIME = "CREATION_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"


class ListEdgePackagingJobsSortBy:
    """ListEdgePackagingJobsSortBy enum values."""

    NAME = "NAME"
    MODEL_NAME = "MODEL_NAME"
    CREATION_TIME = "CREATION_TIME"
    LAST_MODIFIED_TIME = "LAST_MODIFIED_TIME"
    STATUS = "STATUS"


class ListInferenceRecommendationsJobsSortBy:
    """ListInferenceRecommendationsJobsSortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class ListLabelingJobsForWorkteamSortByOptions:
    """ListLabelingJobsForWorkteamSortByOptions enum values."""

    CREATIONTIME = "CreationTime"


class ListOptimizationJobsSortBy:
    """ListOptimizationJobsSortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class ListWorkforcesSortByOptions:
    """ListWorkforcesSortByOptions enum values."""

    NAME = "Name"
    CREATEDATE = "CreateDate"


class ListWorkteamsSortByOptions:
    """ListWorkteamsSortByOptions enum values."""

    NAME = "Name"
    CREATEDATE = "CreateDate"


class MIGProfileType:
    """MIGProfileType enum values."""

    MIG_1G_5GB = "mig-1g.5gb"
    MIG_1G_10GB = "mig-1g.10gb"
    MIG_1G_18GB = "mig-1g.18gb"
    MIG_1G_20GB = "mig-1g.20gb"
    MIG_1G_23GB = "mig-1g.23gb"
    MIG_1G_35GB = "mig-1g.35gb"
    MIG_1G_45GB = "mig-1g.45gb"
    MIG_1G_47GB = "mig-1g.47gb"
    MIG_2G_10GB = "mig-2g.10gb"
    MIG_2G_20GB = "mig-2g.20gb"
    MIG_2G_35GB = "mig-2g.35gb"
    MIG_2G_45GB = "mig-2g.45gb"
    MIG_2G_47GB = "mig-2g.47gb"
    MIG_3G_20GB = "mig-3g.20gb"
    MIG_3G_40GB = "mig-3g.40gb"
    MIG_3G_71GB = "mig-3g.71gb"
    MIG_3G_90GB = "mig-3g.90gb"
    MIG_3G_93GB = "mig-3g.93gb"
    MIG_4G_20GB = "mig-4g.20gb"
    MIG_4G_40GB = "mig-4g.40gb"
    MIG_4G_71GB = "mig-4g.71gb"
    MIG_4G_90GB = "mig-4g.90gb"
    MIG_4G_93GB = "mig-4g.93gb"
    MIG_7G_40GB = "mig-7g.40gb"
    MIG_7G_80GB = "mig-7g.80gb"
    MIG_7G_141GB = "mig-7g.141gb"
    MIG_7G_180GB = "mig-7g.180gb"
    MIG_7G_186GB = "mig-7g.186gb"


class MaintenanceStatus:
    """MaintenanceStatus enum values."""

    MAINTENANCEINPROGRESS = "MaintenanceInProgress"
    MAINTENANCECOMPLETE = "MaintenanceComplete"
    MAINTENANCEFAILED = "MaintenanceFailed"


class ManagedInstanceScalingStatus:
    """ManagedInstanceScalingStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MetricSetSource:
    """MetricSetSource enum values."""

    TRAIN = "Train"
    VALIDATION = "Validation"
    TEST = "Test"


class MlTools:
    """MlTools enum values."""

    DATAWRANGLER = "DataWrangler"
    FEATURESTORE = "FeatureStore"
    EMRCLUSTERS = "EmrClusters"
    AUTOML = "AutoMl"
    EXPERIMENTS = "Experiments"
    TRAINING = "Training"
    MODELEVALUATION = "ModelEvaluation"
    PIPELINES = "Pipelines"
    MODELS = "Models"
    JUMPSTART = "JumpStart"
    INFERENCERECOMMENDER = "InferenceRecommender"
    ENDPOINTS = "Endpoints"
    PROJECTS = "Projects"
    INFERENCEOPTIMIZATION = "InferenceOptimization"
    PERFORMANCEEVALUATION = "PerformanceEvaluation"
    LAKERAGUARD = "LakeraGuard"
    COMET = "Comet"
    DEEPCHECKSLLMEVALUATION = "DeepchecksLLMEvaluation"
    FIDDLER = "Fiddler"
    HYPERPODCLUSTERS = "HyperPodClusters"
    RUNNINGINSTANCES = "RunningInstances"
    DATASETS = "Datasets"
    EVALUATORS = "Evaluators"


class MlflowAppStatus:
    """MlflowAppStatus enum values."""

    CREATING = "Creating"
    CREATED = "Created"
    CREATEFAILED = "CreateFailed"
    UPDATING = "Updating"
    UPDATED = "Updated"
    UPDATEFAILED = "UpdateFailed"
    DELETING = "Deleting"
    DELETEFAILED = "DeleteFailed"
    DELETED = "Deleted"


class ModelApprovalStatus:
    """ModelApprovalStatus enum values."""

    APPROVED = "Approved"
    REJECTED = "Rejected"
    PENDINGMANUALAPPROVAL = "PendingManualApproval"


class ModelCacheSetting:
    """ModelCacheSetting enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ModelCardExportJobSortBy:
    """ModelCardExportJobSortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class ModelCardExportJobSortOrder:
    """ModelCardExportJobSortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class ModelCardExportJobStatus:
    """ModelCardExportJobStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class ModelCardProcessingStatus:
    """ModelCardProcessingStatus enum values."""

    DELETEINPROGRESS = "DeleteInProgress"
    DELETEPENDING = "DeletePending"
    CONTENTDELETED = "ContentDeleted"
    EXPORTJOBSDELETED = "ExportJobsDeleted"
    DELETECOMPLETED = "DeleteCompleted"
    DELETEFAILED = "DeleteFailed"


class ModelCardSortBy:
    """ModelCardSortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class ModelCardSortOrder:
    """ModelCardSortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class ModelCardStatus:
    """ModelCardStatus enum values."""

    DRAFT = "Draft"
    PENDINGREVIEW = "PendingReview"
    APPROVED = "Approved"
    ARCHIVED = "Archived"


class ModelCardVersionSortBy:
    """ModelCardVersionSortBy enum values."""

    VERSION = "Version"


class ModelCompressionType:
    """ModelCompressionType enum values."""

    NONE = "None"
    GZIP = "Gzip"


class ModelInfrastructureType:
    """ModelInfrastructureType enum values."""

    REALTIMEINFERENCE = "RealTimeInference"


class ModelMetadataFilterType:
    """ModelMetadataFilterType enum values."""

    DOMAIN = "Domain"
    FRAMEWORK = "Framework"
    TASK = "Task"
    FRAMEWORKVERSION = "FrameworkVersion"


class ModelPackageGroupSortBy:
    """ModelPackageGroupSortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class ModelPackageGroupStatus:
    """ModelPackageGroupStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    DELETING = "Deleting"
    DELETEFAILED = "DeleteFailed"


class ModelPackageRegistrationType:
    """ModelPackageRegistrationType enum values."""

    LOGGED = "Logged"
    REGISTERED = "Registered"


class ModelPackageSortBy:
    """ModelPackageSortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class ModelPackageStatus:
    """ModelPackageStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    DELETING = "Deleting"


class ModelPackageType:
    """ModelPackageType enum values."""

    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"
    BOTH = "Both"


class ModelRegistrationMode:
    """ModelRegistrationMode enum values."""

    AUTOMODELREGISTRATIONENABLED = "AutoModelRegistrationEnabled"
    AUTOMODELREGISTRATIONDISABLED = "AutoModelRegistrationDisabled"


class ModelSortKey:
    """ModelSortKey enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class ModelSpeculativeDecodingS3DataType:
    """ModelSpeculativeDecodingS3DataType enum values."""

    S3PREFIX = "S3Prefix"
    MANIFESTFILE = "ManifestFile"


class ModelSpeculativeDecodingTechnique:
    """ModelSpeculativeDecodingTechnique enum values."""

    EAGLE = "EAGLE"


class ModelVariantAction:
    """ModelVariantAction enum values."""

    RETAIN = "Retain"
    REMOVE = "Remove"
    PROMOTE = "Promote"


class ModelVariantStatus:
    """ModelVariantStatus enum values."""

    CREATING = "Creating"
    UPDATING = "Updating"
    INSERVICE = "InService"
    DELETING = "Deleting"
    DELETED = "Deleted"


class MonitoringAlertHistorySortKey:
    """MonitoringAlertHistorySortKey enum values."""

    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class MonitoringAlertStatus:
    """MonitoringAlertStatus enum values."""

    INALERT = "InAlert"
    OK = "OK"


class MonitoringExecutionSortKey:
    """MonitoringExecutionSortKey enum values."""

    CREATIONTIME = "CreationTime"
    SCHEDULEDTIME = "ScheduledTime"
    STATUS = "Status"


class MonitoringJobDefinitionSortKey:
    """MonitoringJobDefinitionSortKey enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class MonitoringProblemType:
    """MonitoringProblemType enum values."""

    BINARYCLASSIFICATION = "BinaryClassification"
    MULTICLASSCLASSIFICATION = "MulticlassClassification"
    REGRESSION = "Regression"


class MonitoringScheduleSortKey:
    """MonitoringScheduleSortKey enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class MonitoringType:
    """MonitoringType enum values."""

    DATAQUALITY = "DataQuality"
    MODELQUALITY = "ModelQuality"
    MODELBIAS = "ModelBias"
    MODELEXPLAINABILITY = "ModelExplainability"


class NodeUnavailabilityType:
    """NodeUnavailabilityType enum values."""

    INSTANCE_COUNT = "INSTANCE_COUNT"
    CAPACITY_PERCENTAGE = "CAPACITY_PERCENTAGE"


class NotebookInstanceAcceleratorType:
    """NotebookInstanceAcceleratorType enum values."""

    ML_EIA1_MEDIUM = "ml.eia1.medium"
    ML_EIA1_LARGE = "ml.eia1.large"
    ML_EIA1_XLARGE = "ml.eia1.xlarge"
    ML_EIA2_MEDIUM = "ml.eia2.medium"
    ML_EIA2_LARGE = "ml.eia2.large"
    ML_EIA2_XLARGE = "ml.eia2.xlarge"


class NotebookInstanceLifecycleConfigSortKey:
    """NotebookInstanceLifecycleConfigSortKey enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    LASTMODIFIEDTIME = "LastModifiedTime"


class NotebookInstanceLifecycleConfigSortOrder:
    """NotebookInstanceLifecycleConfigSortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class NotebookInstanceSortKey:
    """NotebookInstanceSortKey enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class NotebookInstanceSortOrder:
    """NotebookInstanceSortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class NotebookInstanceStatus:
    """NotebookInstanceStatus enum values."""

    PENDING = "Pending"
    INSERVICE = "InService"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    FAILED = "Failed"
    DELETING = "Deleting"
    UPDATING = "Updating"


class NotebookOutputOption:
    """NotebookOutputOption enum values."""

    ALLOWED = "Allowed"
    DISABLED = "Disabled"


class ObjectiveStatus:
    """ObjectiveStatus enum values."""

    SUCCEEDED = "Succeeded"
    PENDING = "Pending"
    FAILED = "Failed"


class OfflineStoreStatusValue:
    """OfflineStoreStatusValue enum values."""

    ACTIVE = "Active"
    BLOCKED = "Blocked"
    DISABLED = "Disabled"


class Operator:
    """Operator enum values."""

    EQUALS = "Equals"
    NOTEQUALS = "NotEquals"
    GREATERTHAN = "GreaterThan"
    GREATERTHANOREQUALTO = "GreaterThanOrEqualTo"
    LESSTHAN = "LessThan"
    LESSTHANOREQUALTO = "LessThanOrEqualTo"
    CONTAINS = "Contains"
    EXISTS = "Exists"
    NOTEXISTS = "NotExists"
    IN = "In"


class OptimizationJobDeploymentInstanceType:
    """OptimizationJobDeploymentInstanceType enum values."""

    ML_P4D_24XLARGE = "ml.p4d.24xlarge"
    ML_P4DE_24XLARGE = "ml.p4de.24xlarge"
    ML_P5_48XLARGE = "ml.p5.48xlarge"
    ML_P5E_48XLARGE = "ml.p5e.48xlarge"
    ML_P5EN_48XLARGE = "ml.p5en.48xlarge"
    ML_G5_XLARGE = "ml.g5.xlarge"
    ML_G5_2XLARGE = "ml.g5.2xlarge"
    ML_G5_4XLARGE = "ml.g5.4xlarge"
    ML_G5_8XLARGE = "ml.g5.8xlarge"
    ML_G5_12XLARGE = "ml.g5.12xlarge"
    ML_G5_16XLARGE = "ml.g5.16xlarge"
    ML_G5_24XLARGE = "ml.g5.24xlarge"
    ML_G5_48XLARGE = "ml.g5.48xlarge"
    ML_G6_XLARGE = "ml.g6.xlarge"
    ML_G6_2XLARGE = "ml.g6.2xlarge"
    ML_G6_4XLARGE = "ml.g6.4xlarge"
    ML_G6_8XLARGE = "ml.g6.8xlarge"
    ML_G6_12XLARGE = "ml.g6.12xlarge"
    ML_G6_16XLARGE = "ml.g6.16xlarge"
    ML_G6_24XLARGE = "ml.g6.24xlarge"
    ML_G6_48XLARGE = "ml.g6.48xlarge"
    ML_G6E_XLARGE = "ml.g6e.xlarge"
    ML_G6E_2XLARGE = "ml.g6e.2xlarge"
    ML_G6E_4XLARGE = "ml.g6e.4xlarge"
    ML_G6E_8XLARGE = "ml.g6e.8xlarge"
    ML_G6E_12XLARGE = "ml.g6e.12xlarge"
    ML_G6E_16XLARGE = "ml.g6e.16xlarge"
    ML_G6E_24XLARGE = "ml.g6e.24xlarge"
    ML_G6E_48XLARGE = "ml.g6e.48xlarge"
    ML_INF2_XLARGE = "ml.inf2.xlarge"
    ML_INF2_8XLARGE = "ml.inf2.8xlarge"
    ML_INF2_24XLARGE = "ml.inf2.24xlarge"
    ML_INF2_48XLARGE = "ml.inf2.48xlarge"
    ML_TRN1_2XLARGE = "ml.trn1.2xlarge"
    ML_TRN1_32XLARGE = "ml.trn1.32xlarge"
    ML_TRN1N_32XLARGE = "ml.trn1n.32xlarge"


class OptimizationJobStatus:
    """OptimizationJobStatus enum values."""

    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class OrderKey:
    """OrderKey enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class OutputCompressionType:
    """OutputCompressionType enum values."""

    GZIP = "GZIP"
    NONE = "NONE"


class ParameterType:
    """ParameterType enum values."""

    INTEGER = "Integer"
    CONTINUOUS = "Continuous"
    CATEGORICAL = "Categorical"
    FREETEXT = "FreeText"


class PartnerAppAuthType:
    """PartnerAppAuthType enum values."""

    IAM = "IAM"


class PartnerAppStatus:
    """PartnerAppStatus enum values."""

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    AVAILABLE = "Available"
    FAILED = "Failed"
    UPDATEFAILED = "UpdateFailed"
    DELETED = "Deleted"


class PartnerAppType:
    """PartnerAppType enum values."""

    LAKERA_GUARD = "lakera-guard"
    COMET = "comet"
    DEEPCHECKS_LLM_EVALUATION = "deepchecks-llm-evaluation"
    FIDDLER = "fiddler"


class Peft:
    """Peft enum values."""

    LORA = "LORA"


class PipelineExecutionStatus:
    """PipelineExecutionStatus enum values."""

    EXECUTING = "Executing"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"


class PipelineStatus:
    """PipelineStatus enum values."""

    ACTIVE = "Active"
    DELETING = "Deleting"


class PreemptTeamTasks:
    """PreemptTeamTasks enum values."""

    NEVER = "Never"
    LOWERPRIORITY = "LowerPriority"


class ProblemType:
    """ProblemType enum values."""

    BINARYCLASSIFICATION = "BinaryClassification"
    MULTICLASSCLASSIFICATION = "MulticlassClassification"
    REGRESSION = "Regression"


class ProcessingInstanceType:
    """ProcessingInstanceType enum values."""

    ML_T3_MEDIUM = "ml.t3.medium"
    ML_T3_LARGE = "ml.t3.large"
    ML_T3_XLARGE = "ml.t3.xlarge"
    ML_T3_2XLARGE = "ml.t3.2xlarge"
    ML_M4_XLARGE = "ml.m4.xlarge"
    ML_M4_2XLARGE = "ml.m4.2xlarge"
    ML_M4_4XLARGE = "ml.m4.4xlarge"
    ML_M4_10XLARGE = "ml.m4.10xlarge"
    ML_M4_16XLARGE = "ml.m4.16xlarge"
    ML_C4_XLARGE = "ml.c4.xlarge"
    ML_C4_2XLARGE = "ml.c4.2xlarge"
    ML_C4_4XLARGE = "ml.c4.4xlarge"
    ML_C4_8XLARGE = "ml.c4.8xlarge"
    ML_P2_XLARGE = "ml.p2.xlarge"
    ML_P2_8XLARGE = "ml.p2.8xlarge"
    ML_P2_16XLARGE = "ml.p2.16xlarge"
    ML_P3_2XLARGE = "ml.p3.2xlarge"
    ML_P3_8XLARGE = "ml.p3.8xlarge"
    ML_P3_16XLARGE = "ml.p3.16xlarge"
    ML_C5_XLARGE = "ml.c5.xlarge"
    ML_C5_2XLARGE = "ml.c5.2xlarge"
    ML_C5_4XLARGE = "ml.c5.4xlarge"
    ML_C5_9XLARGE = "ml.c5.9xlarge"
    ML_C5_18XLARGE = "ml.c5.18xlarge"
    ML_M5_LARGE = "ml.m5.large"
    ML_M5_XLARGE = "ml.m5.xlarge"
    ML_M5_2XLARGE = "ml.m5.2xlarge"
    ML_M5_4XLARGE = "ml.m5.4xlarge"
    ML_M5_12XLARGE = "ml.m5.12xlarge"
    ML_M5_24XLARGE = "ml.m5.24xlarge"
    ML_R5_LARGE = "ml.r5.large"
    ML_R5_XLARGE = "ml.r5.xlarge"
    ML_R5_2XLARGE = "ml.r5.2xlarge"
    ML_R5_4XLARGE = "ml.r5.4xlarge"
    ML_R5_8XLARGE = "ml.r5.8xlarge"
    ML_R5_12XLARGE = "ml.r5.12xlarge"
    ML_R5_16XLARGE = "ml.r5.16xlarge"
    ML_R5_24XLARGE = "ml.r5.24xlarge"
    ML_G4DN_XLARGE = "ml.g4dn.xlarge"
    ML_G4DN_2XLARGE = "ml.g4dn.2xlarge"
    ML_G4DN_4XLARGE = "ml.g4dn.4xlarge"
    ML_G4DN_8XLARGE = "ml.g4dn.8xlarge"
    ML_G4DN_12XLARGE = "ml.g4dn.12xlarge"
    ML_G4DN_16XLARGE = "ml.g4dn.16xlarge"
    ML_G5_XLARGE = "ml.g5.xlarge"
    ML_G5_2XLARGE = "ml.g5.2xlarge"
    ML_G5_4XLARGE = "ml.g5.4xlarge"
    ML_G5_8XLARGE = "ml.g5.8xlarge"
    ML_G5_16XLARGE = "ml.g5.16xlarge"
    ML_G5_12XLARGE = "ml.g5.12xlarge"
    ML_G5_24XLARGE = "ml.g5.24xlarge"
    ML_G5_48XLARGE = "ml.g5.48xlarge"
    ML_R5D_LARGE = "ml.r5d.large"
    ML_R5D_XLARGE = "ml.r5d.xlarge"
    ML_R5D_2XLARGE = "ml.r5d.2xlarge"
    ML_R5D_4XLARGE = "ml.r5d.4xlarge"
    ML_R5D_8XLARGE = "ml.r5d.8xlarge"
    ML_R5D_12XLARGE = "ml.r5d.12xlarge"
    ML_R5D_16XLARGE = "ml.r5d.16xlarge"
    ML_R5D_24XLARGE = "ml.r5d.24xlarge"
    ML_G6_XLARGE = "ml.g6.xlarge"
    ML_G6_2XLARGE = "ml.g6.2xlarge"
    ML_G6_4XLARGE = "ml.g6.4xlarge"
    ML_G6_8XLARGE = "ml.g6.8xlarge"
    ML_G6_12XLARGE = "ml.g6.12xlarge"
    ML_G6_16XLARGE = "ml.g6.16xlarge"
    ML_G6_24XLARGE = "ml.g6.24xlarge"
    ML_G6_48XLARGE = "ml.g6.48xlarge"
    ML_G6E_XLARGE = "ml.g6e.xlarge"
    ML_G6E_2XLARGE = "ml.g6e.2xlarge"
    ML_G6E_4XLARGE = "ml.g6e.4xlarge"
    ML_G6E_8XLARGE = "ml.g6e.8xlarge"
    ML_G6E_12XLARGE = "ml.g6e.12xlarge"
    ML_G6E_16XLARGE = "ml.g6e.16xlarge"
    ML_G6E_24XLARGE = "ml.g6e.24xlarge"
    ML_G6E_48XLARGE = "ml.g6e.48xlarge"
    ML_M6I_LARGE = "ml.m6i.large"
    ML_M6I_XLARGE = "ml.m6i.xlarge"
    ML_M6I_2XLARGE = "ml.m6i.2xlarge"
    ML_M6I_4XLARGE = "ml.m6i.4xlarge"
    ML_M6I_8XLARGE = "ml.m6i.8xlarge"
    ML_M6I_12XLARGE = "ml.m6i.12xlarge"
    ML_M6I_16XLARGE = "ml.m6i.16xlarge"
    ML_M6I_24XLARGE = "ml.m6i.24xlarge"
    ML_M6I_32XLARGE = "ml.m6i.32xlarge"
    ML_C6I_XLARGE = "ml.c6i.xlarge"
    ML_C6I_2XLARGE = "ml.c6i.2xlarge"
    ML_C6I_4XLARGE = "ml.c6i.4xlarge"
    ML_C6I_8XLARGE = "ml.c6i.8xlarge"
    ML_C6I_12XLARGE = "ml.c6i.12xlarge"
    ML_C6I_16XLARGE = "ml.c6i.16xlarge"
    ML_C6I_24XLARGE = "ml.c6i.24xlarge"
    ML_C6I_32XLARGE = "ml.c6i.32xlarge"
    ML_M7I_LARGE = "ml.m7i.large"
    ML_M7I_XLARGE = "ml.m7i.xlarge"
    ML_M7I_2XLARGE = "ml.m7i.2xlarge"
    ML_M7I_4XLARGE = "ml.m7i.4xlarge"
    ML_M7I_8XLARGE = "ml.m7i.8xlarge"
    ML_M7I_12XLARGE = "ml.m7i.12xlarge"
    ML_M7I_16XLARGE = "ml.m7i.16xlarge"
    ML_M7I_24XLARGE = "ml.m7i.24xlarge"
    ML_M7I_48XLARGE = "ml.m7i.48xlarge"
    ML_C7I_LARGE = "ml.c7i.large"
    ML_C7I_XLARGE = "ml.c7i.xlarge"
    ML_C7I_2XLARGE = "ml.c7i.2xlarge"
    ML_C7I_4XLARGE = "ml.c7i.4xlarge"
    ML_C7I_8XLARGE = "ml.c7i.8xlarge"
    ML_C7I_12XLARGE = "ml.c7i.12xlarge"
    ML_C7I_16XLARGE = "ml.c7i.16xlarge"
    ML_C7I_24XLARGE = "ml.c7i.24xlarge"
    ML_C7I_48XLARGE = "ml.c7i.48xlarge"
    ML_R7I_LARGE = "ml.r7i.large"
    ML_R7I_XLARGE = "ml.r7i.xlarge"
    ML_R7I_2XLARGE = "ml.r7i.2xlarge"
    ML_R7I_4XLARGE = "ml.r7i.4xlarge"
    ML_R7I_8XLARGE = "ml.r7i.8xlarge"
    ML_R7I_12XLARGE = "ml.r7i.12xlarge"
    ML_R7I_16XLARGE = "ml.r7i.16xlarge"
    ML_R7I_24XLARGE = "ml.r7i.24xlarge"
    ML_R7I_48XLARGE = "ml.r7i.48xlarge"
    ML_P5_4XLARGE = "ml.p5.4xlarge"


class ProcessingJobStatus:
    """ProcessingJobStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"


class ProcessingS3CompressionType:
    """ProcessingS3CompressionType enum values."""

    NONE = "None"
    GZIP = "Gzip"


class ProcessingS3DataDistributionType:
    """ProcessingS3DataDistributionType enum values."""

    FULLYREPLICATED = "FullyReplicated"
    SHARDEDBYS3KEY = "ShardedByS3Key"


class ProcessingS3DataType:
    """ProcessingS3DataType enum values."""

    MANIFESTFILE = "ManifestFile"
    S3PREFIX = "S3Prefix"


class ProcessingS3InputMode:
    """ProcessingS3InputMode enum values."""

    PIPE = "Pipe"
    FILE = "File"


class ProcessingS3UploadMode:
    """ProcessingS3UploadMode enum values."""

    CONTINUOUS = "Continuous"
    ENDOFJOB = "EndOfJob"


class Processor:
    """Processor enum values."""

    CPU = "CPU"
    GPU = "GPU"


class ProductionVariantAcceleratorType:
    """ProductionVariantAcceleratorType enum values."""

    ML_EIA1_MEDIUM = "ml.eia1.medium"
    ML_EIA1_LARGE = "ml.eia1.large"
    ML_EIA1_XLARGE = "ml.eia1.xlarge"
    ML_EIA2_MEDIUM = "ml.eia2.medium"
    ML_EIA2_LARGE = "ml.eia2.large"
    ML_EIA2_XLARGE = "ml.eia2.xlarge"


class ProductionVariantInferenceAmiVersion:
    """ProductionVariantInferenceAmiVersion enum values."""

    AL2_AMI_SAGEMAKER_INFERENCE_GPU_2 = "al2-ami-sagemaker-inference-gpu-2"
    AL2_AMI_SAGEMAKER_INFERENCE_GPU_2_1 = "al2-ami-sagemaker-inference-gpu-2-1"
    AL2_AMI_SAGEMAKER_INFERENCE_GPU_3_1 = "al2-ami-sagemaker-inference-gpu-3-1"
    AL2_AMI_SAGEMAKER_INFERENCE_NEURON_2 = "al2-ami-sagemaker-inference-neuron-2"


class ProductionVariantInstanceType:
    """ProductionVariantInstanceType enum values."""

    ML_T2_MEDIUM = "ml.t2.medium"
    ML_T2_LARGE = "ml.t2.large"
    ML_T2_XLARGE = "ml.t2.xlarge"
    ML_T2_2XLARGE = "ml.t2.2xlarge"
    ML_M4_XLARGE = "ml.m4.xlarge"
    ML_M4_2XLARGE = "ml.m4.2xlarge"
    ML_M4_4XLARGE = "ml.m4.4xlarge"
    ML_M4_10XLARGE = "ml.m4.10xlarge"
    ML_M4_16XLARGE = "ml.m4.16xlarge"
    ML_M5_LARGE = "ml.m5.large"
    ML_M5_XLARGE = "ml.m5.xlarge"
    ML_M5_2XLARGE = "ml.m5.2xlarge"
    ML_M5_4XLARGE = "ml.m5.4xlarge"
    ML_M5_12XLARGE = "ml.m5.12xlarge"
    ML_M5_24XLARGE = "ml.m5.24xlarge"
    ML_M5D_LARGE = "ml.m5d.large"
    ML_M5D_XLARGE = "ml.m5d.xlarge"
    ML_M5D_2XLARGE = "ml.m5d.2xlarge"
    ML_M5D_4XLARGE = "ml.m5d.4xlarge"
    ML_M5D_12XLARGE = "ml.m5d.12xlarge"
    ML_M5D_24XLARGE = "ml.m5d.24xlarge"
    ML_C4_LARGE = "ml.c4.large"
    ML_C4_XLARGE = "ml.c4.xlarge"
    ML_C4_2XLARGE = "ml.c4.2xlarge"
    ML_C4_4XLARGE = "ml.c4.4xlarge"
    ML_C4_8XLARGE = "ml.c4.8xlarge"
    ML_P2_XLARGE = "ml.p2.xlarge"
    ML_P2_8XLARGE = "ml.p2.8xlarge"
    ML_P2_16XLARGE = "ml.p2.16xlarge"
    ML_P3_2XLARGE = "ml.p3.2xlarge"
    ML_P3_8XLARGE = "ml.p3.8xlarge"
    ML_P3_16XLARGE = "ml.p3.16xlarge"
    ML_C5_LARGE = "ml.c5.large"
    ML_C5_XLARGE = "ml.c5.xlarge"
    ML_C5_2XLARGE = "ml.c5.2xlarge"
    ML_C5_4XLARGE = "ml.c5.4xlarge"
    ML_C5_9XLARGE = "ml.c5.9xlarge"
    ML_C5_18XLARGE = "ml.c5.18xlarge"
    ML_C5D_LARGE = "ml.c5d.large"
    ML_C5D_XLARGE = "ml.c5d.xlarge"
    ML_C5D_2XLARGE = "ml.c5d.2xlarge"
    ML_C5D_4XLARGE = "ml.c5d.4xlarge"
    ML_C5D_9XLARGE = "ml.c5d.9xlarge"
    ML_C5D_18XLARGE = "ml.c5d.18xlarge"
    ML_G4DN_XLARGE = "ml.g4dn.xlarge"
    ML_G4DN_2XLARGE = "ml.g4dn.2xlarge"
    ML_G4DN_4XLARGE = "ml.g4dn.4xlarge"
    ML_G4DN_8XLARGE = "ml.g4dn.8xlarge"
    ML_G4DN_12XLARGE = "ml.g4dn.12xlarge"
    ML_G4DN_16XLARGE = "ml.g4dn.16xlarge"
    ML_R5_LARGE = "ml.r5.large"
    ML_R5_XLARGE = "ml.r5.xlarge"
    ML_R5_2XLARGE = "ml.r5.2xlarge"
    ML_R5_4XLARGE = "ml.r5.4xlarge"
    ML_R5_12XLARGE = "ml.r5.12xlarge"
    ML_R5_24XLARGE = "ml.r5.24xlarge"
    ML_R5D_LARGE = "ml.r5d.large"
    ML_R5D_XLARGE = "ml.r5d.xlarge"
    ML_R5D_2XLARGE = "ml.r5d.2xlarge"
    ML_R5D_4XLARGE = "ml.r5d.4xlarge"
    ML_R5D_12XLARGE = "ml.r5d.12xlarge"
    ML_R5D_24XLARGE = "ml.r5d.24xlarge"
    ML_INF1_XLARGE = "ml.inf1.xlarge"
    ML_INF1_2XLARGE = "ml.inf1.2xlarge"
    ML_INF1_6XLARGE = "ml.inf1.6xlarge"
    ML_INF1_24XLARGE = "ml.inf1.24xlarge"
    ML_DL1_24XLARGE = "ml.dl1.24xlarge"
    ML_C6I_LARGE = "ml.c6i.large"
    ML_C6I_XLARGE = "ml.c6i.xlarge"
    ML_C6I_2XLARGE = "ml.c6i.2xlarge"
    ML_C6I_4XLARGE = "ml.c6i.4xlarge"
    ML_C6I_8XLARGE = "ml.c6i.8xlarge"
    ML_C6I_12XLARGE = "ml.c6i.12xlarge"
    ML_C6I_16XLARGE = "ml.c6i.16xlarge"
    ML_C6I_24XLARGE = "ml.c6i.24xlarge"
    ML_C6I_32XLARGE = "ml.c6i.32xlarge"
    ML_M6I_LARGE = "ml.m6i.large"
    ML_M6I_XLARGE = "ml.m6i.xlarge"
    ML_M6I_2XLARGE = "ml.m6i.2xlarge"
    ML_M6I_4XLARGE = "ml.m6i.4xlarge"
    ML_M6I_8XLARGE = "ml.m6i.8xlarge"
    ML_M6I_12XLARGE = "ml.m6i.12xlarge"
    ML_M6I_16XLARGE = "ml.m6i.16xlarge"
    ML_M6I_24XLARGE = "ml.m6i.24xlarge"
    ML_M6I_32XLARGE = "ml.m6i.32xlarge"
    ML_R6I_LARGE = "ml.r6i.large"
    ML_R6I_XLARGE = "ml.r6i.xlarge"
    ML_R6I_2XLARGE = "ml.r6i.2xlarge"
    ML_R6I_4XLARGE = "ml.r6i.4xlarge"
    ML_R6I_8XLARGE = "ml.r6i.8xlarge"
    ML_R6I_12XLARGE = "ml.r6i.12xlarge"
    ML_R6I_16XLARGE = "ml.r6i.16xlarge"
    ML_R6I_24XLARGE = "ml.r6i.24xlarge"
    ML_R6I_32XLARGE = "ml.r6i.32xlarge"
    ML_G5_XLARGE = "ml.g5.xlarge"
    ML_G5_2XLARGE = "ml.g5.2xlarge"
    ML_G5_4XLARGE = "ml.g5.4xlarge"
    ML_G5_8XLARGE = "ml.g5.8xlarge"
    ML_G5_12XLARGE = "ml.g5.12xlarge"
    ML_G5_16XLARGE = "ml.g5.16xlarge"
    ML_G5_24XLARGE = "ml.g5.24xlarge"
    ML_G5_48XLARGE = "ml.g5.48xlarge"
    ML_G6_XLARGE = "ml.g6.xlarge"
    ML_G6_2XLARGE = "ml.g6.2xlarge"
    ML_G6_4XLARGE = "ml.g6.4xlarge"
    ML_G6_8XLARGE = "ml.g6.8xlarge"
    ML_G6_12XLARGE = "ml.g6.12xlarge"
    ML_G6_16XLARGE = "ml.g6.16xlarge"
    ML_G6_24XLARGE = "ml.g6.24xlarge"
    ML_G6_48XLARGE = "ml.g6.48xlarge"
    ML_R8G_MEDIUM = "ml.r8g.medium"
    ML_R8G_LARGE = "ml.r8g.large"
    ML_R8G_XLARGE = "ml.r8g.xlarge"
    ML_R8G_2XLARGE = "ml.r8g.2xlarge"
    ML_R8G_4XLARGE = "ml.r8g.4xlarge"
    ML_R8G_8XLARGE = "ml.r8g.8xlarge"
    ML_R8G_12XLARGE = "ml.r8g.12xlarge"
    ML_R8G_16XLARGE = "ml.r8g.16xlarge"
    ML_R8G_24XLARGE = "ml.r8g.24xlarge"
    ML_R8G_48XLARGE = "ml.r8g.48xlarge"
    ML_G6E_XLARGE = "ml.g6e.xlarge"
    ML_G6E_2XLARGE = "ml.g6e.2xlarge"
    ML_G6E_4XLARGE = "ml.g6e.4xlarge"
    ML_G6E_8XLARGE = "ml.g6e.8xlarge"
    ML_G6E_12XLARGE = "ml.g6e.12xlarge"
    ML_G6E_16XLARGE = "ml.g6e.16xlarge"
    ML_G6E_24XLARGE = "ml.g6e.24xlarge"
    ML_G6E_48XLARGE = "ml.g6e.48xlarge"
    ML_P4D_24XLARGE = "ml.p4d.24xlarge"
    ML_C7G_LARGE = "ml.c7g.large"
    ML_C7G_XLARGE = "ml.c7g.xlarge"
    ML_C7G_2XLARGE = "ml.c7g.2xlarge"
    ML_C7G_4XLARGE = "ml.c7g.4xlarge"
    ML_C7G_8XLARGE = "ml.c7g.8xlarge"
    ML_C7G_12XLARGE = "ml.c7g.12xlarge"
    ML_C7G_16XLARGE = "ml.c7g.16xlarge"
    ML_M6G_LARGE = "ml.m6g.large"
    ML_M6G_XLARGE = "ml.m6g.xlarge"
    ML_M6G_2XLARGE = "ml.m6g.2xlarge"
    ML_M6G_4XLARGE = "ml.m6g.4xlarge"
    ML_M6G_8XLARGE = "ml.m6g.8xlarge"
    ML_M6G_12XLARGE = "ml.m6g.12xlarge"
    ML_M6G_16XLARGE = "ml.m6g.16xlarge"
    ML_M6GD_LARGE = "ml.m6gd.large"
    ML_M6GD_XLARGE = "ml.m6gd.xlarge"
    ML_M6GD_2XLARGE = "ml.m6gd.2xlarge"
    ML_M6GD_4XLARGE = "ml.m6gd.4xlarge"
    ML_M6GD_8XLARGE = "ml.m6gd.8xlarge"
    ML_M6GD_12XLARGE = "ml.m6gd.12xlarge"
    ML_M6GD_16XLARGE = "ml.m6gd.16xlarge"
    ML_C6G_LARGE = "ml.c6g.large"
    ML_C6G_XLARGE = "ml.c6g.xlarge"
    ML_C6G_2XLARGE = "ml.c6g.2xlarge"
    ML_C6G_4XLARGE = "ml.c6g.4xlarge"
    ML_C6G_8XLARGE = "ml.c6g.8xlarge"
    ML_C6G_12XLARGE = "ml.c6g.12xlarge"
    ML_C6G_16XLARGE = "ml.c6g.16xlarge"
    ML_C6GD_LARGE = "ml.c6gd.large"
    ML_C6GD_XLARGE = "ml.c6gd.xlarge"
    ML_C6GD_2XLARGE = "ml.c6gd.2xlarge"
    ML_C6GD_4XLARGE = "ml.c6gd.4xlarge"
    ML_C6GD_8XLARGE = "ml.c6gd.8xlarge"
    ML_C6GD_12XLARGE = "ml.c6gd.12xlarge"
    ML_C6GD_16XLARGE = "ml.c6gd.16xlarge"
    ML_C6GN_LARGE = "ml.c6gn.large"
    ML_C6GN_XLARGE = "ml.c6gn.xlarge"
    ML_C6GN_2XLARGE = "ml.c6gn.2xlarge"
    ML_C6GN_4XLARGE = "ml.c6gn.4xlarge"
    ML_C6GN_8XLARGE = "ml.c6gn.8xlarge"
    ML_C6GN_12XLARGE = "ml.c6gn.12xlarge"
    ML_C6GN_16XLARGE = "ml.c6gn.16xlarge"
    ML_R6G_LARGE = "ml.r6g.large"
    ML_R6G_XLARGE = "ml.r6g.xlarge"
    ML_R6G_2XLARGE = "ml.r6g.2xlarge"
    ML_R6G_4XLARGE = "ml.r6g.4xlarge"
    ML_R6G_8XLARGE = "ml.r6g.8xlarge"
    ML_R6G_12XLARGE = "ml.r6g.12xlarge"
    ML_R6G_16XLARGE = "ml.r6g.16xlarge"
    ML_R6GD_LARGE = "ml.r6gd.large"
    ML_R6GD_XLARGE = "ml.r6gd.xlarge"
    ML_R6GD_2XLARGE = "ml.r6gd.2xlarge"
    ML_R6GD_4XLARGE = "ml.r6gd.4xlarge"
    ML_R6GD_8XLARGE = "ml.r6gd.8xlarge"
    ML_R6GD_12XLARGE = "ml.r6gd.12xlarge"
    ML_R6GD_16XLARGE = "ml.r6gd.16xlarge"
    ML_P4DE_24XLARGE = "ml.p4de.24xlarge"
    ML_TRN1_2XLARGE = "ml.trn1.2xlarge"
    ML_TRN1_32XLARGE = "ml.trn1.32xlarge"
    ML_TRN1N_32XLARGE = "ml.trn1n.32xlarge"
    ML_TRN2_48XLARGE = "ml.trn2.48xlarge"
    ML_INF2_XLARGE = "ml.inf2.xlarge"
    ML_INF2_8XLARGE = "ml.inf2.8xlarge"
    ML_INF2_24XLARGE = "ml.inf2.24xlarge"
    ML_INF2_48XLARGE = "ml.inf2.48xlarge"
    ML_P5_48XLARGE = "ml.p5.48xlarge"
    ML_P5E_48XLARGE = "ml.p5e.48xlarge"
    ML_P5EN_48XLARGE = "ml.p5en.48xlarge"
    ML_M7I_LARGE = "ml.m7i.large"
    ML_M7I_XLARGE = "ml.m7i.xlarge"
    ML_M7I_2XLARGE = "ml.m7i.2xlarge"
    ML_M7I_4XLARGE = "ml.m7i.4xlarge"
    ML_M7I_8XLARGE = "ml.m7i.8xlarge"
    ML_M7I_12XLARGE = "ml.m7i.12xlarge"
    ML_M7I_16XLARGE = "ml.m7i.16xlarge"
    ML_M7I_24XLARGE = "ml.m7i.24xlarge"
    ML_M7I_48XLARGE = "ml.m7i.48xlarge"
    ML_C7I_LARGE = "ml.c7i.large"
    ML_C7I_XLARGE = "ml.c7i.xlarge"
    ML_C7I_2XLARGE = "ml.c7i.2xlarge"
    ML_C7I_4XLARGE = "ml.c7i.4xlarge"
    ML_C7I_8XLARGE = "ml.c7i.8xlarge"
    ML_C7I_12XLARGE = "ml.c7i.12xlarge"
    ML_C7I_16XLARGE = "ml.c7i.16xlarge"
    ML_C7I_24XLARGE = "ml.c7i.24xlarge"
    ML_C7I_48XLARGE = "ml.c7i.48xlarge"
    ML_R7I_LARGE = "ml.r7i.large"
    ML_R7I_XLARGE = "ml.r7i.xlarge"
    ML_R7I_2XLARGE = "ml.r7i.2xlarge"
    ML_R7I_4XLARGE = "ml.r7i.4xlarge"
    ML_R7I_8XLARGE = "ml.r7i.8xlarge"
    ML_R7I_12XLARGE = "ml.r7i.12xlarge"
    ML_R7I_16XLARGE = "ml.r7i.16xlarge"
    ML_R7I_24XLARGE = "ml.r7i.24xlarge"
    ML_R7I_48XLARGE = "ml.r7i.48xlarge"
    ML_C8G_MEDIUM = "ml.c8g.medium"
    ML_C8G_LARGE = "ml.c8g.large"
    ML_C8G_XLARGE = "ml.c8g.xlarge"
    ML_C8G_2XLARGE = "ml.c8g.2xlarge"
    ML_C8G_4XLARGE = "ml.c8g.4xlarge"
    ML_C8G_8XLARGE = "ml.c8g.8xlarge"
    ML_C8G_12XLARGE = "ml.c8g.12xlarge"
    ML_C8G_16XLARGE = "ml.c8g.16xlarge"
    ML_C8G_24XLARGE = "ml.c8g.24xlarge"
    ML_C8G_48XLARGE = "ml.c8g.48xlarge"
    ML_R7GD_MEDIUM = "ml.r7gd.medium"
    ML_R7GD_LARGE = "ml.r7gd.large"
    ML_R7GD_XLARGE = "ml.r7gd.xlarge"
    ML_R7GD_2XLARGE = "ml.r7gd.2xlarge"
    ML_R7GD_4XLARGE = "ml.r7gd.4xlarge"
    ML_R7GD_8XLARGE = "ml.r7gd.8xlarge"
    ML_R7GD_12XLARGE = "ml.r7gd.12xlarge"
    ML_R7GD_16XLARGE = "ml.r7gd.16xlarge"
    ML_M8G_MEDIUM = "ml.m8g.medium"
    ML_M8G_LARGE = "ml.m8g.large"
    ML_M8G_XLARGE = "ml.m8g.xlarge"
    ML_M8G_2XLARGE = "ml.m8g.2xlarge"
    ML_M8G_4XLARGE = "ml.m8g.4xlarge"
    ML_M8G_8XLARGE = "ml.m8g.8xlarge"
    ML_M8G_12XLARGE = "ml.m8g.12xlarge"
    ML_M8G_16XLARGE = "ml.m8g.16xlarge"
    ML_M8G_24XLARGE = "ml.m8g.24xlarge"
    ML_M8G_48XLARGE = "ml.m8g.48xlarge"
    ML_C6IN_LARGE = "ml.c6in.large"
    ML_C6IN_XLARGE = "ml.c6in.xlarge"
    ML_C6IN_2XLARGE = "ml.c6in.2xlarge"
    ML_C6IN_4XLARGE = "ml.c6in.4xlarge"
    ML_C6IN_8XLARGE = "ml.c6in.8xlarge"
    ML_C6IN_12XLARGE = "ml.c6in.12xlarge"
    ML_C6IN_16XLARGE = "ml.c6in.16xlarge"
    ML_C6IN_24XLARGE = "ml.c6in.24xlarge"
    ML_C6IN_32XLARGE = "ml.c6in.32xlarge"
    ML_P6_B200_48XLARGE = "ml.p6-b200.48xlarge"
    ML_P6E_GB200_36XLARGE = "ml.p6e-gb200.36xlarge"
    ML_P5_4XLARGE = "ml.p5.4xlarge"


class ProfilingStatus:
    """ProfilingStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ProjectSortBy:
    """ProjectSortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class ProjectSortOrder:
    """ProjectSortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class ProjectStatus:
    """ProjectStatus enum values."""

    PENDING = "Pending"
    CREATEINPROGRESS = "CreateInProgress"
    CREATECOMPLETED = "CreateCompleted"
    CREATEFAILED = "CreateFailed"
    DELETEINPROGRESS = "DeleteInProgress"
    DELETEFAILED = "DeleteFailed"
    DELETECOMPLETED = "DeleteCompleted"
    UPDATEINPROGRESS = "UpdateInProgress"
    UPDATECOMPLETED = "UpdateCompleted"
    UPDATEFAILED = "UpdateFailed"


class RStudioServerProAccessStatus:
    """RStudioServerProAccessStatus enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class RStudioServerProUserGroup:
    """RStudioServerProUserGroup enum values."""

    R_STUDIO_ADMIN = "R_STUDIO_ADMIN"
    R_STUDIO_USER = "R_STUDIO_USER"


class RecommendationJobStatus:
    """RecommendationJobStatus enum values."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    DELETING = "DELETING"
    DELETED = "DELETED"


class RecommendationJobSupportedEndpointType:
    """RecommendationJobSupportedEndpointType enum values."""

    REALTIME = "RealTime"
    SERVERLESS = "Serverless"


class RecommendationJobType:
    """RecommendationJobType enum values."""

    DEFAULT = "Default"
    ADVANCED = "Advanced"


class RecommendationStatus:
    """RecommendationStatus enum values."""

    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class RecommendationStepType:
    """RecommendationStepType enum values."""

    BENCHMARK = "BENCHMARK"


class RecordWrapper:
    """RecordWrapper enum values."""

    NONE = "None"
    RECORDIO = "RecordIO"


class RedshiftResultCompressionType:
    """RedshiftResultCompressionType enum values."""

    NONE = "None"
    GZIP = "GZIP"
    BZIP2 = "BZIP2"
    ZSTD = "ZSTD"
    SNAPPY = "SNAPPY"


class RedshiftResultFormat:
    """RedshiftResultFormat enum values."""

    PARQUET = "PARQUET"
    CSV = "CSV"


class Relation:
    """Relation enum values."""

    EQUALTO = "EqualTo"
    GREATERTHANOREQUALTO = "GreaterThanOrEqualTo"


class RepositoryAccessMode:
    """RepositoryAccessMode enum values."""

    PLATFORM = "Platform"
    VPC = "Vpc"


class ReservedCapacityInstanceType:
    """ReservedCapacityInstanceType enum values."""

    ML_P4D_24XLARGE = "ml.p4d.24xlarge"
    ML_P5_48XLARGE = "ml.p5.48xlarge"
    ML_P5E_48XLARGE = "ml.p5e.48xlarge"
    ML_P5EN_48XLARGE = "ml.p5en.48xlarge"
    ML_TRN1_32XLARGE = "ml.trn1.32xlarge"
    ML_TRN2_48XLARGE = "ml.trn2.48xlarge"
    ML_P6_B200_48XLARGE = "ml.p6-b200.48xlarge"
    ML_P4DE_24XLARGE = "ml.p4de.24xlarge"
    ML_P6E_GB200_36XLARGE = "ml.p6e-gb200.36xlarge"
    ML_P5_4XLARGE = "ml.p5.4xlarge"
    ML_P6_B300_48XLARGE = "ml.p6-b300.48xlarge"


class ReservedCapacityStatus:
    """ReservedCapacityStatus enum values."""

    PENDING = "Pending"
    ACTIVE = "Active"
    SCHEDULED = "Scheduled"
    EXPIRED = "Expired"
    FAILED = "Failed"


class ReservedCapacityType:
    """ReservedCapacityType enum values."""

    ULTRASERVER = "UltraServer"
    INSTANCE = "Instance"


class ResourceCatalogSortBy:
    """ResourceCatalogSortBy enum values."""

    CREATIONTIME = "CreationTime"


class ResourceCatalogSortOrder:
    """ResourceCatalogSortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class ResourceSharingStrategy:
    """ResourceSharingStrategy enum values."""

    LEND = "Lend"
    DONTLEND = "DontLend"
    LENDANDBORROW = "LendAndBorrow"


class ResourceType:
    """ResourceType enum values."""

    TRAININGJOB = "TrainingJob"
    EXPERIMENT = "Experiment"
    EXPERIMENTTRIAL = "ExperimentTrial"
    EXPERIMENTTRIALCOMPONENT = "ExperimentTrialComponent"
    ENDPOINT = "Endpoint"
    MODEL = "Model"
    MODELPACKAGE = "ModelPackage"
    MODELPACKAGEGROUP = "ModelPackageGroup"
    PIPELINE = "Pipeline"
    PIPELINEEXECUTION = "PipelineExecution"
    FEATUREGROUP = "FeatureGroup"
    FEATUREMETADATA = "FeatureMetadata"
    IMAGE = "Image"
    IMAGEVERSION = "ImageVersion"
    PROJECT = "Project"
    HYPERPARAMETERTUNINGJOB = "HyperParameterTuningJob"
    MODELCARD = "ModelCard"
    PIPELINEVERSION = "PipelineVersion"


class RetentionType:
    """RetentionType enum values."""

    RETAIN = "Retain"
    DELETE = "Delete"


class RootAccess:
    """RootAccess enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RoutingStrategy:
    """RoutingStrategy enum values."""

    LEAST_OUTSTANDING_REQUESTS = "LEAST_OUTSTANDING_REQUESTS"
    RANDOM = "RANDOM"


class RuleEvaluationStatus:
    """RuleEvaluationStatus enum values."""

    INPROGRESS = "InProgress"
    NOISSUESFOUND = "NoIssuesFound"
    ISSUESFOUND = "IssuesFound"
    ERROR = "Error"
    STOPPING = "Stopping"
    STOPPED = "Stopped"


class S3DataDistribution:
    """S3DataDistribution enum values."""

    FULLYREPLICATED = "FullyReplicated"
    SHARDEDBYS3KEY = "ShardedByS3Key"


class S3DataType:
    """S3DataType enum values."""

    MANIFESTFILE = "ManifestFile"
    S3PREFIX = "S3Prefix"
    AUGMENTEDMANIFESTFILE = "AugmentedManifestFile"
    CONVERSE = "Converse"


class S3ModelDataType:
    """S3ModelDataType enum values."""

    S3PREFIX = "S3Prefix"
    S3OBJECT = "S3Object"


class SageMakerImageName:
    """SageMakerImageName enum values."""

    SAGEMAKER_DISTRIBUTION = "sagemaker_distribution"


class SageMakerResourceName:
    """SageMakerResourceName enum values."""

    TRAINING_JOB = "training-job"
    HYPERPOD_CLUSTER = "hyperpod-cluster"
    ENDPOINT = "endpoint"


class SagemakerServicecatalogStatus:
    """SagemakerServicecatalogStatus enum values."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ScheduleStatus:
    """ScheduleStatus enum values."""

    PENDING = "Pending"
    FAILED = "Failed"
    SCHEDULED = "Scheduled"
    STOPPED = "Stopped"


class SchedulerResourceStatus:
    """SchedulerResourceStatus enum values."""

    CREATING = "Creating"
    CREATEFAILED = "CreateFailed"
    CREATEROLLBACKFAILED = "CreateRollbackFailed"
    CREATED = "Created"
    UPDATING = "Updating"
    UPDATEFAILED = "UpdateFailed"
    UPDATEROLLBACKFAILED = "UpdateRollbackFailed"
    UPDATED = "Updated"
    DELETING = "Deleting"
    DELETEFAILED = "DeleteFailed"
    DELETEROLLBACKFAILED = "DeleteRollbackFailed"
    DELETED = "Deleted"


class SearchSortOrder:
    """SearchSortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class SecondaryStatus:
    """SecondaryStatus enum values."""

    STARTING = "Starting"
    LAUNCHINGMLINSTANCES = "LaunchingMLInstances"
    PREPARINGTRAININGSTACK = "PreparingTrainingStack"
    DOWNLOADING = "Downloading"
    DOWNLOADINGTRAININGIMAGE = "DownloadingTrainingImage"
    TRAINING = "Training"
    UPLOADING = "Uploading"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    MAXRUNTIMEEXCEEDED = "MaxRuntimeExceeded"
    COMPLETED = "Completed"
    FAILED = "Failed"
    INTERRUPTED = "Interrupted"
    MAXWAITTIMEEXCEEDED = "MaxWaitTimeExceeded"
    UPDATING = "Updating"
    RESTARTING = "Restarting"
    PENDING = "Pending"


class ServerlessJobType:
    """ServerlessJobType enum values."""

    FINETUNING = "FineTuning"
    EVALUATION = "Evaluation"


class SharingType:
    """SharingType enum values."""

    PRIVATE = "Private"
    SHARED = "Shared"


class SkipModelValidation:
    """SkipModelValidation enum values."""

    ALL = "All"
    NONE = "None"


class SoftwareUpdateStatus:
    """SoftwareUpdateStatus enum values."""

    PENDING = "Pending"
    INPROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    ROLLBACKINPROGRESS = "RollbackInProgress"
    ROLLBACKCOMPLETE = "RollbackComplete"


class SortActionsBy:
    """SortActionsBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class SortArtifactsBy:
    """SortArtifactsBy enum values."""

    CREATIONTIME = "CreationTime"


class SortAssociationsBy:
    """SortAssociationsBy enum values."""

    SOURCEARN = "SourceArn"
    DESTINATIONARN = "DestinationArn"
    SOURCETYPE = "SourceType"
    DESTINATIONTYPE = "DestinationType"
    CREATIONTIME = "CreationTime"


class SortBy:
    """SortBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class SortClusterSchedulerConfigBy:
    """SortClusterSchedulerConfigBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class SortContextsBy:
    """SortContextsBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class SortExperimentsBy:
    """SortExperimentsBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class SortInferenceExperimentsBy:
    """SortInferenceExperimentsBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class SortLineageGroupsBy:
    """SortLineageGroupsBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class SortMlflowAppBy:
    """SortMlflowAppBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class SortOrder:
    """SortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class SortPipelineExecutionsBy:
    """SortPipelineExecutionsBy enum values."""

    CREATIONTIME = "CreationTime"
    PIPELINEEXECUTIONARN = "PipelineExecutionArn"


class SortPipelinesBy:
    """SortPipelinesBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class SortQuotaBy:
    """SortQuotaBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"
    CLUSTERARN = "ClusterArn"


class SortTrackingServerBy:
    """SortTrackingServerBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"


class SortTrialComponentsBy:
    """SortTrialComponentsBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class SortTrialsBy:
    """SortTrialsBy enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"


class SpaceSortKey:
    """SpaceSortKey enum values."""

    CREATIONTIME = "CreationTime"
    LASTMODIFIEDTIME = "LastModifiedTime"


class SpaceStatus:
    """SpaceStatus enum values."""

    DELETING = "Deleting"
    FAILED = "Failed"
    INSERVICE = "InService"
    PENDING = "Pending"
    UPDATING = "Updating"
    UPDATE_FAILED = "Update_Failed"
    DELETE_FAILED = "Delete_Failed"


class SplitType:
    """SplitType enum values."""

    NONE = "None"
    LINE = "Line"
    RECORDIO = "RecordIO"
    TFRECORD = "TFRecord"


class StageStatus:
    """StageStatus enum values."""

    CREATING = "CREATING"
    READYTODEPLOY = "READYTODEPLOY"
    STARTING = "STARTING"
    INPROGRESS = "INPROGRESS"
    DEPLOYED = "DEPLOYED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"


class Statistic:
    """Statistic enum values."""

    AVERAGE = "Average"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    SAMPLECOUNT = "SampleCount"
    SUM = "Sum"


class StepStatus:
    """StepStatus enum values."""

    STARTING = "Starting"
    EXECUTING = "Executing"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"


class StorageType:
    """StorageType enum values."""

    STANDARD = "Standard"
    INMEMORY = "InMemory"


class StudioLifecycleConfigAppType:
    """StudioLifecycleConfigAppType enum values."""

    JUPYTERSERVER = "JupyterServer"
    KERNELGATEWAY = "KernelGateway"
    CODEEDITOR = "CodeEditor"
    JUPYTERLAB = "JupyterLab"


class StudioLifecycleConfigSortKey:
    """StudioLifecycleConfigSortKey enum values."""

    CREATIONTIME = "CreationTime"
    LASTMODIFIEDTIME = "LastModifiedTime"
    NAME = "Name"


class StudioWebPortal:
    """StudioWebPortal enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class TableFormat:
    """TableFormat enum values."""

    DEFAULT = "Default"
    GLUE = "Glue"
    ICEBERG = "Iceberg"


class TagPropagation:
    """TagPropagation enum values."""

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class TargetDevice:
    """TargetDevice enum values."""

    LAMBDA = "lambda"
    ML_M4 = "ml_m4"
    ML_M5 = "ml_m5"
    ML_M6G = "ml_m6g"
    ML_C4 = "ml_c4"
    ML_C5 = "ml_c5"
    ML_C6G = "ml_c6g"
    ML_P2 = "ml_p2"
    ML_P3 = "ml_p3"
    ML_G4DN = "ml_g4dn"
    ML_INF1 = "ml_inf1"
    ML_INF2 = "ml_inf2"
    ML_TRN1 = "ml_trn1"
    ML_EIA2 = "ml_eia2"
    JETSON_TX1 = "jetson_tx1"
    JETSON_TX2 = "jetson_tx2"
    JETSON_NANO = "jetson_nano"
    JETSON_XAVIER = "jetson_xavier"
    RASP3B = "rasp3b"
    RASP4B = "rasp4b"
    IMX8QM = "imx8qm"
    DEEPLENS = "deeplens"
    RK3399 = "rk3399"
    RK3288 = "rk3288"
    AISAGE = "aisage"
    SBE_C = "sbe_c"
    QCS605 = "qcs605"
    QCS603 = "qcs603"
    SITARA_AM57X = "sitara_am57x"
    AMBA_CV2 = "amba_cv2"
    AMBA_CV22 = "amba_cv22"
    AMBA_CV25 = "amba_cv25"
    X86_WIN32 = "x86_win32"
    X86_WIN64 = "x86_win64"
    COREML = "coreml"
    JACINTO_TDA4VM = "jacinto_tda4vm"
    IMX8MPLUS = "imx8mplus"


class TargetPlatformAccelerator:
    """TargetPlatformAccelerator enum values."""

    INTEL_GRAPHICS = "INTEL_GRAPHICS"
    MALI = "MALI"
    NVIDIA = "NVIDIA"
    NNA = "NNA"


class TargetPlatformArch:
    """TargetPlatformArch enum values."""

    X86_64 = "X86_64"
    X86 = "X86"
    ARM64 = "ARM64"
    ARM_EABI = "ARM_EABI"
    ARM_EABIHF = "ARM_EABIHF"


class TargetPlatformOs:
    """TargetPlatformOs enum values."""

    ANDROID = "ANDROID"
    LINUX = "LINUX"


class ThroughputMode:
    """ThroughputMode enum values."""

    ONDEMAND = "OnDemand"
    PROVISIONED = "Provisioned"


class TrackingServerMaintenanceStatus:
    """TrackingServerMaintenanceStatus enum values."""

    MAINTENANCEINPROGRESS = "MaintenanceInProgress"
    MAINTENANCECOMPLETE = "MaintenanceComplete"
    MAINTENANCEFAILED = "MaintenanceFailed"


class TrackingServerSize:
    """TrackingServerSize enum values."""

    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class TrackingServerStatus:
    """TrackingServerStatus enum values."""

    CREATING = "Creating"
    CREATED = "Created"
    CREATEFAILED = "CreateFailed"
    UPDATING = "Updating"
    UPDATED = "Updated"
    UPDATEFAILED = "UpdateFailed"
    DELETING = "Deleting"
    DELETEFAILED = "DeleteFailed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    STOPFAILED = "StopFailed"
    STARTING = "Starting"
    STARTED = "Started"
    STARTFAILED = "StartFailed"
    MAINTENANCEINPROGRESS = "MaintenanceInProgress"
    MAINTENANCECOMPLETE = "MaintenanceComplete"
    MAINTENANCEFAILED = "MaintenanceFailed"


class TrafficRoutingConfigType:
    """TrafficRoutingConfigType enum values."""

    ALL_AT_ONCE = "ALL_AT_ONCE"
    CANARY = "CANARY"
    LINEAR = "LINEAR"


class TrafficType:
    """TrafficType enum values."""

    PHASES = "PHASES"
    STAIRS = "STAIRS"


class TrainingInputMode:
    """TrainingInputMode enum values."""

    PIPE = "Pipe"
    FILE = "File"
    FASTFILE = "FastFile"


class TrainingInstanceType:
    """TrainingInstanceType enum values."""

    ML_M4_XLARGE = "ml.m4.xlarge"
    ML_M4_2XLARGE = "ml.m4.2xlarge"
    ML_M4_4XLARGE = "ml.m4.4xlarge"
    ML_M4_10XLARGE = "ml.m4.10xlarge"
    ML_M4_16XLARGE = "ml.m4.16xlarge"
    ML_G4DN_XLARGE = "ml.g4dn.xlarge"
    ML_G4DN_2XLARGE = "ml.g4dn.2xlarge"
    ML_G4DN_4XLARGE = "ml.g4dn.4xlarge"
    ML_G4DN_8XLARGE = "ml.g4dn.8xlarge"
    ML_G4DN_12XLARGE = "ml.g4dn.12xlarge"
    ML_G4DN_16XLARGE = "ml.g4dn.16xlarge"
    ML_M5_LARGE = "ml.m5.large"
    ML_M5_XLARGE = "ml.m5.xlarge"
    ML_M5_2XLARGE = "ml.m5.2xlarge"
    ML_M5_4XLARGE = "ml.m5.4xlarge"
    ML_M5_12XLARGE = "ml.m5.12xlarge"
    ML_M5_24XLARGE = "ml.m5.24xlarge"
    ML_C4_XLARGE = "ml.c4.xlarge"
    ML_C4_2XLARGE = "ml.c4.2xlarge"
    ML_C4_4XLARGE = "ml.c4.4xlarge"
    ML_C4_8XLARGE = "ml.c4.8xlarge"
    ML_P2_XLARGE = "ml.p2.xlarge"
    ML_P2_8XLARGE = "ml.p2.8xlarge"
    ML_P2_16XLARGE = "ml.p2.16xlarge"
    ML_P3_2XLARGE = "ml.p3.2xlarge"
    ML_P3_8XLARGE = "ml.p3.8xlarge"
    ML_P3_16XLARGE = "ml.p3.16xlarge"
    ML_P3DN_24XLARGE = "ml.p3dn.24xlarge"
    ML_P4D_24XLARGE = "ml.p4d.24xlarge"
    ML_P4DE_24XLARGE = "ml.p4de.24xlarge"
    ML_P5_48XLARGE = "ml.p5.48xlarge"
    ML_P5E_48XLARGE = "ml.p5e.48xlarge"
    ML_P5EN_48XLARGE = "ml.p5en.48xlarge"
    ML_C5_XLARGE = "ml.c5.xlarge"
    ML_C5_2XLARGE = "ml.c5.2xlarge"
    ML_C5_4XLARGE = "ml.c5.4xlarge"
    ML_C5_9XLARGE = "ml.c5.9xlarge"
    ML_C5_18XLARGE = "ml.c5.18xlarge"
    ML_C5N_XLARGE = "ml.c5n.xlarge"
    ML_C5N_2XLARGE = "ml.c5n.2xlarge"
    ML_C5N_4XLARGE = "ml.c5n.4xlarge"
    ML_C5N_9XLARGE = "ml.c5n.9xlarge"
    ML_C5N_18XLARGE = "ml.c5n.18xlarge"
    ML_G5_XLARGE = "ml.g5.xlarge"
    ML_G5_2XLARGE = "ml.g5.2xlarge"
    ML_G5_4XLARGE = "ml.g5.4xlarge"
    ML_G5_8XLARGE = "ml.g5.8xlarge"
    ML_G5_16XLARGE = "ml.g5.16xlarge"
    ML_G5_12XLARGE = "ml.g5.12xlarge"
    ML_G5_24XLARGE = "ml.g5.24xlarge"
    ML_G5_48XLARGE = "ml.g5.48xlarge"
    ML_G6_XLARGE = "ml.g6.xlarge"
    ML_G6_2XLARGE = "ml.g6.2xlarge"
    ML_G6_4XLARGE = "ml.g6.4xlarge"
    ML_G6_8XLARGE = "ml.g6.8xlarge"
    ML_G6_16XLARGE = "ml.g6.16xlarge"
    ML_G6_12XLARGE = "ml.g6.12xlarge"
    ML_G6_24XLARGE = "ml.g6.24xlarge"
    ML_G6_48XLARGE = "ml.g6.48xlarge"
    ML_G6E_XLARGE = "ml.g6e.xlarge"
    ML_G6E_2XLARGE = "ml.g6e.2xlarge"
    ML_G6E_4XLARGE = "ml.g6e.4xlarge"
    ML_G6E_8XLARGE = "ml.g6e.8xlarge"
    ML_G6E_16XLARGE = "ml.g6e.16xlarge"
    ML_G6E_12XLARGE = "ml.g6e.12xlarge"
    ML_G6E_24XLARGE = "ml.g6e.24xlarge"
    ML_G6E_48XLARGE = "ml.g6e.48xlarge"
    ML_TRN1_2XLARGE = "ml.trn1.2xlarge"
    ML_TRN1_32XLARGE = "ml.trn1.32xlarge"
    ML_TRN1N_32XLARGE = "ml.trn1n.32xlarge"
    ML_TRN2_48XLARGE = "ml.trn2.48xlarge"
    ML_M6I_LARGE = "ml.m6i.large"
    ML_M6I_XLARGE = "ml.m6i.xlarge"
    ML_M6I_2XLARGE = "ml.m6i.2xlarge"
    ML_M6I_4XLARGE = "ml.m6i.4xlarge"
    ML_M6I_8XLARGE = "ml.m6i.8xlarge"
    ML_M6I_12XLARGE = "ml.m6i.12xlarge"
    ML_M6I_16XLARGE = "ml.m6i.16xlarge"
    ML_M6I_24XLARGE = "ml.m6i.24xlarge"
    ML_M6I_32XLARGE = "ml.m6i.32xlarge"
    ML_C6I_XLARGE = "ml.c6i.xlarge"
    ML_C6I_2XLARGE = "ml.c6i.2xlarge"
    ML_C6I_8XLARGE = "ml.c6i.8xlarge"
    ML_C6I_4XLARGE = "ml.c6i.4xlarge"
    ML_C6I_12XLARGE = "ml.c6i.12xlarge"
    ML_C6I_16XLARGE = "ml.c6i.16xlarge"
    ML_C6I_24XLARGE = "ml.c6i.24xlarge"
    ML_C6I_32XLARGE = "ml.c6i.32xlarge"
    ML_R5D_LARGE = "ml.r5d.large"
    ML_R5D_XLARGE = "ml.r5d.xlarge"
    ML_R5D_2XLARGE = "ml.r5d.2xlarge"
    ML_R5D_4XLARGE = "ml.r5d.4xlarge"
    ML_R5D_8XLARGE = "ml.r5d.8xlarge"
    ML_R5D_12XLARGE = "ml.r5d.12xlarge"
    ML_R5D_16XLARGE = "ml.r5d.16xlarge"
    ML_R5D_24XLARGE = "ml.r5d.24xlarge"
    ML_T3_MEDIUM = "ml.t3.medium"
    ML_T3_LARGE = "ml.t3.large"
    ML_T3_XLARGE = "ml.t3.xlarge"
    ML_T3_2XLARGE = "ml.t3.2xlarge"
    ML_R5_LARGE = "ml.r5.large"
    ML_R5_XLARGE = "ml.r5.xlarge"
    ML_R5_2XLARGE = "ml.r5.2xlarge"
    ML_R5_4XLARGE = "ml.r5.4xlarge"
    ML_R5_8XLARGE = "ml.r5.8xlarge"
    ML_R5_12XLARGE = "ml.r5.12xlarge"
    ML_R5_16XLARGE = "ml.r5.16xlarge"
    ML_R5_24XLARGE = "ml.r5.24xlarge"
    ML_P6_B200_48XLARGE = "ml.p6-b200.48xlarge"
    ML_M7I_LARGE = "ml.m7i.large"
    ML_M7I_XLARGE = "ml.m7i.xlarge"
    ML_M7I_2XLARGE = "ml.m7i.2xlarge"
    ML_M7I_4XLARGE = "ml.m7i.4xlarge"
    ML_M7I_8XLARGE = "ml.m7i.8xlarge"
    ML_M7I_12XLARGE = "ml.m7i.12xlarge"
    ML_M7I_16XLARGE = "ml.m7i.16xlarge"
    ML_M7I_24XLARGE = "ml.m7i.24xlarge"
    ML_M7I_48XLARGE = "ml.m7i.48xlarge"
    ML_C7I_LARGE = "ml.c7i.large"
    ML_C7I_XLARGE = "ml.c7i.xlarge"
    ML_C7I_2XLARGE = "ml.c7i.2xlarge"
    ML_C7I_4XLARGE = "ml.c7i.4xlarge"
    ML_C7I_8XLARGE = "ml.c7i.8xlarge"
    ML_C7I_12XLARGE = "ml.c7i.12xlarge"
    ML_C7I_16XLARGE = "ml.c7i.16xlarge"
    ML_C7I_24XLARGE = "ml.c7i.24xlarge"
    ML_C7I_48XLARGE = "ml.c7i.48xlarge"
    ML_R7I_LARGE = "ml.r7i.large"
    ML_R7I_XLARGE = "ml.r7i.xlarge"
    ML_R7I_2XLARGE = "ml.r7i.2xlarge"
    ML_R7I_4XLARGE = "ml.r7i.4xlarge"
    ML_R7I_8XLARGE = "ml.r7i.8xlarge"
    ML_R7I_12XLARGE = "ml.r7i.12xlarge"
    ML_R7I_16XLARGE = "ml.r7i.16xlarge"
    ML_R7I_24XLARGE = "ml.r7i.24xlarge"
    ML_R7I_48XLARGE = "ml.r7i.48xlarge"
    ML_P6E_GB200_36XLARGE = "ml.p6e-gb200.36xlarge"
    ML_P5_4XLARGE = "ml.p5.4xlarge"
    ML_P6_B300_48XLARGE = "ml.p6-b300.48xlarge"


class TrainingJobEarlyStoppingType:
    """TrainingJobEarlyStoppingType enum values."""

    OFF = "Off"
    AUTO = "Auto"


class TrainingJobSortByOptions:
    """TrainingJobSortByOptions enum values."""

    NAME = "Name"
    CREATIONTIME = "CreationTime"
    STATUS = "Status"
    FINALOBJECTIVEMETRICVALUE = "FinalObjectiveMetricValue"


class TrainingJobStatus:
    """TrainingJobStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    DELETING = "Deleting"


class TrainingPlanFilterName:
    """TrainingPlanFilterName enum values."""

    STATUS = "Status"


class TrainingPlanSortBy:
    """TrainingPlanSortBy enum values."""

    TRAININGPLANNAME = "TrainingPlanName"
    STARTTIME = "StartTime"
    STATUS = "Status"


class TrainingPlanSortOrder:
    """TrainingPlanSortOrder enum values."""

    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class TrainingPlanStatus:
    """TrainingPlanStatus enum values."""

    PENDING = "Pending"
    ACTIVE = "Active"
    SCHEDULED = "Scheduled"
    EXPIRED = "Expired"
    FAILED = "Failed"


class TrainingRepositoryAccessMode:
    """TrainingRepositoryAccessMode enum values."""

    PLATFORM = "Platform"
    VPC = "Vpc"


class TransformInstanceType:
    """TransformInstanceType enum values."""

    ML_M4_XLARGE = "ml.m4.xlarge"
    ML_M4_2XLARGE = "ml.m4.2xlarge"
    ML_M4_4XLARGE = "ml.m4.4xlarge"
    ML_M4_10XLARGE = "ml.m4.10xlarge"
    ML_M4_16XLARGE = "ml.m4.16xlarge"
    ML_C4_XLARGE = "ml.c4.xlarge"
    ML_C4_2XLARGE = "ml.c4.2xlarge"
    ML_C4_4XLARGE = "ml.c4.4xlarge"
    ML_C4_8XLARGE = "ml.c4.8xlarge"
    ML_P2_XLARGE = "ml.p2.xlarge"
    ML_P2_8XLARGE = "ml.p2.8xlarge"
    ML_P2_16XLARGE = "ml.p2.16xlarge"
    ML_P3_2XLARGE = "ml.p3.2xlarge"
    ML_P3_8XLARGE = "ml.p3.8xlarge"
    ML_P3_16XLARGE = "ml.p3.16xlarge"
    ML_C5_XLARGE = "ml.c5.xlarge"
    ML_C5_2XLARGE = "ml.c5.2xlarge"
    ML_C5_4XLARGE = "ml.c5.4xlarge"
    ML_C5_9XLARGE = "ml.c5.9xlarge"
    ML_C5_18XLARGE = "ml.c5.18xlarge"
    ML_M5_LARGE = "ml.m5.large"
    ML_M5_XLARGE = "ml.m5.xlarge"
    ML_M5_2XLARGE = "ml.m5.2xlarge"
    ML_M5_4XLARGE = "ml.m5.4xlarge"
    ML_M5_12XLARGE = "ml.m5.12xlarge"
    ML_M5_24XLARGE = "ml.m5.24xlarge"
    ML_M6I_LARGE = "ml.m6i.large"
    ML_M6I_XLARGE = "ml.m6i.xlarge"
    ML_M6I_2XLARGE = "ml.m6i.2xlarge"
    ML_M6I_4XLARGE = "ml.m6i.4xlarge"
    ML_M6I_8XLARGE = "ml.m6i.8xlarge"
    ML_M6I_12XLARGE = "ml.m6i.12xlarge"
    ML_M6I_16XLARGE = "ml.m6i.16xlarge"
    ML_M6I_24XLARGE = "ml.m6i.24xlarge"
    ML_M6I_32XLARGE = "ml.m6i.32xlarge"
    ML_C6I_LARGE = "ml.c6i.large"
    ML_C6I_XLARGE = "ml.c6i.xlarge"
    ML_C6I_2XLARGE = "ml.c6i.2xlarge"
    ML_C6I_4XLARGE = "ml.c6i.4xlarge"
    ML_C6I_8XLARGE = "ml.c6i.8xlarge"
    ML_C6I_12XLARGE = "ml.c6i.12xlarge"
    ML_C6I_16XLARGE = "ml.c6i.16xlarge"
    ML_C6I_24XLARGE = "ml.c6i.24xlarge"
    ML_C6I_32XLARGE = "ml.c6i.32xlarge"
    ML_R6I_LARGE = "ml.r6i.large"
    ML_R6I_XLARGE = "ml.r6i.xlarge"
    ML_R6I_2XLARGE = "ml.r6i.2xlarge"
    ML_R6I_4XLARGE = "ml.r6i.4xlarge"
    ML_R6I_8XLARGE = "ml.r6i.8xlarge"
    ML_R6I_12XLARGE = "ml.r6i.12xlarge"
    ML_R6I_16XLARGE = "ml.r6i.16xlarge"
    ML_R6I_24XLARGE = "ml.r6i.24xlarge"
    ML_R6I_32XLARGE = "ml.r6i.32xlarge"
    ML_M7I_LARGE = "ml.m7i.large"
    ML_M7I_XLARGE = "ml.m7i.xlarge"
    ML_M7I_2XLARGE = "ml.m7i.2xlarge"
    ML_M7I_4XLARGE = "ml.m7i.4xlarge"
    ML_M7I_8XLARGE = "ml.m7i.8xlarge"
    ML_M7I_12XLARGE = "ml.m7i.12xlarge"
    ML_M7I_16XLARGE = "ml.m7i.16xlarge"
    ML_M7I_24XLARGE = "ml.m7i.24xlarge"
    ML_M7I_48XLARGE = "ml.m7i.48xlarge"
    ML_C7I_LARGE = "ml.c7i.large"
    ML_C7I_XLARGE = "ml.c7i.xlarge"
    ML_C7I_2XLARGE = "ml.c7i.2xlarge"
    ML_C7I_4XLARGE = "ml.c7i.4xlarge"
    ML_C7I_8XLARGE = "ml.c7i.8xlarge"
    ML_C7I_12XLARGE = "ml.c7i.12xlarge"
    ML_C7I_16XLARGE = "ml.c7i.16xlarge"
    ML_C7I_24XLARGE = "ml.c7i.24xlarge"
    ML_C7I_48XLARGE = "ml.c7i.48xlarge"
    ML_R7I_LARGE = "ml.r7i.large"
    ML_R7I_XLARGE = "ml.r7i.xlarge"
    ML_R7I_2XLARGE = "ml.r7i.2xlarge"
    ML_R7I_4XLARGE = "ml.r7i.4xlarge"
    ML_R7I_8XLARGE = "ml.r7i.8xlarge"
    ML_R7I_12XLARGE = "ml.r7i.12xlarge"
    ML_R7I_16XLARGE = "ml.r7i.16xlarge"
    ML_R7I_24XLARGE = "ml.r7i.24xlarge"
    ML_R7I_48XLARGE = "ml.r7i.48xlarge"
    ML_G4DN_XLARGE = "ml.g4dn.xlarge"
    ML_G4DN_2XLARGE = "ml.g4dn.2xlarge"
    ML_G4DN_4XLARGE = "ml.g4dn.4xlarge"
    ML_G4DN_8XLARGE = "ml.g4dn.8xlarge"
    ML_G4DN_12XLARGE = "ml.g4dn.12xlarge"
    ML_G4DN_16XLARGE = "ml.g4dn.16xlarge"
    ML_G5_XLARGE = "ml.g5.xlarge"
    ML_G5_2XLARGE = "ml.g5.2xlarge"
    ML_G5_4XLARGE = "ml.g5.4xlarge"
    ML_G5_8XLARGE = "ml.g5.8xlarge"
    ML_G5_12XLARGE = "ml.g5.12xlarge"
    ML_G5_16XLARGE = "ml.g5.16xlarge"
    ML_G5_24XLARGE = "ml.g5.24xlarge"
    ML_G5_48XLARGE = "ml.g5.48xlarge"
    ML_TRN1_2XLARGE = "ml.trn1.2xlarge"
    ML_TRN1_32XLARGE = "ml.trn1.32xlarge"
    ML_INF2_XLARGE = "ml.inf2.xlarge"
    ML_INF2_8XLARGE = "ml.inf2.8xlarge"
    ML_INF2_24XLARGE = "ml.inf2.24xlarge"
    ML_INF2_48XLARGE = "ml.inf2.48xlarge"
    ML_G6_XLARGE = "ml.g6.xlarge"
    ML_G6_2XLARGE = "ml.g6.2xlarge"
    ML_G6_4XLARGE = "ml.g6.4xlarge"
    ML_G6_8XLARGE = "ml.g6.8xlarge"
    ML_G6_12XLARGE = "ml.g6.12xlarge"
    ML_G6_16XLARGE = "ml.g6.16xlarge"
    ML_G6_24XLARGE = "ml.g6.24xlarge"
    ML_G6_48XLARGE = "ml.g6.48xlarge"


class TransformJobStatus:
    """TransformJobStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"


class TrialComponentPrimaryStatus:
    """TrialComponentPrimaryStatus enum values."""

    INPROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPING = "Stopping"
    STOPPED = "Stopped"


class TtlDurationUnit:
    """TtlDurationUnit enum values."""

    SECONDS = "Seconds"
    MINUTES = "Minutes"
    HOURS = "Hours"
    DAYS = "Days"
    WEEKS = "Weeks"


class UltraServerHealthStatus:
    """UltraServerHealthStatus enum values."""

    OK = "OK"
    IMPAIRED = "Impaired"
    INSUFFICIENT_DATA = "Insufficient-Data"


class UserProfileSortKey:
    """UserProfileSortKey enum values."""

    CREATIONTIME = "CreationTime"
    LASTMODIFIEDTIME = "LastModifiedTime"


class UserProfileStatus:
    """UserProfileStatus enum values."""

    DELETING = "Deleting"
    FAILED = "Failed"
    INSERVICE = "InService"
    PENDING = "Pending"
    UPDATING = "Updating"
    UPDATE_FAILED = "Update_Failed"
    DELETE_FAILED = "Delete_Failed"


class VariantPropertyType:
    """VariantPropertyType enum values."""

    DESIREDINSTANCECOUNT = "DesiredInstanceCount"
    DESIREDWEIGHT = "DesiredWeight"
    DATACAPTURECONFIG = "DataCaptureConfig"


class VariantStatus:
    """VariantStatus enum values."""

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    ACTIVATINGTRAFFIC = "ActivatingTraffic"
    BAKING = "Baking"


class VendorGuidance:
    """VendorGuidance enum values."""

    NOT_PROVIDED = "NOT_PROVIDED"
    STABLE = "STABLE"
    TO_BE_ARCHIVED = "TO_BE_ARCHIVED"
    ARCHIVED = "ARCHIVED"


class VolumeAttachmentStatus:
    """VolumeAttachmentStatus enum values."""

    ATTACHING = "attaching"
    ATTACHED = "attached"
    DETACHING = "detaching"
    DETACHED = "detached"
    BUSY = "busy"


class WarmPoolResourceStatus:
    """WarmPoolResourceStatus enum values."""

    AVAILABLE = "Available"
    TERMINATED = "Terminated"
    REUSED = "Reused"
    INUSE = "InUse"


class WorkforceIpAddressType:
    """WorkforceIpAddressType enum values."""

    IPV4 = "ipv4"
    DUALSTACK = "dualstack"


class WorkforceStatus:
    """WorkforceStatus enum values."""

    INITIALIZING = "Initializing"
    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"
    ACTIVE = "Active"


@dataclass
class CodeEditorAppImageConfig(PropertyType):
    CONTAINER_CONFIG = "ContainerConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_config": "ContainerConfig",
    }

    container_config: Optional[ContainerConfig] = None


@dataclass
class ContainerConfig(PropertyType):
    CONTAINER_ENTRYPOINT = "ContainerEntrypoint"
    CONTAINER_ENVIRONMENT_VARIABLES = "ContainerEnvironmentVariables"
    CONTAINER_ARGUMENTS = "ContainerArguments"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_entrypoint": "ContainerEntrypoint",
        "container_environment_variables": "ContainerEnvironmentVariables",
        "container_arguments": "ContainerArguments",
    }

    container_entrypoint: Optional[Union[list[str], Ref]] = None
    container_environment_variables: Optional[list[CustomImageContainerEnvironmentVariable]] = None
    container_arguments: Optional[Union[list[str], Ref]] = None


@dataclass
class CustomImageContainerEnvironmentVariable(PropertyType):
    VALUE = "Value"
    KEY = "Key"

    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "key": "Key",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    key: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FileSystemConfig(PropertyType):
    MOUNT_PATH = "MountPath"
    DEFAULT_GID = "DefaultGid"
    DEFAULT_UID = "DefaultUid"

    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_path": "MountPath",
        "default_gid": "DefaultGid",
        "default_uid": "DefaultUid",
    }

    mount_path: Optional[Union[str, Ref, GetAtt, Sub]] = None
    default_gid: Optional[Union[int, Ref, GetAtt, Sub]] = None
    default_uid: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class JupyterLabAppImageConfig(PropertyType):
    CONTAINER_CONFIG = "ContainerConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "container_config": "ContainerConfig",
    }

    container_config: Optional[ContainerConfig] = None


@dataclass
class KernelGatewayImageConfig(PropertyType):
    KERNEL_SPECS = "KernelSpecs"
    FILE_SYSTEM_CONFIG = "FileSystemConfig"

    _property_mappings: ClassVar[dict[str, str]] = {
        "kernel_specs": "KernelSpecs",
        "file_system_config": "FileSystemConfig",
    }

    kernel_specs: Optional[list[KernelSpec]] = None
    file_system_config: Optional[FileSystemConfig] = None


@dataclass
class KernelSpec(PropertyType):
    DISPLAY_NAME = "DisplayName"
    NAME = "Name"

    _property_mappings: ClassVar[dict[str, str]] = {
        "display_name": "DisplayName",
        "name": "Name",
    }

    display_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

