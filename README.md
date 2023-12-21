Q2: Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

Objective: To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.

Task: Automate the deletion of files older than 30 days in a specific S3 bucket.

Instructions:

1. S3 Setup:

   - Navigate to the S3 dashboard and create a new bucket.

   - Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonS3FullAccess` policy to this role. (Note: For enhanced security in real-world scenarios, use more restrictive permissions.)

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 S3 client.
     2. List objects in the specified bucket.
     3. Delete objects older than 30 days.
     4. Print the names of deleted objects for logging purposes.

4. Manual Invocation:

   - After saving your function, manually trigger it.

   - Go to the S3 dashboard and confirm that only files newer than 30 days remain.
  
----------------------------------------------------------------------------------------------------------------------------------
Solution:

1. Checked and found that there are existing dummy buckets in S3 and they are older than 30 days
2. Made Sure that the objects in there are also older than 30 days
3. Navigated to IAM, created a role, and attached `AmazonS3FullAccess`
4. Created a Lambda Function with Python 3.x and attached the role that was created.
5. Wrote te code using boto3 module, and https://boto3.amazonaws.com/v1/documentation
6. Manually testes the function
7. The function is Deleting the objects older than 30 days and also priting the names of the objects
8. Attached Screenshots
9. Also the code is well documented with comments.
