import boto3
import json
import os
import decimal

SFN_ARN = 'ARN_of_Step_Function'

sfn = boto3.client('stepfunctions')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    data['waitSeconds'] = int(data['waitSeconds'])
    
    # Validation Checks
    checks = []
    checks.append('waitSeconds' in data)
    checks.append(type(data['waitSeconds']) == int)
    checks.append('preference' in data)
    checks.append('message' in data)
    if data.get('preference') == 'sms':
        checks.append('phone' in data)
    if data.get('preference') == 'email':
        checks.append('email' in data)

    # Check if there are errors in validation checks
    if False in checks:
        response = {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin":"*"},
            "body": json.dumps(
                {
                    "Status": "Success", 
                    "Reason": "Validation Failed"
                },
                cls=DecimalEncoder
            )
        }
    # If none, run the state machine
    else: 
        sfn.start_execution(
            stateMachineArn=SFN_ARN,
            input=json.dumps(data, cls=DecimalEncoder)
        )
        response = {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin":"*"},
            "body": json.dumps(
                {"Status": "Success"},
                cls=DecimalEncoder
            )
        }
    return response

# Workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)

