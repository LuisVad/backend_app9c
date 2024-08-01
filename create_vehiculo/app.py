import json
import os
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

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
        'dueño': body['dueño'],  # Agregado
        'caballosDeFuerza': body['caballosDeFuerza']  # Agregado
    }

    try:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Vehículo creado exitosamente'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }