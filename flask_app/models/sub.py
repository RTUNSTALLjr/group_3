from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

db = "sub_shop"

class Sub:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.description=data['description']
        self.img_url=data['img_url']
        self.bread=data['bread']
        self.protein=data['protein']
        self.cheese=data['cheese']
        self.vegetables=data['vegetables']
        self.sauce=data['sauce']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def delete_sub(cls,data):
        query ="DELETE FROM subs WHERE id =%(id)s"
        result= connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all_subs(cls,data):
        query ="SELECT * FROM subs"
        result = connectToMySQL(db).query_db(query,data)
    
    @classmethod
    def get_sub_by_id(cls,data):
        query = "SELECT * FROM subs WHERE id =%(id)s"
        results = connectToMySQL(db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update_sub(cls,data):
        query="UPDATE subs SET name=%(name)s,price=%(price)s,description=%(description)s,img_url=%(img_url)s,bread=%(bread)s,protein=%(protein)s,cheese=%(cheese)s,vegetables=%(vegetable)s,sauce=%(sauce)s,updated_at= NOW "
        return connectToMySQL(db).query_db(query,data) 