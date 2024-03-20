from flask import Blueprint, request, jsonify, session, current_app
import flask
import json
import logging
import os
import pandas as pd
from pymongo import MongoClient
import urllib.request as urlRequest
import urllib.request
import urllib.error as urlError

from db.la_tax_service_dtos import assess_values_dto, change_order_dto
import helpers as util 
import db.oracle_db_connection as odb


from db.mongo_db import user

logging.basicConfig(level=logging.DEBUG, filename=__name__, filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

change_order_bp = Blueprint("change_order", __name__)


def switch(start: int, stop: int, altid: str, item: str) -> str:
    fips = {"1": "22171", "2": "22172", "3": "22173",
            "4": "22174", "5": "22175", "6": "22176", "7": '22177'}

    val = altid[start:stop]

    if item == 'fips':
        return fips[altid[start:stop]]
    elif item == "ward":
        return '22172'
    elif val == "3":
        return '22173'
    elif val == "4":
        return '22174'
    elif val == "5":
        return '22175'
    elif val == "6":
        return '22176'
    elif val == "7":
        return '22177'
    else:
        return "Invalid altid"


@change_order_bp.route("/api/get_user_data", methods=['GET'])
def get_user_data():
    req = json.loads(request.data)
    token = req['token']
    print(f"token in get_user_data is {token}")
    with current_app.app_context():
        client = MongoClient(current_app.config['MONGO_URI'])
        mongodb = client[current_app.config['MONGO_DBNAME']]
        col = mongodb["user_data"]
        try:
            return user.get_user_data(col, token)
        except:
            print("in the except")
            return util.create_json_object(message='unable to retrieve user data.')


@change_order_bp.route("/api/set_user_data", methods=['POST'])
def set_user_data():
    req = json.loads(request.data)

    with current_app.app_context():
        client = MongoClient(current_app.config['MONGO_URI'])
        mongodb = client[current_app.config['MONGO_DBNAME']]
        col = mongodb["user_data"]
        try:
            user.insert_user_data_into_mongodb(col, req)
            return util.create_json_object(message='user data inserted into collection user_data')
        except:
            return util.create_json_object(message='insert into collection user_data failed')




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


@change_order_bp.route("/api/get_batch", methods=['GET', 'POST'])
def get_batch(): pass
# req = json.loads(request.data)
# parid = req['parid']
# taxyear = req['taxyear']
# altid = req['altid']
# print("IN get_batch()")
# # --------------------------------DEBUG---------------
# print("DEBUG------------------------------------------------------")
# print(f'flask.session["token"]{flask.session["token"]}')
# print(f'request.cookies.get("ltcToken"){request.cookies.get("ltcToken")}')
# print(f'session.sid{session.sid}')
# print(f'request.cookies.get("session"){request.cookies.get("session")}')

# if helper.is_valid_session(request.cookies.get("session"), session.sid):
#     print("ABOVE TRY.....")
#     # OracleDB is a singleton class
#     try:
#         print('connecting to db....')
#         db = odb.OracleDBConnection.getInstance()
#         print("IN TRY OF HELPER.IS_VALID_SESSION")
#         curr_dir = os.path.dirname(__file__)
#         print(f'curr_dir {curr_dir}')
#         parent_dir = os.path.dirname(curr_dir)
#         db_dir = os.path.join(parent_dir, 'db', 'db_scripts')
#         sql_filename = os.path.join(db_dir, 'get_batch.sql')
#         print(f"sql_filename {sql_filename}")
#         with open(sql_filename, 'r') as file:
#             print('in with...')
#             query = file.read()

#         df = pd.read_sql_query(query, db.engine, params=[
#                                (parid, taxyear, 'Y', altid)])
#         print(f'df {df}')
#         change_order = change_order_dto.ChangeOrderDTO()
#         print(f'type of change_order {type(change_order)} ')
#         assess_value = assess_values_dto.AssessOrdersDTO()
#         print("Befor the for loop.")
#         for ind in df.index:
#             # fips_code = switch(1,1,df["altid"][ind], 'fips')
#             print('before taxyear assignment')
#             change_order.tax_year = df["taxyr"][ind]
#             print('after taxyre assignment')
#             # change_order.fips_code = ""
#             change_order.assessment_no = df["altid"][ind]
#             # change_order.ward = ""
#             # change_order.assessor_ref_no = ""
#             # change_order.place_fips = ""
#             # change_order.parcel_address = ""
#             # change_order.assessment_type = ""
#             # change_order.assessment_status = ""
#             # change_order.homestead_exempt = ""
#             # change_order.homestead_percent = ""
#             # change_order.restoration_tax_exempt = ""
#             print('befor own1')
#             change_order.taxpayer_name = df['own1'][ind]
#             # change_order.contact_name = ""
#             # change_order.taxpayer_addr1 = ""
#             # change_order.taxpayer_addr2 = ""
#             # change_order.taxpayer_addr3 = ""
#             # change_order.tc_fee_pd = ""
#             # change_order.reason = ""
#             # change_order.check_no = ""
#             # change_order.check_amount = ""
#             # change_order.assess_values = ""

#         json_data = json.dumps(change_order.__dict__,
#                                indent=2, default=str)
#         print(f"json_data {json_data}")
#         return json_data

#     except:
#         return jsonify({'message': 'Database error'})
# else:
#     response = jsonify({
#         'message': 'Not logged in'
#     })
#     helper.clear_session(response)
#     return response


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
    if session_id_from_cookie == session_id_from_server:
        url = os.environ.get('LTC_API_URL_PROD')
        paths = [url, "Auth/v1/authenticate?param=value&param2=value"]

        url = "".join(paths)
        url = 'https://testapi.latax.la.gov/api/Auth/v1/ChangeOrderGetStatus?param=value&param2=value&param3=value&param4=value'

        values = {"changeOrderBatchId": change_order_batch_id,
                  "taxYear": tax_year,
                  "fipsCode": fips_code
                  }
        headers = {'accept': 'text/plain',
                   "Content-Type": "application/json"}  # ,
        # "Authorization": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDYxMjQ1MDcsImlzcyI6Imh0dHBzOi8vdGVzdGFwaS5sYXRheC5sYS5nb3YvIiwiYXVkIjoidGVzdCJ9.kz8fdH5-fD03OOW2GCLipNFf-HRQVHS178_3Pd1tgPc'
        # }

        creds = json.dumps(values).encode('utf-8')
        print('after creds')
        req = urllib.request.Request(
            url, headers=headers, data=creds, method='GET')
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
            flask.session['secretkey'] = current_app.secret_key.encode('utf-8')
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
