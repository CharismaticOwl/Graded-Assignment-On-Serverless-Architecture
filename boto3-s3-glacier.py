import boto3
from datetime import date

s3 = boto3.client('s3')

bucket_name='akhil16'

response_s3 = s3.list_objects(
    Bucket=bucket_name
)

for content in response_s3['Contents']:

    Last_Modified_date = content['LastModified'].date()

    Current_date = date.today()

    diff = (Current_date-Last_Modified_date).days

    copy_source={
        'Bucket':bucket_name,
        'Key':content['Key']
    }

    if diff > 60:

        s3.copy(
            copy_source,bucket_name,content['Key'],
            ExtraArgs = {
                'StorageClass': 'GLACIER',
                'MetadataDirective': 'COPY'
            }
        )
        print(f"{content['Key']} - object from bucket {bucket_name} has been moved to Glacier storage class, as it was not modified since 60 days")