Q7: Assignment 7: Monitor and Alert High AWS Billing Using AWS Lambda, Boto3, and SNS

Objective: Create an automated alerting mechanism for when your AWS billing exceeds a certain threshold.

Task: Set up a Lambda function to check your AWS billing amount daily, and if it exceeds a specified threshold, send an alert via SNS.

Instructions:

1. SNS Setup:

   - Navigate to the SNS dashboard and create a new topic.

   - Subscribe your email to this topic.

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach policies that allow reading CloudWatch metrics and sending SNS notifications.

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize boto3 clients for CloudWatch and SNS.
     2. Retrieve the AWS billing metric from CloudWatch.
     3. Compare the billing amount with a threshold (e.g., $50).
     4. If the billing exceeds the threshold, send an SNS notification.
     5. Print messages for logging purposes.

4. Event Source (Bonus):

   - Attach an event source, like Amazon CloudWatch Events, to trigger the Lambda function daily.

5. Testing:

   - Manually trigger the Lambda function or wait for the scheduled event.

   - If your billing is over the threshold, you should receive an email alert.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Solution:

1. Navigated to IAM, created a role, and attached allow reading CloudWatch metrics and sending SNS notifications.
2. Attached policies that allow reading CloudWatch metrics and sending SNS notifications.
3. Created a EvenBridge rule to run everyday at 10am - `cron(0 10 * * ? *)`
4. Created a SNS Topic, and subcribed my email for messages
5. Wrote a lambda function using `CostExpolrer` and also `SNS`
6. Tested manually triggering the lambda function when it is found that threshold is already breached
7. Attached Screenshots
8. Also the code is well documented with comments.
