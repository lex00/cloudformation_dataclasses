# DynamoDB CloudFormation Examples

Examples demonstrating DynamoDB table creation using `cloudformation-dataclasses`.

## Examples

### simple_table.py

A simple DynamoDB table with:
- Hash key only (configurable name and type via parameters)
- Provisioned throughput (configurable via parameters)
- Point-in-time recovery enabled

Inspired by [AWS's DynamoDB_Table.yaml](https://github.com/awslabs/aws-cloudformation-templates/blob/master/DynamoDB/DynamoDB_Table.yaml).

#### Usage

```bash
python simple_table.py
```

#### Generated Template Structure

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: AWS CloudFormation Sample Template DynamoDB_Table...
Parameters:
  HashKeyName:
    Type: String
    Default: id
  HashKeyType:
    Type: String
    Default: S
  ReadCapacity:
    Type: Number
    Default: 5
  WriteCapacity:
    Type: Number
    Default: 10
Resources:
  MyTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: !Ref HashKeyName
          AttributeType: !Ref HashKeyType
      KeySchema:
        - AttributeName: !Ref HashKeyName
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: !Ref ReadCapacity
        WriteCapacityUnits: !Ref WriteCapacity
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true
Outputs:
  TableName:
    Value: !Ref MyTable
```

---

### secondary_indexes.py

A DynamoDB table demonstrating secondary indexes:
- Composite primary key: `Category` (HASH) + `Title` (RANGE)
- Local Secondary Index (LSI): `LanguageIndex` for querying by language within a category
- Global Secondary Index (GSI): `TitleIndex` for querying by title across all categories
- Both indexes use `KEYS_ONLY` projection
- Point-in-time recovery enabled

Inspired by [AWS's DynamoDB_Secondary_Indexes.yaml](https://github.com/awslabs/aws-cloudformation-templates/blob/master/DynamoDB/DynamoDB_Secondary_Indexes.yaml).

#### Usage

```bash
python secondary_indexes.py
```

#### Generated Template Structure

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: AWS CloudFormation Sample Template DynamoDB_Secondary_Indexes...
Parameters:
  ReadCapacityUnits:
    Type: Number
    Default: 5
  WriteCapacityUnits:
    Type: Number
    Default: 10
Resources:
  TableOfBooks:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: Title
          AttributeType: S
        - AttributeName: Category
          AttributeType: S
        - AttributeName: Language
          AttributeType: S
      KeySchema:
        - AttributeName: Category
          KeyType: HASH
        - AttributeName: Title
          KeyType: RANGE
      ProvisionedThroughput:
        ReadCapacityUnits: !Ref ReadCapacityUnits
        WriteCapacityUnits: !Ref WriteCapacityUnits
      LocalSecondaryIndexes:
        - IndexName: LanguageIndex
          KeySchema:
            - AttributeName: Category
              KeyType: HASH
            - AttributeName: Language
              KeyType: RANGE
          Projection:
            ProjectionType: KEYS_ONLY
      GlobalSecondaryIndexes:
        - IndexName: TitleIndex
          KeySchema:
            - AttributeName: Title
              KeyType: HASH
          Projection:
            ProjectionType: KEYS_ONLY
          ProvisionedThroughput:
            ReadCapacityUnits: !Ref ReadCapacityUnits
            WriteCapacityUnits: !Ref WriteCapacityUnits
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true
Outputs:
  TableName:
    Value: !Ref TableOfBooks
```
