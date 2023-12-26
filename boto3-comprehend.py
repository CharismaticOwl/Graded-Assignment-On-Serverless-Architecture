import boto3

comprehend = boto3.client('comprehend')

response_sentiment = comprehend.detect_sentiment(
    Text='Finance minister Niramala Sitharaman to meet heads of PSBs on Sat; review progress of implementation of govt schemes',
    LanguageCode='en'
)

print(response_sentiment)