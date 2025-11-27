from flask import jsonify

from app import appFlask
from models.Contact import Contact
from utils.decode_mongo import decode_mongo

@appFlask.route("/<name>", methods=["GET"])
def get_by_name_handler(name):
    contacts = decode_mongo(Contact.objects(name = name))
    
    if len(contacts) == 0:
        return jsonify({
            "message": "Contact not found",
            "result" : None
        }), 404
        
    return jsonify({
        "message" : "Get contact successfuly",
        "result" : contacts[0]
    }), 200