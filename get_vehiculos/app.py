import json
import os
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])


def decimal_to_float(d):
    if isinstance(d, Decimal):
        return float(d)
    raise TypeError("Type not serializable")


def lambda_handler(event, context):
    try:
        response = table.scan()
        items = response['Items']

        # Convert Decimal to float
        items_serializable = [{k: decimal_to_float(v) if isinstance(v, Decimal) else v for k, v in item.items()} for
                              item in items]

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Permite solicitudes desde cualquier origen
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE'
            },
            'body': json.dumps(items_serializable)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': 'Internal server error', 'details': str(e)})
        }
