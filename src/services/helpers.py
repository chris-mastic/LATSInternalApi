from flask import session, current_app, make_response

def is_valid_session(request_body_session_id: str) -> bool:
    pass


# def is_valid_session(session_id_from_cookie: str, session_id_from_server: str) -> bool:
#     if session_id_from_cookie == session_id_from_server:
#         return True
#     return False

# def clear_session(response: object) -> object:
#     session.clear()
#     response.set_cookie('session', expires=0)
#     return response