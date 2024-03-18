import sys
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import cross_origin

# additional_paths = [
#         'C:/Users/christopher.mazza/source/repos/LATSInternalApi/src/services/',
#         'C:/Users/christopher.mazza/source/repos/LATSInternalApi/src/db/'
#         ]
# sys.path.extend(additional_paths)

import helpers as helper
from services.ltc_api_connections import LTCApiConnections

from flask import Blueprint, request, render_template, jsonify, session, current_app

from flask import Blueprint, redirect, request, render_template, jsonify, session, current_app, make_response, url_for

import flask
from itsdangerous import URLSafeTimedSerializer
import json
import logging
import oracle_db_connection as odb
from pymongo import MongoClient
import warnings
import functools
from db.mongo_db import user


logging.basicConfig(level=logging.DEBUG, filename=__name__, filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")


authentication_bp = Blueprint(
    "authentication", __name__, template_folder='authentication/templates')


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)
    return new_func

""" Following two functions are intended to handle CORS related issuses
"""

@authentication_bp.route('/api/login', methods=['OPTIONS'])
def handle_preflight():
    """ This function receives the browser's preflight request (An HTTP OPTIONS request)
        The request should include headers (Orign, Access-Control-Request-Method and 
        Access-Control-Request-Headers). This will cause the server to respond with
        appropriate CORS headers indicating whether the actual request is allowed
        from the specific orign. The server includes CORS headers in its response (prefilight
        or acutal). The acutal headers are set in __init__.py.
    """
    return '', 204  # No content, just acknowledge the preflight request


@authentication_bp.after_request
def set_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response


@authentication_bp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if "logout" in request.form: logout()
        # Get the username and password from the form
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"username {username}")
        # Validate the credentials (you can replace this with your own validation logic)
        session_id_from_cookie = request.cookies.get('session')
        session_id_from_server = session.sid

        if helper.is_valid_session(session_id_from_cookie, session_id_from_server):
            print("In if helper.is_valid_seesion")
            # return the values already stored in the session dictionary from previous login
            print(f"session_id_from_cookie {session_id_from_cookie}")
            print(f"session_id_from_server {session_id_from_server}")
            print(f"token {session.get('token')}")
            print(f"userName {session.get('username')}")
            print(f"userId {session.get('userId')}")
            return jsonify({
                'token': session.get('token'),
                'expiration': session.get('expiration'),
                'userName': session.get("username"),
                'userId': session.get('userId'),
                'roles': session.get('roles')
            })
        else:
            # Create a new session
            print("IN else")
            ltc_api = LTCApiConnections(logging)
            response = ltc_api.login(username, password)
            print(f"resonpnse {response}")
            set_flask_session_values(response)

            if flask.session['token'] is None:
                logging.error(f'{username} unable to log in to LTC site')
                del ltc_api
                return helper.clear_session(response)

            del ltc_api
            return create_json_object()


    return render_template('authentication/login.html')


@authentication_bp.route("/api/logout", methods=['POST'])
def logout():

    ltc_api = LTCApiConnections(logging)
    req = json.loads(request.data)
    token = req['token']
    username = req['username']

    with current_app.app_context():
        client = MongoClient(current_app.config['MONGO_URI'])
        mongodb = client[current_app.config['MONGO_DBNAME']]
        col = mongodb["user_session"]
        if user.active_session(col, token):
            resp = ltc_api.logout(username, token)
            user.remove_user_session_from_mongodb(col, token)
            del ltc_api
            return create_json_object(message="Logged out")

        else:
            return create_json_object(message="Not logged in")


@authentication_bp.route("/api/login", methods=['POST'])
@cross_origin()
def login() -> object:
    """
        Initiate a session for authenticated user/application

        Once user is authenticated, this endpoint should return
        a session identifier and LTC token that can be used to access protected
        resources. Store it as a cookie or in header of 
        subsequent API requests.
    """
    req = json.loads(request.data)
    username = req['username']
    password = req['password']
    token = req['token']

    with current_app.app_context():

        client = MongoClient(current_app.config['MONGO_URI'])
        mongodb = client[current_app.config['MONGO_DBNAME']]
        col = mongodb["user_session"]

        # Check if user has an active session
        is_valid_session = user.active_session(col, token)

        # User has an active session
        if is_valid_session:
            logging.info("user tried to log in again")
            # return the values already stored in the session dictionary from previous login
            user_session_info = user.get_user_session_data(col, token)
            if 'token' in user_session_info:
                return create_json_object(token=user_session_info['token'], expiration=user_session_info['expiration'], username=user_session_info['username'])
            else:
                # returns an empty dictionary
                user_session_info['message'] = 'Failed to fetch user session'
                return user_session_info

        # No active session, try to create one
        else:
            # Connect to LTC API
            ltc_api = LTCApiConnections(logging)
            response = ltc_api.login(username, password)
            # Log bad response
            if type(response) is not dict and 'token' not in response.json:
                logging.error(f'{username} unable to log in to LTC site')
                del ltc_api
                return create_json_object(message="Failed to receive response from LTC")

            # Valid response, write to database
            user.insert_user_session_into_mongodb(
                col,  response['token'], username, response['expiration'])
            del ltc_api

            return create_json_object(token=response['token'], expiration=response['expiration'], username=username)


@deprecated
def set_flask_session_values(response: object):
    # store in the session dictionary
    try:
        token = response['token']
        flask.session['token'] = token
        flask.session['secretkey'] = current_app.secret_key.encode('utf-8')
        flask.session['username'] = response['userName']
        flask.session['expiration'] = response['expiration']
        flask.session['roles'] = response['roles']
        flask.session['userId'] = response['userId']

    except:
        flask.session["token"] = None


def create_json_object(**kwargs) -> object:
    return json.dumps({key: value for key, value in kwargs.items()})


@deprecated
def create_salted_key(api_token):
    """
        This code works. It salts the secret_key with the session id and decodes it
    """
    print(f"current_app.secret_key {current_app.secret_key}")
    # print(f"authtoken from api {authtoken}")
    s = URLSafeTimedSerializer(
        current_app.secret_key, api_token)  # ,authtoken)
    signed = s.dumps(session.sid)
    print(f"signe {signed}")

    print(f"decoded {s.loads(signed)}")
    print(f"session id {session.sid}")
    return signed


@authentication_bp.route("/api/reset_password", methods=['GET', 'POST'])
def reset_password():
    return create_json_object(message="password reset")
    

@authentication_bp.route("/api/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    return create_json_object(message="check email for password reset link")
    
