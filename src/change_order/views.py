from flask import Blueprint, request, jsonify, session, current_app
import flask
import json
import logging
import os
from flask_cors import cross_origin
import pandas as pd
from pymongo import MongoClient
from sqlalchemy import text
import urllib.request as urlRequest
import urllib.request
import urllib.error as urlError

from db.la_tax_service_dtos import assess_values_dto, change_order_dto
from db.mysql_table_definitions.noa_ltc_change_order_table import noa_ltc_change_order_table
import db.oracle_db_connection as odb
import db.mysql_db_connection as mysqldb
import services.helpers as util


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


""" Following two functions are intended to handle CORS related issuses
"""


@change_order_bp.route('/api/login', methods=['OPTIONS'])
def handle_preflight(response):
    """ This function receives the browser's preflight request (An HTTP OPTIONS request)
        The request should include headers (Orign, Access-Control-Request-Method and 
        Access-Control-Request-Headers). This will cause the server to respond with
        appropriate CORS headers indicating whether the actual request is allowed
        from the specific orign. The server includes CORS headers in its response (prefilight
        or acutal). 
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    # Lets browser know which custom headers are allowed
    response.headers["Access-Control-Allow-Headers"] = "*"
    # Specifies which HTTP methods are allowed (scheme)
    response.headers["Access-Control-Allow-Methods"] = "GET,POST"
    return '', 204  # No content, just acknowledge the preflight request

# after_request ensures this method will run after each response


@change_order_bp.after_request
def set_headers(response):
    # Allows any domain to access app
    response.headers["Access-Control-Allow-Origin"] = "*"
    # Lets browser know which custom headers are allowed
    response.headers["Access-Control-Allow-Headers"] = "*"
    # Specifies which HTTP methods are allowed (scheme)
    response.headers["Access-Control-Allow-Methods"] = "GET,POST"
    return response


@change_order_bp.route("/api/get_user_data", methods=['GET'])
@cross_origin()
def get_user_data():
    token = request.args.get('token')
    with current_app.app_context():
        client = MongoClient(current_app.config['MONGO_URI'])
        mongodb = client[current_app.config['MONGO_DBNAME']]
        collection = mongodb["user_data"]
        try:
            return user.get_user_data(collection, token)
        except:
            return util.create_json_object(code="500", message='unable to retrieve user data.')


@change_order_bp.route("/api/set_user_data", methods=['POST'])
@cross_origin()
def set_user_data():
    req = json.loads(request.data)
    # TODO: ADD VALIDATION. This method returns 200 even if no data was passed in

    with current_app.app_context():
        client = MongoClient(current_app.config['MONGO_URI'])
        mongodb = client[current_app.config['MONGO_DBNAME']]
        collection = mongodb["user_data"]
        try:
            rtn_code = user.create_update_user_data(collection, req)
            if rtn_code == 0:
                return util.create_json_object(
                    code="200", message='user data updated/inserted into collection user_data')
            else:
                return util.create_json_object(code="500", message='update/insert into collection user_data failed')
        except:
            return util.create_json_object(code="500", message='Method all to create_update_user_data failed')


@change_order_bp.route("/api/add_to_batch", methods=['GET', 'POST'])
def add_to_batch():
    """
    You will need to figure out how to add in the token here

    headers = {'accept': '*/*',
               "Content-Type": "application/json",
               "Authorization: Bearer " <token>
               }

    """

    # Get user data

    # Connect to db

    try:
        db = mysqldb.MySQLDBConnection()
        engine = db.engine

        with engine.connect() as connection:
            insert_stmt = noa_ltc_change_order_table.insert().values(
                tax_year='2024', fips_code='1234', assessment_no='12', batch_created='04-25-2024')
            connection.execute(insert_stmt)
            connection.commit()

    except Exception as e:
        print(f"Error connecting to MySQL: {str(e)}")

    return "ok"

def update_noa_ltc_change_order(dto:change_order_dto.ChangeOrderDTO):
    
    try:
        db = mysqldb.MySQLDBConnection()
        engine = db.engine

        with engine.connect() as connection:
            insert_stmt = noa_ltc_change_order_table.insert().values(
                auth_token = "12345",
                tax_year = dto.tax_year,
                fips_code = dto.fips_code,
                assessment_no = dto.assessment_no,
                ward = dto.ward,
                assessor_ref_no = dto.assessor_ref_no,
                place_fips = dto.place_fips,
                parcel_add = dto.parcel_add,
                assessment_type = dto.assessment_type,
                assessment_status = dto.assessment_status,
                homestead_exempt = "T",#dto.homestead_exempt,
                homestead_percent = dto. homestead_percent,
                restoration_tax_expmt = dto.restoration_tax_expmt,
                taxpayer_name = dto.taxpayer_name,
                contact_name = dto.contact_name,
                taxpayer_addr1 = dto.taxpayer_addr1,
                taxpayer_addr2 = dto.taxpayer_addr2,
                taxpayer_addr3 = dto.taxpayer_addr3,
                tc_fee_pd = dto.tc_fee_pd,
                reason = dto.reason,
                chk_no = dto.chk_no,
                chk_amt = dto.chk_amt,
                id_com = dto.id_com,
                batch_no = dto.batch_no,
                ltc_nbr_total = dto.ltc_nbr_total,
                batch_created = dto.batch_created,
                status = dto.status,
                batch_updated = dto.batch_updated,
                batch_submitted = dto.batch_submitted,
                batch_approved = dto.batch_approved,
                batch_rejected = dto.batch_rejected,
                reject_reason = dto.reject_reason,
                approved_by = dto.approved_by,
                received_by = dto.received_by,
                batch_submitted_by = dto.batch_submitted_by,
                co_detail_id = dto.co_detail_id,
                fk_co_master = dto.fk_co_master,
                status_cod = dto.status_cod,
                status_date = dto.status_date,
                ltc_comment = dto.ltc_comment,
                batch_item_no = dto.batch_item_no,
                prop_desc = dto.prop_desc,
                co_submitted_by = dto.co_submitted_by,
                id_cav = dto.id_cav,
                changeordersdetailsid = dto.changeordersdetailsid,
                presentdescription = dto.presentdescription,
                presentexempt = dto.presentexempt,
                presenttotalassessed = dto.presenttotalassessed,
                presenthomesteadcredit = dto.presenthomesteadcredit,
                presenttaxpayershare = dto.presenttaxpayershare,
                presentquantity = dto.presentquantity,
                presentunits = dto.presentunits,
                reviseddescription = dto.reviseddescription,
                revisedexempt = dto.revisedexempt,
                revisedtotalassessed = dto.revisedtotalassessed,
                revisedhomesteadcredit = dto.revisedhomesteadcredit,
                revisedtaxpayershare = dto.revisedtaxpayershare,
                revisedunits = dto.revisedunits,
                revisedquantity = dto.revisedquantity)
            connection.execute(insert_stmt)
            connection.commit()

    except Exception as e:
        print(f"Error connecting to MySQL: {str(e)}")

    return "ok"


@change_order_bp.route("/api/get_batch", methods=['GET', 'POST'])
def get_batch():
    req = json.loads(request.data)
    parid = req['parid']
    taxyear = req['taxyear']
    altid = req['altid']
    print("IN get_batch()")
    # --------------------------------DEBUG---------------
    print("DEBUG------------------------------------------------------")

    # OracleDB is a singleton class
    try:
        print('connecting to db....')
        db = odb.OracleDBConnection()
        engine = db.engine
        curr_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(curr_dir)
        db_dir = os.path.join(parent_dir, 'db', 'db_scripts')
        sql_filename = os.path.join(db_dir, 'get_batch.sql')
        with open(sql_filename, 'r') as file:
            print('in with...')
            query = file.read()

        print(f"query {query}")
        
        df = pd.read_sql_query(query, engine, params=[
            (parid, taxyear, 'Y', altid)])
        print(f'df {df}')

        change_order = change_order_dto.ChangeOrderDTO()
        print(f'type of change_order {type(change_order)} ')
        assess_value = assess_values_dto.AssessOrdersDTO()
        print("Befor the for loop.")
        for ind in df.index:
            # fips_code = switch(1,1,df["altid"][ind], 'fips')
            print('before taxyear assignment')
            change_order.tax_year = df["taxyr"][ind]
            print('after taxyre assignment')
            # change_order.fips_code = ""
            change_order.assessment_no = df["altid"][ind]
            change_order.ward = ""
            change_order.assessor_ref_no = ""
            change_order.place_fips = ""
            change_order.parcel_address = ""
            change_order.assessment_type = ""
            change_order.assessment_status = ""
            change_order.homestead_exempt = df['flag4'][ind]
            change_order.homestead_percent = ""
            change_order.restoration_tax_exempt = ""
            print('befor own1')
            change_order.taxpayer_name = df['own1'][ind]
            change_order.contact_name = ""
            change_order.taxpayer_addr1 = df['addr1'][ind]
            change_order.taxpayer_addr2 = df['addr2'][ind]
            change_order.taxpayer_addr3 = df['addr3'][ind]
            change_order.tc_fee_pd = ""
            change_order.reason = ""
            change_order.check_no = ""
            change_order.check_amount = ""
            change_order.assess_values = ""

        json_data = json.dumps(change_order.__dict__,
                               indent=2, default=str)
        print(f"json_data {json_data}")
        update_noa_ltc_change_order(change_order)
        return json_data

    except Exception as e:
        print(f"Error connecting to MySQL: {str(e)}")

        return jsonify({'message': 'Database error'})


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
