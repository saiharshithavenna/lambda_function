import json

def lambda_handler(event,context):
    personId = event['queryStringParameters']['PersonId']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "personId":personId + "from Lambda",
        }),
    }