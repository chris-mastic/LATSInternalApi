import json
import db.oracle_db_connection as odb
import os
import pandas as pd
import urllib.request as urlRequest
import urllib.request
import urllib.parse as urlParse
import urllib.error as urlError

class ApiSettings:
    def __init_(self): pass

    def login(self, username: str, password: str):
        print("in login of ApiSettings....")
        url = os.environ.get('LTC_API_URL_PROD')

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
        with urlRequest.urlopen(req) as response:
            body = response.read()
        
        return json.loads(body)
    

    #  # TODO Add this exception handling in

      

    # except urlError.URLError as e:
    #     message = "There is a problem connecting to the LTC API"
    #     error_code = e.errno
    #     return jsonify({'error': error_code,
    #                     'message': message})
