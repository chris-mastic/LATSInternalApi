import json

from flask import jsonify
import db.oracle_db_connection as odb
import os
import pandas as pd
import urllib.request as urlRequest
import urllib.request
import urllib.parse as urlParse
import urllib.error as urlError


class ApiSettings:
    def __init_(self): pass

    def logout(self, username, token):
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
            return jsonify({
                'message': 'logged out'
            })

    def login(self, username: str, password: str):
        print("in login of ApiSettings....")
        # url = os.environ.get('LTC_API_URL_PROD')
        url = os.environ.get('LTC_API_URL_TEST')

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

        # TODO: Replace with the new singleton class
        try: 
            with urlRequest.urlopen(req) as response:
                body = response.read()

            return json.loads(body)
        except urlError.URLError as e:
            message = "There is a problem connecting to the LTC API"
            error_code = e.errno
            return jsonify({'error': error_code,
                        'message': message})
         
       

    # TODO: Figure out how to destroy this class if invalid session or user logs out.
