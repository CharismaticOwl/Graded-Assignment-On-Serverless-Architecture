# importing necessary modules - boto3 and datetime
import boto3
from datetime import datetime


# Lambda function
def lambda_handler(event, context):
    
    # boto3 command to store invoke client for s3
    client = boto3.client('s3')

    # using liste_objects function for s3 and string the response
    response = client.list_objects(Bucket='lokeshstaticwebsite')
    
    # as per docuemntation, the objects details are stored in Contents key
    # for every content we will execute the code
    for object in response['Contents']:

        # Printing the key of the object and also the last modified date for it
        print(object['Key'], object['LastModified'])

        # empty list to store the key
        key_list = []

        # appending the key name as string in the list
        key_list.append(object['Key'])

        # converting the datetime of the object and only extracting date, using the date() function
        object_date = object['LastModified'].date()
        print(object_date)

        # getting the current date time for today and only extracting date in it
        current_date = datetime.today().date()
        print(current_date)

        # with the help of days function, we can caluclate the difference between the dates, and stores the difference in a age variable
        if current_date < object_date:
            print((object_date-current_date).days)
            age = int((object_date-current_date).days)
        else:
            print((current_date-object_date).days)
            age = int((current_date-object_date).days)
    
        # if the age variable is greater than 30 days, we will delete the object
        if age > 30:

            # printing the obejct name before deleting it
            print(f"Deleting object as {object['Key']} is aged more than 30 days")

            # using delete_object to delete the object in the same bucket
            delete_response = client.delete_object(
                Bucket='lokeshstaticwebsite',
                Key=key_list[0]
            )
        
    # once the task is completed the function will throw below status code
    return {
        'statusCode': 'done'
    }
