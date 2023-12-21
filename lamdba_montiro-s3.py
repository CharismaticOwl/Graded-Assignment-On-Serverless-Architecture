# importing modules - boto3 to access AWS resources using Python
import json
import boto3

# Lambda Function
def lambda_handler(event, context):
    
    # defining client, and setting resource name 's3'
    s3 = boto3.client('s3')
    
    # Using list_buckets in boto3 class to geta response from aws
    response = s3.list_buckets()

    # instanciating a empt list to store the bucket names
    bucket_names = []
    
    # loop to access data from response json data
    for i in response['Buckets']:
        
        # Storing the bucket names in our list
        bucket_names.append(i['Name'])
        
        # printing bucket names to the console
        print(bucket_names)

    # instanciating a empt list to store the bucket names without any encryption
    non_encrypted_bucket_names = []
    
    # loop to access each bucket name
    for j in bucket_names:
        
        # Using get_bucket_encryption to get the encrytion details of each bucket and storing the response
        response_encryption = s3.get_bucket_encryption(
                Bucket=j
            )
        
        # try except block to check if the bucket has rules defined for type of encryption
        try:
            rules = response_encryption['ServerSideEncryptionConfiguration']['Rules']
        except:
            
            # If exception raised because no rules found, then print the name of the bucket and append to non_encrypted_bucket_names list
            print(f'Bucket {j} is not encrypted')
            non_encrypted_bucket_names.append(j)
        else:
            
            # If no exception then simply print that the bucket is encrypted
            print(f'Bucket {j} is encrypted')
            
    # Print the bucket names found to be non-encrypted
    print(non_encrypted_bucket_names)
    
    # If none are found then simply print the fact there are no there are no buckets without server-side encryption
    if len(non_encrypted_bucket_names) == 0:
        print("There are no buckets without server-side encryption")
    else:
        # for loop to get each bucket name which are non-encrypted
        for k in non_encrypted_bucket_names:
            print("Deleting the bucket {k} as it is not server-side encrypted")
            
            # Using delete_bucket to delete non-encrypted bucket
            response_delete_bucket = s3.delete_bucket(
                    Bucket=k
                )
    # returning a value once the function is done
    return {
        'statusCode': 'Done'
    }
