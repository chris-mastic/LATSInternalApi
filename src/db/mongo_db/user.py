from datetime import datetime
from mongoengine import Document, StringField, DateTimeField
import services.helpers as helper


class User(Document):
    """
    Various methods used for performing CRUD operantions on a Mongodb database


    Attributes:
        token (string): LTC auth token
        username (string): username provided at login by user
        expiration (datetime): Expiration set on LTC auth token 

    Methods:
        active_session(collection, session_id: str) -> bool:
            '''
            Determines if the LTC token is in user_session collection

            Args:
                collection (mongodb Collection) : A Mongodb Collection object
                session_id (string): LTC token

                Returns:
                    bool: LTC token found or not found
            '''
        get_user_session_data(collection, session_id: str) -> dict:
            '''
            Determines whether a given LTC token exists in user_session collection

            Args:
                collection (mongodb collection): A Mongodb Colleciont object
                session_id (string): The token assigned by LTC and used to identify a user

            Returns:
                dict: A dictionary with following structure
                    dict: A dictionary with following structure:
                        {
                            "session_dict": {
                                'token': 'token',
                                'token_expiration': 'token_expiration',
                                'username': username'

                            }

                        }

            '''

        remove_user_from_mongodb(db, auth_token: str) -> int:
            '''
            '''

        insert_user_session_into_mongodb(collection, auth_token, username, expiration):
            '''
            '''

        insert_user_data_into_mongodb(collection, req):
            '''
            '''

        get_user_data(collection, auth_token: str) -> dict:
            '''
            '''


    """

    # Get docstring for parent class 'Document'
    __doc__ += Document.__doc__

    token = StringField(required=True, unique=True)
    username = StringField(max_length=30)
    expirtation = DateTimeField(required=True)


def active_session(collection, auth_token: str) -> bool:

    user_session_data = {'token': auth_token}

    try:
        user_profile = collection.find_one(user_session_data)
        return True if user_profile.get("token") else False

    except:
        return False


def get_user_session_data(collection, auth_token: str) -> dict:
    """
    Determines whether a given LTC token exists in user_session collection

    Args:
        collection: The user_session collection
        session_id: The token assigned by LTC and used to identify a user

    Returns:
        dict: A dictionary with following structure:
            {
                "session_dict": {
                    'token': 'token',
                    'token_expiration': 'token_expiration',
                    'username': username'

                }

            }
    """
    user_session_data = {'token': auth_token}
    session_dict = {}
    try:
        user_profile = collection.find_one(user_session_data)
        session_dict['token'] = user_profile.get("token")
        session_dict['token_expiration'] = user_profile.get("token_expiration")
        session_dict['username'] = user_profile.get("username")
        return (session_dict)

    except:
        return session_dict


def remove_user_from_mongodb(db, auth_token: str) -> int:
    """
    Removes all documents, from all collections associated with a token

    Args: 
        db: The mongodb connection
        auth_token: The token assigned by LTC and used to identify a user

    Returns:
        int: 0 for success, 1 for failure
    """
    try:
        collection_names = db.list_collection_names()
        for collection_name in collection_names:
            collection = db[collection_name]
            if collection.count_documents({"token": auth_token}) > 0:
                collection.delete_many({"token": auth_token})
        return 0
    except:
        return 1


def insert_user_session_into_mongodb(collection, auth_token, username, expiration):
    user_session_data = {'token': auth_token,
                         'username': username, 'date': datetime.now(),
                         'token_expiration': expiration}
    collection.insert_one(user_session_data)


def create_update_user_data(collection, req) -> int:
    """
    Determines whether to insert new document into user_data or update 
    existing document.

    Args: 
        collection: The mongodb collection - user_data
        req: Dictionary of k,v pairs received as user request

    Returns:
        int: 0 for success, 1 for failure
    """
    if (_is_new_data_insertion(collection, req['token'])):
        return _insert_new_user_data_into_mongodb(collection, req)
    else:
        # Updates single document
        return _update_user_data(collection, req)


def _is_new_data_insertion(collection, auth_token) -> bool:
    user_session_data = {'token': auth_token}
    try:
        return False if collection.find_one(user_session_data) else True
    except:
        return False


def _insert_new_user_data_into_mongodb(collection, req) -> int:
    """
    Inserts a new document into user_data collection

    Args:
        colleciton: A mongodb collection - user_data
        req: Dictionary of k,v pairs received as user request

    Returns:
        int: 0 for success, 1 for failure     
    """
    try:
        req['created'] = datetime.now()
        collection.insert_one(req)
        return 0

    except:
        return 1


def _update_user_data(collection, req) -> int:
    """
    Updates an existing document in user_data collection

    Args:
        colleciton: A mongodb collection - user_data
        req: Dictionary of k,v pairs received as user request

    Returns:
        int: 0 for success, 1 for failure     
    """
    try:
        req['modified'] = datetime.now()
        collection.update_one({"token": req['token']}, {"$set": req})
        return 0

    except:
        return 1


def get_user_data(collection, auth_token: str) -> dict:
    user_data = {'token': auth_token}
    user_data = {key.replace('"', ''): val.replace('"', '')
                 for key, val in user_data.items()}

    try:
        data = collection.find_one(user_data)
        # delete _id, since it is not needed
        del data['_id']
        return (data)

    except:
        return helper.create_json_object(code="500", message="unable to retrieve user data")
