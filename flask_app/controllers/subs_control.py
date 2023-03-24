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

@app.route('/create_sub')
def create_sub():
    # add conditional check to protect route for sub shop owner
    return render_template('create_sub.html')

@app.route('/edit_sub')
def edit_sub():
    # add conditional check to protect route for sub shop owner
    return render_template('edit_sub.html')
