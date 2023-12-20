import json
import boto3

client = boto3.client('ec2')

response = client.describe_instances(
    Filters=[
        {
            'Name':'tag:tag', 'Values':['Auto-Stop','Auto-Start']
        }
    ]
)

stop_instance_ids = []

start_instance_ids = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        for tags in instance['Tags']:
            if tags['Value'] == 'Auto-Stop':
                stop_instance_ids.append(instance['InstanceId'])
            elif tags['Value'] == 'Auto-Start':
                start_instance_ids.append(instance['InstanceId'])
            else:
                print("Done")
                
print(stop_instance_ids)
print(start_instance_ids)

print("Starting Instances with tag:Auto-Start")
client.start_instances(InstanceIds=start_instance_ids)
print("start complete")

print("Stopping Instances with tag:Auto-Stop")
client.stop_instances(InstanceIds=stop_instance_ids)
print("Stop complete")