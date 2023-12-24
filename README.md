Q6: Assignment 6: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

Objective: Learn to automate the tagging of EC2 instances as soon as they are launched, ensuring better resource tracking and management.

Task: Automatically tag any newly launched EC2 instance with the current date and a custom tag.

Instructions:

1. EC2 Setup:

   - Ensure you have the capability to launch EC2 instances.

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonEC2FullAccess` policy to this role.

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 EC2 client.
     2. Retrieve the instance ID from the event.
     3. Tag the new instance with the current date and another tag of your choice.
     4. Print a confirmation message for logging purposes.

4. CloudWatch Events:

   - Set up a CloudWatch Event Rule to trigger the EC2 instance launch event.

   - Attach the Lambda function as the target.

5. Testing:

   - Launch a new EC2 instance.

   - After a short delay, confirm that the instance is automatically tagged as specified.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Solution:

1. Navigated to IAM, created a role, and attached AmazonEc2FullAccess
2. Created a Lambda function satya_assignment_Q6
3. Created a trigger using cloud watch or event bridge
4. The trigger is set for an event of state change to running
5. Using the event retrieved the instance id in lambda and created tags to it, it adds a tag, and a date tag
6. Tested using ec2 instance, manually launching or chaging state to running
7. Attached Screenshots
8. Also the code is well documented with comments.
