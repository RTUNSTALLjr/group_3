from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import user, order, sub
from flask_app.controllers import subs_control, users_control

@app.route('/cart')
def cart():
    return render_template('checkout.html')

@app.route('/confirmation')
def order_confirm():
    return render_template('order_confirm.html')