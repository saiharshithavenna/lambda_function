import json

def lambda_handler(event,context):
    body = json.loads(event['body'])
    name = body.get('name','Guest')

    greeting = f"Hello,{name}"

    response = {
        "statuscode": 200,
        "body":json.dumps({"message":greeting})
    }

    return response