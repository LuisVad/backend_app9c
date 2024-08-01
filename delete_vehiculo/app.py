import json
import os
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    id = event['pathParameters']['id']
    try:
        # Opción: en lugar de eliminar, podrías actualizar el estado a 'inactivo'
        table.delete_item(Key={'id': id})
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Vehículo eliminado exitosamente'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
