import os
from flask import Blueprint, request, render_template, jsonify, session, current_app, make_response
import flask
from flask_login import login_user
from itsdangerous import URLSafeTimedSerializer
import json
import oracle_db as odb
import pandas as pd
import urllib.request as urlRequest
import urllib.request
import urllib.parse as urlParse
import urllib.error as urlError

authentication_bp = Blueprint("authentication", __name__)


@authentication_bp.route("/", methods=['GET', 'POST'])
def index():
    print('in index')

    db = odb.OracleDB.getInstance()
    conn = db.engine.connect()
    # result = conn.execute('SELECT * FROM cmazza.noa_report_filter')

    # with db.engine.connect() as connection:
    # # print(connection.scalar(text("""SELECT UNIQUE CLIENT_DRIVER
    # #                                 FROM V$SESSION_CONNECT_INFO
    # #                                 WHERE SID = SYS_CONTEXT('USERENV', 'SID')""")))
    # #print(connection.execute(text("SELECT * FROM noa_report_filter")))
    test_df = pd.read_sql_query("""SELECT a.parid FROM ASMT a INNER JOIN LEGDAT l ON a.parid = l.parid AND a.cur = l.cur AND l.taxyr = a.taxyr 
                    WHERE a.taxyr = 2025 AND l.cur = 'Y' AND a.parid = '7501-ROCHONAV'  """, db.engine)
    print(test_df)


#     from sqlalchemy.engine import create_engine
#     import pandas as pd
#     import cx_Oracle

#     host_name   = 'opaodb-01.assessororleans.gov'# content of "Host"
#     port_number = 1521 # content of "Port"
#     user_name   = 'IASWORK' # content of "User name"
#     pwd  =  'IASWORK' # content of "Password"
#     service_name = 'IASWORK' # content of "Database" (the "Service Name" option is selected)

#     #dsn_tns = cx_Oracle.makedsn(host_name, port_number, service_name = service_name)
#    # dsn_tns = cx_Oracle.makedsn(host_name, 1521, service_name=service_name)
#     #dsn = cx_Oracle.makedsn(host_name, 1521, sid='IASWORK')
#     dsn = cx_Oracle.makedsn("oracle.opaodb-01.assessororleans.gov", "1521", service_name="IASWORK")
#     conn = cx_Oracle.connect(user = user_name, password = pwd, dsn = dsn, encoding='UTF-8')

    # engine = create_engine('oracle://IASWORK:IASWORK@IASWORK')
    # con = engine.connect()
    # output = con.execute("SELECT * FROM noa_report_filter")
    # df = pd.DataFrame(output.fetchall())
    # df.columns = output.keys()
    # print(df.head())
    # con.close()

    # DIALECT = 'oracle'
    # SQL_DRIVER = 'cx_oracle'
    # USERNAME = 'IASWORK'
    # PASSWORD = 'IASWORK'
    # HOST = 'opaodb-01.assessororleans.gov'
    # PORT = 1521
    # SERVICE = 'IASWORK'

    # ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

    # engine = create_engine(ENGINE_PATH_WIN_AUTH)

    # test_df = pd.read_sql_query('SELECT * FROM noa_report_filter', engine)
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

    print('in logout')
    print(f"token {flask.session['token']}")
    # url = os.environ.get('LTC_API_URL_TEST')
    url = os.environ.get('LTC_API_URL_PROD')

    paths = [url, "Users/v1/logout"]
    url = "".join(paths)

    values = {"username": f"{flask.session['username']}"
              }
    headers = {"Accept": "text/plain",
               "Authorization": f"Bearer {flask.session['token']}"
               }

    creds = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(
        url, headers=headers, data=creds, method='POST')

    # req = urlRequest.Request(url, creds, headers)
    print(f"req {req}")
    with urlRequest.urlopen(req) as response:
        body = response.read()

    # print(f"after the WITH {body}")
    # resp = json.loads(body)
    # print(f"resp {resp}")

    response = make_response('Logged out successfully')
    clear_session(response)
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

    print(f"username {username}")
    print(f"password {password}")

    # Check if user has an active session
    # Get the session ID from the cookie
    session_id_from_cookie = request.cookies.get('session')
    # Get the session ID from the server
    session_id_from_server = session.sid
    # Compare the two IDs
    if session_id_from_cookie == session_id_from_server:
        # return the values already stored in the session dictionary from previous login
        print("in first if")
        return jsonify({
            'token': session.get('token'),
            'expiration': session.get('expiration'),
            'userName': session.get("username"),
            'userId': session.get('userId'),
            'roles': session.get('roles')
        })

    # If user does not have an active session
    if session_id_from_cookie != session_id_from_server or session_id_from_cookie is None:
        print('in second if')

        # url = os.environ.get('LTC_API_URL_TEST')
        url = os.environ.get('LTC_API_URL_PROD')

        paths = [url, "Auth/v1/authenticate?param=value&param2=value"]
        url = "".join(paths)

        values = {"username": username,
                  "password": password
                  }
        headers = {'accept': '*/*',
                   "Content-Type": "application/json"}

        response = make_response(authenticate_user(url, values, headers))

        # assign values to cookies only if user was able to connect to LTC API
        if flask.session['token'] is not None:
            # response.set_cookie('ltcToken', flask.session["token"])
            response.set_cookie('ltcToken')
        else:
            clear_session(response)
            response.set_cookie('session', expires=0)

        return response


def authenticate_user(url, values, headers) -> object:

    creds = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(
        url, headers=headers, data=creds, method='POST')

    flask.session["token"] = None
    # req = urlRequest.Request(url, creds, headers)
    print("In authenticate, before the try block")
    try:
        with urlRequest.urlopen(req) as response:
            body = response.read()

        resp = json.loads(body)

        # store in the session dictionary
        token = resp['token']
        flask.session["token"] = token
        flask.session['secretkey'] = current_app.secret_key.encode('utf-8')
        flask.session['username'] = resp['userName']
        flask.session['expiration'] = resp['expiration']
        flask.session['roles'] = resp['roles']
        flask.session['userId'] = resp['userId']

        # TODO figure out how to use the SECRET_KEY and salt it with the session id
        # need to use this value to salt the secret key and return to user
        session_id = create_salted_key(flask.session["token"])

        return jsonify({
            'token': resp['token'],
            'expiration': resp['expiration'],
            'userName': resp['userName'],
            'userId': resp['userId'],
            'roles': resp['roles']
        })

    except urlError.URLError as e:
        message = "There is a problem connecting to the LTC API"
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
    s = URLSafeTimedSerializer(
        current_app.secret_key, api_token)  # ,authtoken)
    signed = s.dumps(session.sid)
    print(f"signe {signed}")

    print(f"decoded {s.loads(signed)}")
    print(f"session id {session.sid}")

    return signed


def clear_session(response):
    session.clear()
    response.set_cookie('session', expires=0)
    response.set_cookie('ltcToken', expires=0)
    return response


@authentication_bp.route("/api/reset_password", methods=['GET', 'POST'])
def reset_password():
    "username, oldpassword,newpassword"
    return "ok"


@authentication_bp.route("/api/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    return "ok"
