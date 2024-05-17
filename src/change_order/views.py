
import asyncio
from datetime import datetime, timezone
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
    req = json.loads(request.data)
    print(f"req body {req}")

    tax_year = '2024'
    fips_code = '1234'
    assessment_no = '12'
    batch_created = '04-25-2024'

    # Connect to db

    try:
        db = mysqldb.MySQLDBConnection()
        engine = db.engine
        cursor = connection.cursor()
        with engine.connect() as connection:
            insert_stmt = noa_ltc_change_order_table.insert().values(
                tax_year='2024', fips_code='1234', assessment_no='12', batch_created='04-25-2024')
            connection.execute(insert_stmt)
            connection.commit()

    except Exception as e:
        print(f"Error connecting to MySQL: {str(e)}")

    return "ok"

def batch_exists(token) -> tuple:
    print("in batch_exists")
    try:
        db = mysqldb.MySQLDBConnection()
        engine = db.engine
        with engine.connect() as connection:
            sql_query = text('SELECT * FROM noa_ltc_change_order WHERE auth_token = :token')
            results = connection.execute(sql_query, {"token":token})
            rows = results.fetchall()
            print("after rows")
            if rows:
                print("in if")
                return (True, results)
            else:
                print("in else")
                return (False,)
    except Exception as e:
        print(f"Error connecting to MySQL: {str(e)}")


def update_noa_ltc_change_order(df):
    
    try:
        db = mysqldb.MySQLDBConnection()
        engine = db.engine
        print("within update_noa_ltc_change_order")
        with engine.connect() as connection:
            df.to_sql('noa_ltc_change_order', con=engine,
                      if_exists='append', index=False)
            # insert_stmt = noa_ltc_change_order_table.insert().values(
            #     auth_token=df["auth_token"][ind],
            #     tax_year=df["tax_year"][ind],
            #     fips_code=df["fips_code"][ind],
            #     assessment_number=df["assessment_number"][ind],
            #     ward=df["ward"][ind],
            #     assessor_ref_no=df["assessor_ref_no"][ind],
            #     place_fips=df["place_fips"][ind],
            #     parcel_address=df["parcel_address"][ind],
            #     assessment_type=df["assessment_type"][ind],
            #     assessment_status=df["assessment_status"][ind],
            #     # dto.homestead_exempt,
            #     homestead_exempt=df["homestead_exempt"][ind],
            #     homestead_percent=df["homestead_percent"][ind],
            #     restoration_tax_exempt=df["restoration_tax_exempt"][ind],
            #     taxpayer_name=df["taxpayer_name"][ind],
            #     contact_name=df["contact_name"][ind],
            #     taxpayer_addr1=df["taxpayer_addr1"][ind],
            #     taxpayer_addr2=df["taxpayer_addr2"][ind],
            #     taxpayer_addr3=df["taxpayer_addr3"][ind],
            #     city=df["city"][ind],
            #     state=df["state"][ind],
            #     zipcode=df["zipcode"][ind],
            #     tc_fee_pd=df["tc_fee_pd"][ind],
            #     reason=df["reason"][ind],
            #     check_no=df["check_no"][ind],
            #     check_amount=df["check_amount"][ind],
            #     batch_no=df[""][ind],
            #     ltc_nbr_total=df[""][ind],
            #     batch_created=df[""][ind],
            #     status=df[""][ind],
            #     batch_updated=df[""][ind],
            #     batch_submitted=df[""][ind],
            #     batch_approved=df[""][ind],
            #     batch_rejected=df[""][ind],
            #     reject_reason=df[""][ind],
            #     approved_by=df[""][ind],
            #     received_by=df[""][ind],
            #     batch_submitted_by=df[""][ind],
            #     co_detail_id=df[""][ind],
            #     fk_co_master=df[""][ind],
            #     status_cod=df[""][ind],
            #     status_date=df[""][ind],
            #     ltc_comment=df[""][ind],
            #     batch_item_no=df[""][ind],
            #     prop_desc=df[""][ind],
            #     co_submitted_by=df[""][ind],
            #     id_cav=df[""][ind],
            #     changeordersdetailsid=df[""][ind],
            #     presentdescription=df[""][ind],
            #     presentexempt=df[""][ind],
            #     presenttotalassessed=df[""][ind],
            #     presenthomesteadcredit=df[""][ind],
            #     presenttaxpayershare=df[""][ind],
            #     presentquantity=df[""][ind],
            #     presentunits=df[""][ind],
            #     reviseddescription=df[""][ind],
            #     revisedexempt=df[""][ind],
            #     revisedtotalassessed=df[""][ind],
            #     revisedhomesteadcredit=df[""][ind],
            #     revisedtaxpayershare=df[""][ind],
            #     revisedunits=df[""][ind],
            #     revisedquantity=df[""][ind],
            #     land_ltc_sub_class_old=df[""][ind],
            #     land_ltc_sub_class_new=df[""][ind],
            #     land_quantity_old=df[""][ind],
            #     land_quantity_new=df[""][ind],
            #     land_units_old=df[""][ind],
            #     land_units_new=df[""][ind],
            #     land_other_exempt_old=df[""][ind],
            #     land_other_exempt_new=df[""][ind],
            #     land_value_old_total=df[""][ind],
            #     land_value_new_total=df[""][ind],
            #     land_value_old_hs=df[""][ind],
            #     land_value_new_hs=df[""][ind],
            #     land_value_old_tp=df[""][ind],
            #     land_value_new_tp=df[""][ind],
            #     building_ltc_sub_class_old=df[""][ind],
            #     building_ltc_sub_class_new=df[""][ind],
            #     building_quantity_old=df[""][ind],
            #     building_quantity_new=df[""][ind],
            #     building_units_old=df[""][ind],
            #     building_units_new=df[""][ind],
            #     building_other_exempt_old=df[""][ind],
            #     building_other_exempt_new=df[""][ind],
            #     building_value_old_tota=df[""][ind],
            #     building_value_new_total=df[""][ind],
            #     building_value_old_hs=df[""][ind],
            #     building_value_new_hs=df[""][ind],
            #     building_value_old_tp=df[""][ind],
            #     building_value_new_tp=df[""][ind])
            # connection.execute(insert_stmt)
            # connection.commit()

    except Exception as e:
        print(f"Error connecting to MySQL: {str(e)}")

    return "ok"


