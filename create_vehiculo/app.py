import json
import os
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    body = json.loads(event['body'])
    item = {
        'id': body['id'],
        'marca': body['marca'],
        'modelo': body['modelo'],
        'autonomia': body['autonomia'],
        'velocidadMaxima': body['velocidadMaxima'],
        'dueño': body['dueño'],
        'caballosDeFuerza': body['caballosDeFuerza']
    }

    try:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Permite solicitudes desde cualquier origen
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE'
            },
            'body': json.dumps({'message': 'Vehículo creado exitosamente'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': str(e)})
        }
