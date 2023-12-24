# importing necessary modules - boto3 and datetime
import json
import boto3
from datetime import date

# Lambda function
def lambda_handler(event, context):
    
    # Invoke costexplorer using boto3 client module
    ce = boto3.client('ce')
    
    # getting todays date, date when the lambda function is triggered
    today_date = date.today()
    
    # converting it to string
    str_today = str(today_date)
    
    # getting date for 1st of current month
    first_of_current_month = today_date.replace(day=1)
    
    # converting it to a string
    str_first_of_current_month = str(first_of_current_month)
    
    # Calling get_cost_and_usage to store the response
    response_ce = ce.get_cost_and_usage(
            TimePeriod={
                'Start': str_first_of_current_month,
                'End': str_today
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost']
        )
    
    # retreiving current months bill and storing it in a variable
    bill = response_ce['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    
    # Using threshold as $50.00, and comparing the current bill
    if float(bill) > 50.00:
        
        # If the bill exceeds then trigger a SNS topic, that already setup
        sns = boto3.client('sns')
        
        # a short message stored 
        message = 'Dude your bill exceeds the Threshold, you better watchout. Current Bill: ' + bill
        
        # invoking sns publich, so that a message can be puvlished
        response_sns = sns.publish(
            
                # arn value for the SNS topic
                TopicArn='arn:aws:sns:us-east-1:295397358094:sns_for_cost_threshold',
                Message= message
            )
    
    # once the task is completed the function will throw below status code
    return {
        'statusCode': "Done"
    }
