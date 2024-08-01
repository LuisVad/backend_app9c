import json
import pytest
from hello_world import app as hello_world_app
from create_vehiculo import app as create_vehiculo_app

@pytest.fixture()
def apigw_event():
    """Generates API GW Event with multiple test records for create_vehiculo"""
    return {
        "body": json.dumps([
            {"id": "1", "marca": "Toyota", "modelo": "Corolla", "autonomia": 500, "velocidadMaxima": 180, "dueño": "Alice", "caballosDeFuerza": 150},
            {"id": "2", "marca": "Honda", "modelo": "Civic", "autonomia": 600, "velocidadMaxima": 200, "dueño": "Bob", "caballosDeFuerza": 140},
            {"id": "3", "marca": "Ford", "modelo": "Focus", "autonomia": 450, "velocidadMaxima": 170, "dueño": "Charlie", "caballosDeFuerza": 160},
            {"id": "4", "marca": "Chevrolet", "modelo": "Cruze", "autonomia": 550, "velocidadMaxima": 190, "dueño": "David", "caballosDeFuerza": 155},
            {"id": "5", "marca": "Hyundai", "modelo": "Elantra", "autonomia": 580, "velocidadMaxima": 210, "dueño": "Eve", "caballosDeFuerza": 170},
            {"id": "6", "marca": "Mazda", "modelo": "3", "autonomia": 500, "velocidadMaxima": 180, "dueño": "Frank", "caballosDeFuerza": 145}
        ]),
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }

def test_hello_world_handler(apigw_event, mocker):
    ret = hello_world_app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])
    status_code = 200
    assert ret["statusCode"] == status_code
    assert "message" in ret["body"]
    assert data["message"] == "hello world"

def test_create_vehiculo_handler(apigw_event, mocker):
    # Modifica el apigw_event para el caso de prueba de create_vehiculo
    create_vehiculo_event = apigw_event.copy()
    create_vehiculo_event["body"] = json.dumps([
        {"id": "1", "marca": "Toyota", "modelo": "Corolla", "autonomia": 500, "velocidadMaxima": 180, "dueño": "Alice", "caballosDeFuerza": 150},
        {"id": "2", "marca": "Honda", "modelo": "Civic", "autonomia": 600, "velocidadMaxima": 200, "dueño": "Bob", "caballosDeFuerza": 140},
        {"id": "3", "marca": "Ford", "modelo": "Focus", "autonomia": 450, "velocidadMaxima": 170, "dueño": "Charlie", "caballosDeFuerza": 160},
        {"id": "4", "marca": "Chevrolet", "modelo": "Cruze", "autonomia": 550, "velocidadMaxima": 190, "dueño": "David", "caballosDeFuerza": 155},
        {"id": "5", "marca": "Hyundai", "modelo": "Elantra", "autonomia": 580, "velocidadMaxima": 210, "dueño": "Eve", "caballosDeFuerza": 170},
        {"id": "6", "marca": "Mazda", "modelo": "3", "autonomia": 500, "velocidadMaxima": 180, "dueño": "Frank", "caballosDeFuerza": 145}
    ])

    ret = create_vehiculo_app.lambda_handler(create_vehiculo_event, "")
    data = json.loads(ret["body"])
    status_code = 200
    assert ret["statusCode"] == status_code
    assert isinstance(data, list)  # Asegúrate de que los datos devueltos sean una lista
    assert len(data) == 6  # Verifica que haya 6 registros
    for item in data:
        assert "id" in item
        assert "marca" in item
        assert "modelo" in item
        assert "autonomia" in item
        assert "velocidadMaxima" in item
        assert "dueño" in item
        assert "caballosDeFuerza" in item
