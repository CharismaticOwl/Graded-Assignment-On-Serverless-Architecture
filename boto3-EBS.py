import boto3
from datetime import date

ec2 = boto3.client('ec2')

response_ec2 = ec2.describe_instances(
    InstanceIds=['i-08e89729efed24ff5']
)

volume_ids=[]

for reservation in response_ec2['Reservations']:
    for instance in reservation['Instances']:
        volume_ids.append(instance['BlockDeviceMappings'][0]['Ebs']['VolumeId'])

print(volume_ids[0])

response_volume = ec2.describe_volumes(
    VolumeIds=volume_ids
)


response_snapshot_create = ec2.create_snapshot(
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
    ],
)

created_snapshot_ids = []

created_snapshot_ids.append(response_snapshot_create['SnapshotId'])

print(f"Snapshot is created with SnapshotId {created_snapshot_ids[0]}")

f = open('created_snapshot.txt','a+')

f.write(f"{created_snapshot_ids[0]}\n")

f.close()

##################################################

list_of_snapshots = []
all_snapshots = ec2.describe_snapshots(
    Filters=[
        {
            'Name':'tag:volume_id',
            'Values': volume_ids
            }
        ]
    )

for i in all_snapshots['Snapshots']:
    list_of_snapshots.append(i['SnapshotId'])

print(list_of_snapshots)

for snapshots in all_snapshots['Snapshots']:
    snap_start_date = snapshots['StartTime'].date()

    current_date = date.today()

    diff = (current_date-snap_start_date).days

    if diff > 30:
        print(f"Deleting the snap ID {snapshots['SnapshotId']} as it is older than 30 days")
        g = open('deleted_snapshot.txt','a')

        g.write(f"{snapshots['SnapshotId']}\n")

        g.close()
        response_delete_snap = ec2.delete_snapshot(
            SnapshotId=j
        )
    else:
        print(f"This snap age is {diff} days, no action being taken snap-id {snapshots['SnapshotId']}")