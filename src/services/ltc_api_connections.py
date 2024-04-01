from flask import jsonify, current_app
import json
import os
import urllib.request as urlRequest
import urllib.request
import urllib.parse as urlParse
import urllib.error as urlError

import services.helpers as util


class LTCApiConnections:
    def __init__(self, logger):
        self.logger = logger

    def logout(self, username: str, token: str) -> object:
        url = os.environ.get('LTC_API_URL_TEST')
        # url = os.environ.get('LTC_API_URL_PROD')

        paths = [url, "Users/v1/logout"]
        url = "".join(paths)

        values = {"username": f"{username}"
                  }
        headers = {"Accept": "text/plain",
                   "Authorization": f"Bearer {token}"
                   }

        creds = json.dumps(values).encode('utf-8')
        req = urllib.request.Request(
            url, headers=headers, data=creds, method='POST')

        with urlRequest.urlopen(req) as response:
            body = response.read()

        try:
            return json.loads(body)
        except:
            return util.create_json_object(message='logged out')

    def login(self, username: str, password: str) -> object:
        # url = current_app.config["LTC_API_URL_PROD"]
        url = current_app.config["LTC_API_URL_TEST"]
        paths = [url, "Auth/v1/authenticate?param=value&param2=value"]
        url = "".join(paths)
        values = {"username": username,
                  "password": password
                  }
        headers = {'accept': '*/*',
                   "Content-Type": "application/json"}
        creds = json.dumps(values).encode('utf-8')
        req = urllib.request.Request(
            url, headers=headers, data=creds, method='POST')

        try:

            with urlRequest.urlopen(req) as response:
                body = response.read()

            return json.loads(body)
        except urlError.URLError as e:
            return json.loads(util.create_json_object(error=1, message=e.reason))
