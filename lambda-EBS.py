# importing necessary modules - boto3 and datetime
import json
import boto3
from datetime import date

# Lambda function
def lambda_handler(event, context):
    
    # instanctiating ec2 using boto3 client module
    ec2 = boto3.client('ec2')
    
    # cerating a empty list to store the volumes attached
    volume_ids = []
    
    # calling describe_instaces to get the api call with volume ID
    response_ec2 = ec2.describe_instances(
        InstanceIds=['i-08e89729efed24ff5']
        )
    
    # Extracting volume id for the instance
    for reservation in response_ec2['Reservations']:
        for instance in reservation['Instances']:
            volume_ids.append(instance['BlockDeviceMappings'][0]['Ebs']['VolumeId'])  
           
    # Priting the volume id to verify 
    print(f"The volume is {volume_ids[0]}")
       
    # using create_snapshot to take snapshot of the volume and also adding a tag as it can be used in future to extract data 
    response_create_snapshot = ec2.create_snapshot(
        VolumeId=volume_ids[0],
        TagSpecifications=[
        {
            'ResourceType': 'snapshot',
            'Tags': [
                {
                    'Key':'volume_id',
                    'Value': volume_ids[0]
                },
            ]
        },
        ]
        )
    
    # Storing the created snapshot
    created_snapshot_ids = []
    
    # sotring the value
    created_snapshot_ids.append(response_create_snapshot['SnapshotId'])
    
    # Printing the list of snapshots that were created
    print(f"List of snapshots created {created_snapshot_ids}")
    
    
    # Empty list to store all the snapshots for the volume
    list_of_all_snapshots = []
    
    # Using describe_snapshots to extract the snapshots with specific tag
    all_snapshots = ec2.describe_snapshots(
        Filters=[
            {
                'Name':'tag:volume_id',
                'Values': volume_ids
            }
            ]
        )
        
    # loop to iterate each snapshot, and store it in the list
    for i in all_snapshots['Snapshots']:
        list_of_all_snapshots.append(i['SnapshotId'])
    
    # Printing the list of existing snapshot ids
    print(f"List of all the snapshots for volume {volume_ids[0]} : {list_of_all_snapshots}")
    
    # loop to iterate in all snapshots
    for snapshots in all_snapshots['Snapshots']:
        
        # retrieving the start datetime for the snapshot
        snap_start_date = snapshots['StartTime'].date()

        # current date
        current_date = date.today()

        # difference in the time stamps to get the age
        diff = (current_date-snap_start_date).days
        
        
        if diff > 30:
            # Printing snapshot Id that will be deleted
            print(f"Deleting the snap ID {snapshots['SnapshotId']} as it is older than 30 days")
            
            # Using delete_snapshot to delete the snapshot
            response_delete_snap = ec2.delete_snapshot(
                SnapshotId=snapshots
            )
        else:
            
            # If none aged more than 30 days, no action will be taken
            print(f"This snap age is {diff} days, no action being taken snap-id {snapshots['SnapshotId']}")
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
