import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

bucket_names=[]

for bucket in response['Buckets']:
    bucket_names.append(bucket['Name'])
    print(bucket['Name'])

# print(bucket_names)

non_encyrpted_bucket_names = []

for i in bucket_names:
    response_encryption = s3.get_bucket_encryption(
        Bucket=i
    )
    
    # print(response_encryption)

    try:
        rules = response_encryption['ServerSideEncryptionConfiguration']['Rules']
    except:
        print(f'Bucket {i} is not encrypted')
        non_encyrpted_bucket_names.append(i)
    else:
        print(f'Bucket {i} is encrypted')

print(non_encyrpted_bucket_names)

if len(non_encyrpted_bucket_names) == 0:
    print("There are no buckets without server-side encyrption")
else:
    for j in non_encyrpted_bucket_names:
        print(f'Deleting the bucket {j} as it is not server-side encrypted')
        response_delete_bucket = s3.delete_bucket(
            Bucket=j
        )