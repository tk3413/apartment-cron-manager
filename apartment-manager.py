import json
import boto3

client = boto3.client('ecs')

def lambda_handler(event, context):
    print('recieved request to set ' + event['service'] + " to " + event['status'])
    
    response = client.update_service(
        cluster      = 'apartment-app',
        service      = event['service'],
        desiredCount = int(event['status'])
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response['service']['status'])
    }