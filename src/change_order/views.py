from flask import  Blueprint, request, jsonify

change_order_bp = Blueprint("change_order", __name__)

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

@change_order_bp.route("/api/submit_batch", methods=['GET', 'POST'])
def submit_batch():
    return "ok"

@change_order_bp.route("/api/get_status", methods=['GET', 'POST'])
def get_status():
    return "ok"