# importing necessary modules - boto3
import json
import boto3

# Lambda function
def lambda_handler(event, context):
    
    # Invoking comprehend to call aws comprehend service
    comprehend = boto3.client('comprehend')
    
    # Using detect_sentiment module to send the user review and get a response
    response_comprehend = comprehend.detect_sentiment(
        Text=event['Text'],
        LanguageCode='en'
        )
    
    # Printing the response to get the results
    return response_comprehend


'''
{
  "Text": "Finance minister Niramala Sitharaman to meet heads of PSBs on Sat; review progress of implementation of govt schemes"
}
'''