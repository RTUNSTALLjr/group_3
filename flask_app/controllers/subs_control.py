from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import user, order, sub
from flask_app.controllers import users_control, orders_control

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/insert_sub', methods=['POST'])
def insert_sub():
    print('AAAAAAAAAAAAAAAAAAAAAA')
    if sub.Sub.validate_sub(request.form):
        sub.Sub.save_sub(request.form)
        temp = session["user_id"]
        session.clear()
        session["user_id"] = temp
        return redirect('/menu')
    else :
        session["name"] = request.form["name"]
        session["price"] = request.form["price"]
        session["brief_description"] = request.form["brief_description"]
        session["full_description"] = request.form["full_description"]
        session["bread"] = request.form["bread"]
        session["protein"] = request.form["protein"]
        session["cheese"] = request.form["cheese"]
        session["vegetables"] = request.form["vegetables"]
        session["sauce"] = request.form["sauce"]
        return redirect('/create_sub')

@app.route('/create_sub')
def create_sub():
    print('BBBBBBBBBBBBBBBBBBBBBB')
    #if session["user_id"] ==1:
    # add conditional check to protect route for sub shop owner
    return render_template('create_sub.html')
    #else:
        #return redirect('/menu')

@app.route('/edit_sub')
def edit_sub():
    # add conditional check to protect route for sub shop owner
    return render_template('edit_sub.html')
