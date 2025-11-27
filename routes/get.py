from flask import jsonify

from app import appFlask
from models.Contact import Contact
from utils.decode_mongo import decode_mongo

@appFlask.route("/", methods=["GET"])
def get_handler():
    contacts = decode_mongo(Contact.objects())
    
    return jsonify({
        "message" : "get contacts successfuly",
        "result" : contacts
    })