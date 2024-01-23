from flask import Blueprint, request, render_template, jsonify, session, current_app, make_response
import flask
from itsdangerous import URLSafeTimedSerializer
import json
import urllib.request as urlRequest
import urllib.request
import urllib.parse as urlParse
import urllib.error as urlError


change_order_bp = Blueprint("change_order", __name__)

@change_order_bp.route("/api/add_to_batch", methods=['GET', 'POST'])
def add_to_batch():
    
    """
    You will need to figure out how to add in the token here

    headers = {'accept': '*/*',
               "Content-Type": "application/json",
               "Authorization: Bearer " <token>
               }
    
    """
    
    return "ok"

@change_order_bp.route("/api/submit_batch", methods=['GET', 'POST'])
def submit_batch():
    return "ok"


"""
      changeOrderBatchId : int
      taxYear:
      fipsCode: 
     """
@change_order_bp.route("/api/get_status", methods=['GET'])
def get_status():
     
    req = json.loads(request.data)
    change_order_batch_id = req['changeOrderBatchId']
    tax_year = req['taxYear']
    fips_code = req['fipsCode']

    # Verify user is authenticate
    session_id_from_cookie = request.cookies.get('session')
    print(f'session_id from cookie: {session_id_from_cookie}')
    session_id_from_server = session.sid
    print(f'session id from server {session_id_from_server}')
    # Compare the two IDs
    if session_id_from_cookie == session_id_from_server :
        url = 'https://testapi.latax.la.gov/api/Auth/v1/ChangeOrderGetStatus?param=value&param2=value&param3=value&param4=value'

        values = {"changeOrderBatchId": change_order_batch_id,
                  "taxYear": tax_year,
                  "fipsCode": fips_code
                }
        headers = {'accept': 'text/plain',
                   "Content-Type": "application/json"}#,
                   #"Authorization": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDYxMjQ1MDcsImlzcyI6Imh0dHBzOi8vdGVzdGFwaS5sYXRheC5sYS5nb3YvIiwiYXVkIjoidGVzdCJ9.kz8fdH5-fD03OOW2GCLipNFf-HRQVHS178_3Pd1tgPc'
                   #}
      
        creds = json.dumps(values).encode('utf-8')
        print('after creds')
        req = urllib.request.Request(url, headers=headers, data=creds, method='GET')
        print(f"req {req}")
        try:
            print('entering context manager')
            with urlRequest.urlopen(req) as response:
                print('after with, before body')
                body = response.read()
                print('inside with')
            resp = json.loads(body)
     
            print(f"resp: {resp}")
            # store in the session dictionary
            token = resp['token']
            flask.session["token"] = token
            flask.session['secretkey'] =  current_app.secret_key.encode('utf-8')
            flask.session['username'] = resp['userName']
            flask.session['expiration'] = resp['expiration']
            flask.session['roles'] = resp['roles']
            flask.session['userId'] = resp['userId']
                 
            print('before jsonify')
            return jsonify({
                'token': resp['token'],
                'expiration': resp['expiration'],
                'userName': resp['userName'],
                'userId': resp['userId'],
                'roles': resp['roles']
            })

          

        except urlError.URLError as e:
            message = e.reason
            error_code = e.errno
            return jsonify({'error': error_code,
                                'message': message})
    

    else:
        
        return jsonify({'error': 401,
                            'message': 'You are not logged in.'})
    


   
    
    return "ok"