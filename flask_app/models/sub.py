from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
import re
number_regex = re.compile(r'^[0-9]\d*(.\d+)?$')
db = "sub_shop"

class Sub:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.brief_description=data['brief_description']
        self.full_description=data['full_description']
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
        query = "DELETE FROM subs WHERE id =%(id)s;"
        connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all_subs(cls):
        query = "SELECT * FROM subs;"
        results = connectToMySQL(db).query_db(query)
        sub_list = []
        for row in results:
            sub_list.append(cls(row))
        return sub_list
    
    @classmethod
    def get_sub_by_id(cls,data):
        query = "SELECT * FROM subs WHERE id =%(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def save_sub(cls,data):
        query = '''
            INSERT INTO subs (name, price, brief_description, full_description, img_url, bread, protein, cheese, vegetables, sauce)
            VALUES (%(name)s, %(price)s, %(brief_description)s, %(full_description)s, %(img_url)s, %(bread)s, %(protein)s, %(cheese)s, %(vegetables)s, %(sauce)s);
        '''
        return connectToMySQL(db).query_db( query, data )
    
    @classmethod
    def update_sub(cls,data):
        query = '''
            UPDATE subs
            SET name = %(name)s,
                price = %(price)s,
                brief_description = %(brief_description)s,
                full_description = %(full_description)s,
                img_url = %(img_url)s,
                bread = %(bread)s,
                protein = %(protein)s,
                cheese = %(cheese)s,
                vegetables = %(vegetables)s,
                sauce = %(sauce)s
            WHERE id = %(id)s;
        '''
        connectToMySQL(db).query_db(query,data) 

    @staticmethod
    def validate_sub(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters", "name")
            is_valid = False
        if not number_regex.match(data['price']):
            flash("Invalid price", "price")
            is_valid = False
        if len(data['brief_description']) < 1:
            flash("Description Required", "brief_description")
            is_valid = False
        if len(data['full_description']) < 1:
            flash("Description Required", "full_description")
            is_valid = False
        if len(data['bread']) < 1:
            flash("Bread Required", "bread")
            is_valid = False
        if len(data['protein']) < 1:
            flash("Invalid 2 characters required", "protein")
            is_valid = False
        if len(data['cheese']) < 1:
            flash("Invalid 2 characters required", "cheese")
            is_valid = False
        if len(data['vegetables']) < 1:
            flash("Invalid 2 characters required", "vegetables")
            is_valid = False
        if len(data['sauce']) < 1:
            flash("Invalid 2 characters required", "sauce")
            is_valid = False
        return is_valid