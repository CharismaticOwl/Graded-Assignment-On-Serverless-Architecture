import boto3
from datetime import date

ce = boto3.client('ce')

today = date.today()

str_today = str(today)

first_of_current_month = today.replace(day=1)

str_start_date = str(first_of_current_month)


response_ce = ce.get_cost_and_usage(
    TimePeriod={
        'Start': str_start_date,
        'End': str_today
    },
    Granularity='MONTHLY',
    Metrics=['UnblendedCost']
)

current_cost = response_ce['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']

message_sns = 'Dude your bill exceeds the Threshold, you better watchout. Current Bill: '+current_cost

if float(current_cost) > 50.00:
    sns = boto3.client('sns')

    response_sns = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:295397358094:sns_for_cost_threshold',
        Message=message_sns
    )

