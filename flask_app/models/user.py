from flask import Flask,flash
from flask_app.config.mysqlconnection import connectToMySQL


db ='sub_shop'

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_id_by_email(cls,data):
        query = "SELECT id FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query,data)
        return(result[0]["id"])

    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT email FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query,data)
        if len(result) < 1:
            return False
        return(result[0]["email"])
    
    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        user_data={
            "id":results[0]['id'],
            'first_name':results[0]['first_name'],
            'last_name':results[0]['last_name'],
            'email':results[0]['email'],
            'password':"",
            'created_at':'',
            "updated_at":''
            }
        return cls(user_data)
    
    @classmethod
    def save(cls,data):
        query="INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        return connectToMySQL(db).query_db( query, data )