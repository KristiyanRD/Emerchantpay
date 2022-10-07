import requests
import unittest
from requests.auth import HTTPBasicAuth
from common.file_reader import *

credentials = FileReader.yaml_reader('../config/codemonsters_credentials.yaml')


class BasePage:

    @staticmethod
    def api_requests(json_data, request_type='GET', url=None, auth_user=None, auth_password=None):
        if auth_user is None and auth_password is None:
            auth = HTTPBasicAuth(credentials['login'], credentials['password'])
        else:
            auth = HTTPBasicAuth(auth_user, auth_password)

        if url is None:
            url = 'http://localhost:3001/payment_transactions/'

        response = requests.request(method=request_type, url=url, auth=auth, json=json_data)
        print(f"\nSTATUS CODE: {response.status_code}")
        return response
