import boto3
from datetime import date

ec2 = boto3.client('ec2')

response = ec2.describe_instances(
    InstanceIds=["i-06071f0984a121b4e"]
)

response_tags = ec2.create_tags(
    Resources=['i-06071f0984a121b4e'],
    Tags=[
        {
            'Key':'newTag',
            'Value':'Tag created by Lambda'
        },
        {
            'Key':'Date',
            'Value': str(date.today())
        }
    ]
)