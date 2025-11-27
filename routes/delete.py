from app import appFlask

@appFlask.route("/<name>", methods=["DELETE"])
def delete_handler(name):    
    
    return name
