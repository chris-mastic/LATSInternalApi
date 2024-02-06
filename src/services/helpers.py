def isvalid_session(session_id_from_cookie: str, session_id_from_server: str) -> bool:
    if session_id_from_cookie == session_id_from_server:
        return True
    return False

def clear_session(session,response):
    session.clear()
    response.set_cookie('session', expires=0)
    return response