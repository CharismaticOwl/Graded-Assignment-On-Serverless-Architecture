# importing necessary modules - boto3 and datetime
import json
import boto3
from datetime import date

# Lambda function
def lambda_handler(event, context):
    
    # Invoking ec2 using the boto3 client module
    ec2=boto3.client('ec2')
    
    # empty list to store the instance ids
    instance_ids=[]
    
    # extracting the instance id from event
    instance_ids.append(event['detail']['instance-id'])
    
    # printing the resource that has triggered the lambda
    print(f"Resource that has started to run: {event['detail']['instance-id']}")
    
    # Using boto3 create_tags to add the new tags
    response_tags = ec2.create_tags(
    Resources=instance_ids,
    Tags=[
        {
            'Key':'newTag',
            'Value':'Tag created by Lambda'
        },
        {
            'Key':'Date',
            'Value':str(date.today())
        }
    ]
    )

    # once the task is completed the function will throw below status code
    return {
        'statusCode': 'New tag is added!'
    }
