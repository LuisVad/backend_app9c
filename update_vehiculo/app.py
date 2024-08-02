import json
import os
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    id = event['pathParameters']['id']
    body = json.loads(event['body'])
    update_expression = """
        SET marca = :marca,
            modelo = :modelo,
            autonomia = :autonomia,
            velocidadMaxima = :velocidadMaxima,
            dueno = :dueno,
            caballosDeFuerza = :caballosDeFuerza
    """
    expression_values = {
        ':marca': body['marca'],
        ':modelo': body['modelo'],
        ':autonomia': body['autonomia'],
        ':velocidadMaxima': body['velocidadMaxima'],
        ':dueno': body['dueño'],  # Cambiado a 'dueno'
        ':caballosDeFuerza': body['caballosDeFuerza']
    }

    try:
        table.update_item(
            Key={'id': id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values
        )
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Permite solicitudes desde cualquier origen
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE'
            },
            'body': json.dumps({'message': 'Vehículo actualizado exitosamente'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': 'Error updating item', 'details': str(e)})
        }
