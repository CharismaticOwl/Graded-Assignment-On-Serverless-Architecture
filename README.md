Q9: Assignment 9: Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend

Objective: Automatically analyze and categorize the sentiment of user reviews using Amazon Comprehend.

Task: Set up a Lambda function to receive user reviews, analyze their sentiment using Amazon Comprehend, and log the results.

Instructions:

1. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach policies that allow Lambda to use Amazon Comprehend.

2. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created previously.

   - Write the Boto3 Python script to:

     1. Extract the user review from an event.
     2. Use Amazon Comprehend to analyze the sentiment of the review.
     3. Log the sentiment result.

3. Testing:

   - Manually trigger the Lambda function with sample reviews.

   - Confirm the sentiment analysis results in the Lambda logs.
  
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Solution:

1. Created a role with `ComprehendFullAccess`
2. Created a new lambda function `satya_assignment_Q9`
3. Attached the role
4. Wrote code using comprehend and boto3,
5. Also created a test event with Text in it
6. Ouput the response and the sentiment scores
7. Manually tested the function
8. Attached Screenshots
9. Also the code is well documented with comments.
