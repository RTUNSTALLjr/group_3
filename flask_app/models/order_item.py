from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user,sub

db = 'sub_shop'


class Order_Items:
    def __init__(self,data):
        self.id = data['id']
        self.quantity = data['quantity']
        self.sub_id = data['sub_id']
        self.order_id = data['order_id']
        self.sub = None

    @classmethod
    def insert_order_items(query, data):
        query = '''
            INSERT INTO order_items (quantity, sub_id, order_id)
            VALUES (%(quantity)s, %(sub_id)s, %(order_id)s);
        '''
        connectToMySQL(db).query_db(query, data)

