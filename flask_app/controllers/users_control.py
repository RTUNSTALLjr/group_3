from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import user, order, sub
from flask_app.controllers import subs_control, orders_control

@app.route('/login-register')
def login_register():
    return render_template('login_reg.html')

