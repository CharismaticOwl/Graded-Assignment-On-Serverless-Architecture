import boto3

client = boto3.client('rds')

response = client.describe_db_instances(
    DBInstanceIdentifier='assignment-q3'
)

print(response)

response_snapshot = client.create_db_snapshot(
    DBSnapshotIdentifier='Test-snapshot',
    DBInstanceIdentifier='assignment-q3'
)

print(response_snapshot)