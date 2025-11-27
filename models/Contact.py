from mongoengine import Document, StringField

class Contact(Document):
    name = StringField(required=True)
    phone = StringField(required=True)
    
    meta = {"collection" : "contacts"}