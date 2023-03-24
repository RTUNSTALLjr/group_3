from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import user, order, sub
from flask_app.controllers import subs_control, orders_control

@app.route('/customer/register', methods = ['POST'])
def register_user():
        if user.User.create_user(request.form):
            return redirect('/')
        return redirect('/registration')
@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/customer/login', methods=['POST'])
def user_login():
    if user.User.user_login(request.form):
        return redirect('/')
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