@change_order_bp.route("/api/get_batch", methods=['GET', 'POST'])
def get_batch():
    req = json.loads(request.data)
    token = req['token']
    parid = req['parid']
    taxyear = req['taxyear']
    altid = req['altid']

    rtn = batch_exists(token)
    exists = rtn[0]

    print(f"reuslt {rtn} and exists {exists}")
    if(not(exists)):
        """Query Oracle DB and retrieve records
            Insert new record into MySQL and
            return results to user
        """
        print("in if(not(exists))")
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

            # print(f"query {query}")

            df = pd.read_sql_query(query, engine, params=[
                (parid, taxyear,)])
            df['auth_token'] = [token]
            utc_time = datetime.now().astimezone(timezone.utc)
            df['batch_created'] = utc_time.strftime('%Y-%m-%d %H:%M:%S')
            
            print(f"df {df}")
            # Write to MySQL table
            
            update_noa_ltc_change_order(df)

            # Format data to return to front end
            json_data = json.dumps(df.to_dict(orient='records'))
            return json_data

        except Exception as e:
            print(f"Error connecting to MySQL: {str(e)}")
    
    else:
        """ Return existing record in MySQL only
        """
        rows = rtn[1].fetchall()
        column_names = rtn[1].keys()
        print(column_names)
        print(f"rows {rows}")
        result_list = []
        for row in rows:
            row_dict = dict(zip(column_names, row))
            print(f"row_dict {row_dict}")
            result_list.append(row_dict)
        print(f"result_list {result_list}")   
        return json.dumps(result_list, indent=4)
        


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


