# importing modules - boto3 to access AWS resources using Python
import json
import boto3

# defining region
region='us-east-1'

# defining client, and setting resource name ec2
client = boto3.client('ec2',region_name=region)

# Lambda Function
def lambda_handler(event, context):
    
    # Creating empty lists for storing instance ids for Auto-Start and Auto-Stop tags
    
    start_instance_ids = []
    stop_instance_ids = []
    
    # Using describe_instances from AWS botob3 documentaion, store it in a variable
    response = client.describe_instances(
            # defining filters so that the variable will only include the instances that have specific tags
            Filters = [
                    {
                        'Name' : 'tag:tag',
                        "Values" : ['Auto-Start','Auto-Stop']
                    }
                ]
        )
        
    # extracting the instance ids from response recieved from aws
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            for tags in instance['Tags']:
                if tags['Value'] == 'Auto-Start':
                    start_instance_ids.append(instance['InstanceId'])
                elif tags['Value'] == 'Auto-Stop':
                    stop_instance_ids.append(instance['InstanceId'])
                    
    # printing the start and stop instances

    print(start_instance_ids)
    print(stop_instance_ids)
    
    # Using start_instances we will start the instances with tag 'Auto-Start'
    
    print("Starting Instances with tag:Auto-Start")
    client.start_instances(InstanceIds=start_instance_ids)
    print("start complete")
    
    # Using stop_instances we will stop the instances with tag 'Auto-Stop'

    print("Stopping Instances with tag:Auto-Stop")
    client.stop_instances(InstanceIds=stop_instance_ids)
    print("Stop complete")
    
    # returning a value once the function is done
    
    return {
        'result': "Task Completed"
    }
