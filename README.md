Q4: Assignment 4: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

Objective: To enhance your AWS security posture by setting up a Lambda function that detects any S3 bucket without server-side encryption.

Task: Automate the detection of S3 buckets that don't have server-side encryption enabled.

Instructions:

1. S3 Setup:

   - Navigate to the S3 dashboard and create a few buckets. Ensure that a couple of them don't have server-side encryption enabled.

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonS3ReadOnlyAccess` policy to this role.

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 S3 client.
     2. List all S3 buckets.
     3. Detect buckets without server-side encryption.
     4. Print the names of unencrypted buckets for logging purposes.

4. Manual Invocation:

   - After saving your function, manually trigger it.

   - Review the Lambda logs to identify the buckets without server-side encryption.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Solution:

1. There were already buckets present in s3 section in aws, though created a few buckets
2. Navigated to IAM, created a role, and attached `AmazonS3ReadOnlyAccess` and also made sure that delete option is enabled for the role
3. Created a Lambda Function with Python 3.x and attached the role that was created.
4. Wrote the code using boto3 module, and https://boto3.amazonaws.com/v1/documentation
5. Manually tested the function
6. Attached Screenshots
7. Also the code is well documented with comments.
