from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import user, order, sub
from flask_app.controllers import subs_control, users_control
from datetime import datetime, timedelta


@app.route("/sub_add/<name>/<float:price>", methods=["POST"])
def add_sub(name, price):
    # check if first time adding to sub_list
    if "sub_list" not in session:
        sub_list = []
    # if 2+ time, replace local sub_list with previous session addition
    else:
        sub_list = session["sub_list"]
    
    # create data dict with sub info
    sub_data = {
        "name": name,
        "price": price,
        "quantity": int(request.form["quantity"])
    }      

    # add sub info to the local sub_list variable
    increment_flag = False
    for subs in sub_list:
        if subs["name"] == sub_data["name"]:
            subs["quantity"] += sub_data["quantity"]
            increment_flag = True
    if increment_flag == False:
        sub_list.append(sub_data)
    # set the growing sub_list variable to session
    session["sub_list"] = sub_list

    subtotal = 0
    for each in sub_list:
        subtotal += (each["price"] * each["quantity"])
    session["subtotal"] = subtotal

    # create flash message to show user order added
    flash(f"{sub_data['name']} added!", "sub")
    return redirect("/menu")

@app.route('/remove/<name>/<page>')
def remove_from_cart(name, page):
    banana = session['sub_list']
    for i in range(len(session['sub_list'])):
        if session['sub_list'][i]['name'] == name:
            banana.pop(i)
            break
    session['sub_list'] = banana
    subtotal = 0
    for each in banana:
        subtotal += (each["price"] * each["quantity"])
    session["subtotal"] = subtotal
    if page == 'menu':
        return redirect('/menu')
    return redirect('/cart')

@app.route('/cart')
def cart():
    if "user_id" in session:
        user_info = user.User.get_user_by_id({'id': session['user_id']})
        pu_time = datetime.now() + timedelta(minutes=20)
        current_time = pu_time.strftime("%H:%M")
        return render_template('checkout.html', time=current_time, user = user_info)
    pu_time = datetime.now() + timedelta(minutes=20)
    current_time = pu_time.strftime("%H:%M")
    return render_template('checkout.html', time=current_time)
    

@app.route('/create_order', methods=['POST'])
def create_order():
    order_data = {
        'price' : session['subtotal'],
        'pickup_time' : request.form['pickup_time'],
        'status' : 'pending',
        
    }
    if 'user_id' in session:
        order_data['user_id'] = session["user_id"]
    return redirect('/confirmation')

@app.route('/confirmation')
def order_confirm():
    return render_template('order_confirm.html')
