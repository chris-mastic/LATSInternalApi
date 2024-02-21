import sys

additional_paths = [
        '/var/www/LATSInternalApi/src',
        '/var/www/LATSInternalApi/src/services/',
        '/var/www/LATSInternalApi/src/db/'
        ]
sys.path.extend(additional_paths)

import helpers as helper
from services.ltc_api_connections import LTCApiConnections
from flask import Blueprint, request, render_template, jsonify, session, current_app, make_response
import flask
from flask_login import login_user
from itsdangerous import URLSafeTimedSerializer
import json
import oracle_db_connection as odb
import os
import pandas as pd
import urllib.request as urlRequest
import urllib.request
import urllib.parse as urlParse
import urllib.error as urlError




authentication_bp = Blueprint("authentication", __name__, template_folder='authentication/templates')


@authentication_bp.route("/", methods=['GET', 'POST'])
def index():
    return render_template('authentication/index.html')
  

@authentication_bp.route("/api/logout", methods=['POST'])
def logout():

    ltc_api = LTCApiConnections()
    if 'username' in session:
        response = ltc_api.logout(
            flask.session['username'], flask.session['token'])
    else:
        response = jsonify({
            'message': 'Not logged in'
        })

    helper.clear_session(response)
    # Implicity destroy connection instance.
    del ltc_api
    return response


@authentication_bp.route("/api/login", methods=['POST'])
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

    session_id_from_cookie = request.cookies.get('session')
    session_id_from_server = session.sid

    if helper.is_valid_session(session_id_from_cookie, session_id_from_server):
        # return the values already stored in the session dictionary from previous login
        return jsonify({
            'token': session.get('token'),
            'expiration': session.get('expiration'),
            'userName': session.get("username"),
            'userId': session.get('userId'),
            'roles': session.get('roles')
        })
    else:
        # Create a new session
        ltc_api = LTCApiConnections()
        response = ltc_api.login(username, password)
        print(f"resonpnse {response}")
        set_flask_session_values(response)

        if flask.session['token'] is None:
            del ltc_api
            return helper.clear_session(response)

        del ltc_api
        return create_json_object()


def set_flask_session_values(response: object):
    flask.session["token"] = None
    # store in the session dictionary
    token = response['token']
    flask.session["token"] = token
    flask.session['secretkey'] = current_app.secret_key.encode('utf-8')
    flask.session['username'] = response['userName']
    flask.session['expiration'] = response['expiration']
    flask.session['roles'] = response['roles']
    flask.session['userId'] = response['userId']


def create_json_object() -> object:

    return jsonify({
        'token': flask.session["token"],
        'expiration': flask.session['expiration'],
        'userName': flask.session['username'],
        'userId': flask.session['userId'],
        'roles': flask.session['roles']
    })


"""
    NOT CURRENTLY IMPLEMENTED
"""


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
