# importing necessary modules - boto3 and datetime
import json
import boto3
from datetime import date

# Lambda function
def lambda_handler(event, context):

    # Invoking boto3 client to use s3 service
    s3 = boto3.client('s3')
    
    # pre-defined bucket name to be checked stored in a variable
    bucket_name = 'revanth.k'
    
    # requesting for response for each object in the bucket using list_objects and passsing bucket name in the API call
    response_s3 = s3.list_objects(
            Bucket=bucket_name
        )
        
    # for each content we can loop to get last modified date and compare with current date to execute the task
    for content in response_s3['Contents']:
        
        # Last Modified date is extracted and stored in a variable
        last_modified_date = content['LastModified'].date()
        
        # current date extracted and stored in a variable
        current_date = date.today()
        
        # calculating the difference and storing in a variable
        diff = (current_date - last_modified_date).days
        
        # defining a copy source with bucket name and key in it, so that the old object can be copied as new object and pass extra arguments
        copy_source = {
            'Bucket':bucket_name,
            'Key':content['Key']
        }
        
        # if difference is more than 60 days, lets execute the storage class change
        if diff > 60:
            
            # s3 copy function to copy the same object to itself and pass extra arguments
            s3.copy(
                    copy_source,bucket_name,content['Key'],
                    ExtraArgs={
                        'StorageClass': 'GLACIER',
                        'MetadataDirective': 'COPY'
                    }
            )
            
            # Printing the message to console for logging purpose
            print(f"{content['Key']} - This object from bucket - {bucket_name} is being moved to Glacier storage class, as it was last modified more than 60 days ago!!")
            
        else:
            print("All objects last modified age is less than 60 days")
        
    return {
        'statusCode': 'Task completed without an error'
    }
