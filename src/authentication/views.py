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
import flask
from itsdangerous import URLSafeTimedSerializer
import json
import logging
import oracle_db_connection as odb
from pymongo import MongoClient
import warnings
import functools


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


@authentication_bp.route("/", methods=['GET', 'POST'])
def index():
    return render_template('authentication/index.html')


@authentication_bp.route("/api/logout", methods=['POST'])
def logout():

    ltc_api = LTCApiConnections(logging)
    req = json.loads(request.data)
    token = req['token']

    with current_app.app_context():
        client = MongoClient(current_app.config['MONGO_URI'])
        mongodb = client[current_app.config['MONGO_DBNAME']]
        col = mongodb["user_session"]
        if active_session(col, token):
            remove_user_session_from_mongodb(col, token)
            del ltc_api
            return create_json_object(message="Logged out")

        else:
            return create_json_object(message="Not logged in")


@authentication_bp.route('/api/login', methods=['OPTIONS'])
def handle_preflight():
    return '', 204  # No content, just acknowledge the preflight request


@authentication_bp.after_request
def set_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response


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
        is_valid_session = active_session(col, token)

        # User has an active session
        if is_valid_session:
            logging.info("user tried to log in again")
            # return the values already stored in the session dictionary from previous login
            user_session_info = get_user_session_data(col, token)
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
            insert_user_session_into_mongodb(
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
    "username, oldpassword,newpassword"
    return "ok"


@authentication_bp.route("/api/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    return "ok"


def active_session(col, session_id: str) -> bool:

    user_session_data = {'session': session_id}

    try:
        user_profile = col.find_one(user_session_data)
        return True if user_profile.get("session") else False

    except:
        return False


def get_user_session_data(col, session_id: str) -> dict:
    user_session_data = {'token': session_id}
    session_dict = {}
    try:
        user_profile = col.find_one(user_session_data)
        session_dict['token'] = user_profile.get("token")
        session_dict['expiration'] = user_profile.get("expiration")
        session_dict['username'] = user_profile.get("username")
        return (session_dict)

    except:
        return session_dict


def remove_user_session_from_mongodb(col, auth_token):
    user_session_data = {'token': auth_token}
    col.delete_one(user_session_data)


def insert_user_session_into_mongodb(col, auth_token, username, expiration):
    user_session_data = {'token': auth_token,
                         'username': username, 'date': datetime.now(),
                         'expiration': expiration}
    col.insert_one(user_session_data)
