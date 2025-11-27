from flask import request

from app import appFlask
from models.Contact import Contact
from utils.decode_mongo import decode_mongo

@appFlask.route("/<n>", methods=["PUT"])
def edit_handler(n):
    data = request.get_json()
    
    name = data.get("name")
    phone = data.get("phone")
    
    contact = decode_mongo(Contact.objects(name = n))[0]
    
    if name :
        contact["name"] = name
        
    if phone :
        contact["phone"] = phone
    
    
    return contact
