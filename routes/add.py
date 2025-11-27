from flask import request, jsonify

from app import appFlask
from models.Contact import Contact

@appFlask.route("/", methods=["POST"])
def add_handler():
    data = request.get_json()
    name = data.get("name")
    phone = data.get("phone")
    
    if not name :
        return jsonify({
            "message": "name is required",
            "result" : None
        }) , 400
    
    if not phone :
        return jsonify({
            "message": "phone is required",
            "result" : None
        }) , 400
    
    if len(phone) != 11 or not phone.isdigit():
        return jsonify({
            "message" : "phone invalid",
            "result" : None
        }), 400
    
    is_exist = Contact.objects(name = name).first()
    
    if is_exist :
        return jsonify({
            "message" : "contact is exist",
            "result" : None
        }), 400
    
    Contact(**data).save()
    
    return jsonify({
        "message" : "Add contact successfuly",
        "result" : data
    }), 201
