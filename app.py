import os

from flask import Flask
from mongoengine import connect
from dotenv import load_dotenv

load_dotenv()
connect(db= os.getenv("DB_NAME"), host= os.getenv("DB_HOST"))

appFlask = Flask(__name__)

from routes import *

if __name__ == "__main__":
    appFlask.run(debug=True)
    

# add contact @
# edit contact /
# delete contact /
# show contact @
# search one contact @