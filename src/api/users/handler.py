import json
import jwt
from models.users import User


def login(event, context):
    request_body = event['body']
    response = {
        'header': {
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
        }
    }

    try:
        response['statusCode'] = 200
        response['body'] = User.__manager__.find_one_user(
            email=request_body['user']['email'],
            password=request_body['user']['password']
        )
        response['body']['token'] = jwt.encode(
            {
                'email': request_body['user']['email'],
                'logged_in': True,
            },
            key='key'
        )
    except KeyError:
        response['statusCode'] = 400
    except ValueError:
        response['statusCode'] = 400

    response['body'] = json.dumps(response['body'])
    return response


def register(event, context):
    request_body = event['body']
    response = {
        'header': {
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
        }
    }

    try:
        response['statusCode'] = 200
        response['body'] = User.__manager__.create_user(
            email=request_body['user']['email'],
            username=request_body['user']['username'],
            password=request_body['user']['password']
        )
        response['body']['token'] = jwt.encode(
            {
                'email': request_body['user']['email'],
                'logged_in': True,
            },
            key='key'
        )
    except (KeyError, ValueError):
        response['statusCode'] = 400

    response['body'] = json.dumps(response['body'])
    return response


def get_current_user(event, context):
    pass


def update_user(event, context):
    pass
