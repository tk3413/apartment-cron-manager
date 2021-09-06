import json
import boto3


def lambda_handler(event, context):
    """
    turns ecs services on or off
    :param event (dict) example: {"service": "server", "status":"1"}
    :param context (None)
    :returns dict example: {"statusCode": 200, "body": 200}
    """
    client = boto3.client('ecs')
    print('recieved request to set ' + event['service'] +
          " to " + event['status'])

    response = client.update_service(
        cluster='apartment-app',
        service=event['service'],
        desiredCount=int(event['status'])
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response['service']['status'])
    }
