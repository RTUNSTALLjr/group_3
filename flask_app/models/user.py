from flask import Flask,flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

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
# creat a user
    @classmethod
    def create_user(cls, data):
        if not cls.validate_user_reg_data(data):
            return False
        parsed_data = cls.parse_reg_data(data)
        query = """
        INSERT INTO users (first_name,last_name,email,password,created_at,updated_at)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW())
            ;"""
        result = connectToMySQL(db).query_db(query,parsed_data)
        session['user_id'] = result
        return result

    @classmethod
    def get_id_by_email(cls,data):
        query = "SELECT id FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query,data)
        return(result[0]["id"])

    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT email FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query,data)
        if result:
            result = cls(result[0])
        return result
    
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
    
# Validation
    @staticmethod
    def validate_user_reg_data(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['first_name'])<3:
            flash("First name must be at least three character")
            is_valid = False
        if len(data['last_name'])<3:
            flash("Last name must be at least three character")
            is_valid = False
        if len(data['password'])<8:
            flash("Your password must be at least 8 character")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Please use the correct  email.')
            is_valid = False
        if User.get_user_by_email(data['email']):
            flash('That email is already in use.')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('Your passwords do not match')
            is_valid = False
        return is_valid
# pasrse data
    @staticmethod
    def parse_reg_data(data):
        parsed_data = {}
        parsed_data['first_name'] = data['first_name']
        parsed_data['last_name'] = data['last_name']
        parsed_data['password'] = bcrypt.generate_password_hash(data['password'])
        parsed_data['email'] = data['email']
        return parsed_data
# login validation
    @staticmethod
    def user_login(data):
        this_user = User.get_user_by_email(data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data['password']):
                session['user_id'] = this_user.id
                return True
        flash('Your enter wrong information')