@change_order_bp.route("/api/insert_change_orders", methods=['POST'])
def insert_change_orders():
    req = json.loads(request.data)
    tax_year = req['tax_year']
    fips_code = req['fips_code']
    assessment_no = req['assessment_no']
    ward = req['']
    assessor_ref_no = req['']
    place_fips = req['']
    parcel_address = req['']
    assessment_type = req['']
    assessment_status = req['']
    homestead_exempt = req['']
    homestead_percent = req['']
    restoration_tax_expmt = req['']
    taxpayer_name = req['']
    contact_name = req['']
    taxpayer_addr1 = req['']
    taxpayer_addr2 = req['']
    taxpayer_addr3 = req['']
    tc_fee_pd = req['']
    check_no = req['']
    check_amount = req['']
    ltc_sub_class_old_land = req['']
    ltc_sub_class_new_land = req['']
    quantity_old_land = req['']
    quantity_new_land = req['']
    units_old_land = req['']
    units_new_land = req['']
    other_exempt_old_land = req['']
    other_exempt_new_land = req['']
    value_old_total_land = req['']
    value_new_total_land = req['']
    value_old_hs_land = req['']
    value_new_hs_land = req['']
    value_old_tp_land = req['']
    value_new_tp_land = req['']
    ltc_sub_class_old_building = req['']
    ltc_sub_class_new_building = req['']
    quantity_old_building = req['']
    quantity_new_building = req['']
    units_old_building = req['']
    units_new_building = req['']
    other_exempt_old_building = req['']
    other_exempt_new_building = req['']
    value_old_total_building = req['']
    value_new_total_building = req['']
    value_old_hs_building = req['']
    value_new_hs_building = req['']
    value_old_tp_building = req['']
    value_new_tp_building = req['']
    print("IN INSERT..")
    try:
        print('connecting to db....')
        # db = odb.OracleDBConnection()
        db = mysqldb.MySQLDBConnection()
        engine = db.engine

        # "val04": [val01],
        # "val05": [val02]
        data_to_insert = {
            "parcel_add": [parid],
            "value_new_total_land": [val01],
            "value_new_total_building": [val02],
            "tax_year": [],
            "fips_code": [],
            "assessment_no": [],
            "ward": [],
            "assessor_ref_no": [],
            "place_fips": [],
            "parcel_address": [],
            "assessment_type": [],
            "assessment_status": [],
            "homestead_exempt": [],
            "homestead_percent": [],
            "restoration_tax_expmt": [],
            "taxpayer_name": [],
            "contact_name": [],
            "taxpayer_addr1": [],
            "taxpayer_addr2": [],
            "taxpayer_addr3": [],
            "tc_fee_pd": [],
            "reason": [],
            "check_no": [],
            "check_amount": [],
            "ltc_sub_class_old_land": [],
            "ltc_sub_class_new_land": [],
            "quantity_old_land": [],
            "quantity_new_land": [],
            "units_old_land": [],
            "units_new_land": [],
            "other_exempt_old_land": [],
            "other_exempt_new_land": [],
            "value_old_total_land": [],
            "value_new_total_land": [],
            "value_old_hs_land": [],
            "value_new_hs_land": [],
            "value_old_tp_land": [],
            "value_new_tp_land": [],
            "ltc_sub_class_old_building": [],
            "ltc_sub_class_new_building": [],
            "quantity_old_building": [],
            "quantity_new_building": [],
            "units_old_building": [],
            "units_new_building": [],
            "other_exempt_old_building": [],
            "other_exempt_new_building": [],
            "value_old_total_building": [],
            "value_new_total_building": [],
            "value_old_hs_building": [],
            "value_new_hs_building": [],
            "value_old_tp_building": [],
            "value_new_tp_building": []
        }

        df = pd.DataFrame(data_to_insert)
        print(f"df {df}")
        df.to_sql(name=current_app.config['PARID_CHANGE_ORDERS'],
                  con=engine, if_exists="append", index=False)

        return 'OK'

    except Exception as e:
        print(f"Error connecting to OracleSQL: {str(e)}")

        return jsonify({'message': 'Database error'})
