from flask import Flask
from mongoengine import connect

connect(db="contact-flask",host="mongodb://localhost:27017/contact-flask")

appFlask = Flask(__name__)

from routes import *

if __name__ == "__main__":
    appFlask.run(debug=True)
    
    
    

# add contact @
# edit contact
# delete contact
# show contact
# search one contact