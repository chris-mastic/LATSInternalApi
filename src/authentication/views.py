from bson.objectid import ObjectId
from flask_cors import cross_origin
import functools
import flask
# Note: current_app the application instance returned by the factory function in __init__.py
from flask import Blueprint, request, render_template, jsonify, session, current_app
from itsdangerous import URLSafeTimedSerializer
import json
import logging
from pymongo import MongoClient
import warnings

from db.mongo_db import user
import helpers as util
from services.ltc_api_connections import LTCApiConnections


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


@authentication_bp.route("/api/logout", methods=['POST'])
def logout():

    ltc_api = LTCApiConnections(logging)
    req = json.loads(request.data)
    token = req['token']
    username = req['username']

    with current_app.app_context():
        client = MongoClient(current_app.config['MONGO_URI'])
        mongodb = client[current_app.config['MONGO_DBNAME']]
        user_session_col = mongodb["user_session"]
        user_data_col = mongodb["user_data"]
        if user.active_session(user_session_col, token):
            resp = ltc_api.logout(username, token)
            rtn_code = user.remove_user_from_mongodb(user_session_col, token)
            if rtn_code == 0:
                rtn_code = user.remove_user_from_mongodb(user_data_col, token)
                if rtn_code != 0:
                    logging.error(
                        f'{token} unable to delete from user_data collection')

            else:
                logging.error(
                    f'{token} unable to delete from user_session collection')
            del ltc_api
            return util.create_json_object(code="200",message="Logged out")

        else:
            return util.create_json_object(code="200",message="Not logged in")


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

    print(f"secret_key {current_app.config['SECRET_KEY']}")
    print(f"development {current_app.config['DEVELOPMENT']}")
    print(f"flask_debug {current_app.config['FLASK_DEBUG']}")
    print(f"debug {current_app.config['DEBUG']}")

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
                return util.create_json_object(code="200",token=user_session_info['token'], expiration=user_session_info['token_expiration'], username=user_session_info['username'])
            else:
                # returns an empty dictionary
                return util.create_json_object(code="500", message="unable to fetch user information")

        # No active session, try to create one
        else:
            # Connect to LTC API
            ltc_api = LTCApiConnections(logging)
            response = ltc_api.login(username, password)
            # Log bad response
            if type(response) is not dict and 'token' not in response.json:
                logging.error(f'{username} unable to log in to LTC site')
                del ltc_api
                return util.create_json_object(code="401", message="unable to login. check username and password")

            # Valid response, write to database
            user.insert_user_session_into_mongodb(
                col,  response['token'], username, response['expiration'])
            del ltc_api

            return util.create_json_object(code="200",token=response['token'], expiration=response['expiration'], username=username)


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
    return util.create_json_object(code="200",message="password reset")


@authentication_bp.route("/api/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    return util.create_json_object(code="200",message="check email for password reset link")
