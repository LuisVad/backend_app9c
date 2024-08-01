import json
import os
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    id = event['pathParameters']['id']
    body = json.loads(event['body'])
    update_expression = "SET marca = :marca, modelo = :modelo, autonomia = :autonomia, velocidadMaxima = :velocidadMaxima, dueño = :dueño, caballosDeFuerza = :caballosDeFuerza"
    expression_values = {
        ':marca': body['marca'],
        ':modelo': body['modelo'],
        ':autonomia': body['autonomia'],
        ':velocidadMaxima': body['velocidadMaxima'],
        ':dueño': body['dueño'],  # Agregado
        ':caballosDeFuerza': body['caballosDeFuerza']  # Agregado
    }

    try:
        table.update_item(
            Key={'id': id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Vehículo actualizado exitosamente'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
