from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user,sub, order_item

db = 'sub_shop'


class Orders:
    def __init__(self,data):
        self.id = data['id']
        self.price = data['price']
        self.pickup_time = data['pickup_time']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.order_items = []

    @classmethod
    def get_all_orders(cls,data):
        query = "SELECT * FROM orders;"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_order_by_id(cls,data):
        query = """
            SELECT * FROM orders O 
            LEFT JOIN order_items OI ON O.id = OI.order_id
            LEFT JOIN subs S ON OI.sub_id = S.id
            WHERE O.id = %(id)s;
        """
        results= connectToMySQL(db).query_db(query,data)
        order_object =  cls(results[0])
        order_items_list = []
        for row in results:
            order_items_data ={
                "id" : row['OI.id'],
                "quantity" : row['quantity'],
                "sub_id" : row['sub_id'],
                "order_id" :row['order_id']
            }
            order_items_object = order_item.Order_Items(order_items_data)
            sub_data={
                "id" :row['S.id'],
                "name":row['name'],
                "price" :row['S.price'],
                "brief_description":row['brief_description'],
                "full_description":row['full_description'],
                "img_url":row['img_url'],
                "bread":row['bread'],
                "protein":row['protein'],
                "cheese":row['cheese'],
                "vegetables":row['vegetables'],
                "sauce":row['sauce'],
                'created_at':row['S.created_at'],
                "updated_at":row['S.updated_at']
            }
            sub_object = sub.Sub(sub_data)
            order_items_object.sub = sub_object
            order_items_list.append(order_items_object)
        order_object.order_items = order_items_list
        return order_object
    
    @classmethod
    def insert_order(query, data):
        query = '''
            INSERT INTO orders (price, pickup_time, status, user_id)
            VALUES (%(price)s, %(pickup_time)s, %(status)s, %(user_id)s);
        '''
        return connectToMySQL(db).query_db(query, data)