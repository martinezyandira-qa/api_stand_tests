

import configuration
import requests

def post_new_user(body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body
    )
    return response


def get_users_table():
    response = requests.get(
        configuration.URL_SERVICE + configuration.USERS_TABLE_PATH
    )
    return response