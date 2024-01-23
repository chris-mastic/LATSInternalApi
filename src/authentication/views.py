from flask import Blueprint, request, render_template, jsonify, session, current_app, make_response
import flask
from itsdangerous import URLSafeTimedSerializer
import json
import urllib.request as urlRequest
import urllib.request
import urllib.parse as urlParse
import urllib.error as urlError
import pickle
import base64

authentication_bp = Blueprint("authentication", __name__)



@authentication_bp.route("/", methods=['GET', 'POST'])
def index():
    return render_template("authentication/index.html")

"""
    TODO: Add an Authentication endpoint to verify identity of user/application
        username
        password

        returns authentication token or session identifier
        Include this in header of subsequent API requests.

"""

@authentication_bp.route("/api/logout", methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'logged out'
    })

 
@authentication_bp.route("/api/login", methods=['POST'])
def login() -> object:
    
    """
        Initiate a session for authenticated user/application

        Once user is authenticated, this endpoint should return
        a session identifier that can be used to acess protected
        resources. Store it as a cookie or in header of 
        subsequent API requests.
    """

    req = json.loads(request.data)
    username = req['username']
    password = req['password']

    print(f"username {username}")
    print(f"password {password}")
    
    # Check if user has an active session
    # Get the session ID from the cookie
    session_id_from_cookie = request.cookies.get('session')
    # Get the session ID from the server
    print(f"session.sid is {session.sid}")
    session_id_from_server = session.sid
    # Compare the two IDs
    if session_id_from_cookie == session_id_from_server : 
        # return the values already stored in the session dictionary from previous login
        print("in first if")
        return jsonify ({
                'token': session.get('token'),
                'expiration': session.get('expiration'),
                'userName': session.get("username"),
                'userId': session.get('userId'),
                'roles': session.get('roles')
            })

    # If user does not have an active session
    if session_id_from_cookie != session_id_from_server or session_id_from_cookie is None:
        print('in second if')
        # Get token from the LA Tax Service API and build JSON object to return
        # to user and store in session dictionary
        #url = 'http://127.0.0.1:8300/api/Users/v1/login'
        #url = 'https://ltc-dev-server.vercel.app/api/Users/v1/login'
        #url = 'https://py-http-server.vercel.app/login'
        #url = 'https://testapi.latax.la.gov/api/Auth/v1/authenticate'
        url = 'https://testapi.latax.la.gov/api/Auth/v1/authenticate?param=value&param2=value'
        #url = 'https://testserver-chrism.pythonanywhere.com/api/Users/v1/login'
        values = {"username": username,
                    "password": password
                }
        headers = {'accept': '*/*',
                   "Content-Type": "application/json"}
        
        response = make_response(authenticate_user(url,values, headers))
       
        return response


def authenticate_user(url, values, headers) -> object:

    # make a request to authentication endpoint
    #url = "https://testapi.latax.la.gov/api/login"
    #user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    print("in authenticate_user")     

    #creds = urlParse.urlencode(values)
    #creds = creds.encode('ascii')
    creds = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(url, headers=headers, data=creds, method='POST')
    #req = urlRequest.Request(url, creds, headers)
    try:
        with urlRequest.urlopen(req) as response:
            body = response.read()
           
        resp = json.loads(body)
       
        # store in the session dictionary
        token = resp['token']
        flask.session["token"] = token
        flask.session['secretkey'] =  current_app.secret_key.encode('utf-8')
        flask.session['username'] = resp['userName']
        flask.session['expiration'] = resp['expiration']
        flask.session['roles'] = resp['roles']
        flask.session['userId'] = resp['userId']
       
        # TODO figure out how to use the SECRET_KEY and salt it with the session id
        #need to use this value to salt the secret key and return to user
        session_id = create_salted_key(flask.session["token"])
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
   
"""
    NOT CURRENTLY IMPLEMENTED
"""
def create_salted_key(api_token):
    """
        This code works. It salts the secret_key with the session id and decodes it
    """
    print(f"current_app.secret_key {current_app.secret_key}")
    # print(f"authtoken from api {authtoken}")
    s = URLSafeTimedSerializer(current_app.secret_key,api_token) #,authtoken)
    signed = s.dumps(session.sid)
    print(f"signe {signed}")

    print(f"decoded {s.loads(signed)}")
    print(f"session id {session.sid}")

    return signed
   

@authentication_bp.route("/api/reset_password", methods=['GET', 'POST'])
def reset_password():
    "username, oldpassword,newpassword"
    return "ok"

@authentication_bp.route("/api/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    return "ok"