import boto3
from datetime import datetime

s3 = boto3.client('s3')

response = s3.list_objects(Bucket='lokeshstaticwebsite')

for object in response['Contents']:
    print(object['Key'], object['LastModified'])

    key_list = []

    key_list.append(object['Key'])

    object_date = object['LastModified'].date()
    print(object_date)

    current_date = datetime.today().date()
    print(current_date)

    if current_date < object_date:
        print((object_date-current_date).days)
        age = int((object_date-current_date).days)
    else:
        print((current_date-object_date).days)
        age = int((current_date-object_date).days)
    
    if age > 30:
        print(f"Deleting object as {object['Key']} is aged more than 30 days")
        delete_response = s3.delete_object(
            Bucket='lokeshstaticwebsite',
            Key=key_list[0]
        )