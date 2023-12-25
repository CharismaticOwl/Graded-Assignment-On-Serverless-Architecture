Q8: Assignment 8: DynamoDB Item Change Alert Using AWS Lambda, Boto3, and SNS

Objective: Automate the process to receive an alert whenever an item in a DynamoDB table gets updated.

Task: Set up a Lambda function that gets triggered when an item in a DynamoDB table is updated and sends an alert via SNS.

Instructions:

1. DynamoDB Setup:

   - Navigate to the DynamoDB dashboard and create a table.

   - Add a few items to the table.

2. SNS Setup:

   - Navigate to the SNS dashboard and create a new topic.

   - Subscribe your email to this topic.

3. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach policies that allow Lambda to read DynamoDB Streams and send SNS notifications.

4. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Extract the modified DynamoDB item from the event.
     2. Send an SNS notification detailing the change.
     3. Log messages for tracking.

5. DynamoDB Stream:

   - Enable DynamoDB Streams on your table and set the view type to "New and old images".

   - Attach the Lambda function to the DynamoDB Stream.

6. Testing:

   - Update an item in your DynamoDB table.

   - Confirm that you receive an SNS alert detailing the change.
  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Solution:

1. Created a DynamoDB table
2. Navigated to Export and Streams
3. Turned on DynamoDB Streams, with view type `New and old images`
4. Created a Trigger here itself, with adding the Lambda function that was created - `satya_assignment_Q8`
5. Added a Destination as the SNS Topic, which was used in the previous assignment, it has email subcription
6. Tested by adding items to dynamodb manually, and the sns topic did publish, and also the cloud logs show the steps that were taken
7. Attached Screenshots
8. Also the code is well documented with comments.
