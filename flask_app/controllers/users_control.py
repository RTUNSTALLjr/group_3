from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import user, order, sub
from flask_app.controllers import subs_control, orders_control


# REGISTRATION
@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/customer/register', methods = ['POST'])
def register_user():
        if user.User.create_user(request.form):
            temp = session["user_id"]
            session.clear()
            session["user_id"] = temp
            return redirect('/')
        session["first_name"] = request.form["first_name"]
        session["last_name"] = request.form["last_name"]
        session["email"] = request.form["email"]
        return redirect('/registration')

# LOGIN
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/customer/login', methods=['POST'])
def user_login():
    if user.User.user_login(request.form):
        return redirect('/')
    return redirect('/login')


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")