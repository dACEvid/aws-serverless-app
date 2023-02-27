import boto3

VERIFIED_EMAIL = 'dpsukps@gmail.com'

ses = boto3.client('ses')

def lambda_handler(event, context):
    ses.send_email(
        Source=VERIFIED_EMAIL,
        Destination={
            'ToAddresses': [event['email']]
        },
        Message={
            'Subject': {'Data': 'This is an email reminder from your reminder service!'},
            'Body': {'Text': {'Data': event['message']}}
        }
    )
    return 'Success!'