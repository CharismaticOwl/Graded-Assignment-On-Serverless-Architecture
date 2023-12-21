# importing necessary modules - boto3 and datetime
import json
import boto3

# Lambda function
def lambda_handler(event, context):
    
    
    # boto3 command to store invoke client for rds
    rds = boto3.client('rds')
    
    # using describe_db_instances getting response for our RDS - name - assignment-q3
    response = rds.describe_db_instances(
            DBInstanceIdentifier='assignment-q3'
        )
        
    # Storing the response in a variable
    
    db_data = response['DBInstances']
    
    # priting the details of our db instance
    print(db_data)
    
    # using create_db_snapshot creating a snapshot of our db instance
    response_snapshot = rds.create_db_snapshot(
            # snapshot identifier is provided by us
            DBSnapshotIdentifier='Lambda-invoked-snapshot-2',
            
            # specifiying the db instance for which we want a snapshot
            DBInstanceIdentifier='assignment-q3'
        )
        
    # Storing the response in a variable
    db_snapshot_data = response_snapshot['DBSnapshot']
    
    # priting the details of our snapshot for the db instance
    print(db_snapshot_data)
    
    # once the task is completed the function will throw below status code
    return {
        'statusCode': 'done'
    }
