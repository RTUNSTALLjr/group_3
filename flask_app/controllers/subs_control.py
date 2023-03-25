from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import user, order, sub
from flask_app.controllers import users_control, orders_control

@app.route('/')
def dashboard():
    if "user_id" in session:
        user_info = user.User.get_user_by_id({'id' : session['user_id']})
        return render_template('dashboard.html', user = user_info)
    return render_template('dashboard.html')

@app.route('/menu')
def menu():
    if "user_id" in session:
        menu_list = sub.Sub.get_all_subs()
        user_info = user.User.get_user_by_id({'id' : session['user_id']})
        return render_template('menu.html', user = user_info, menu = menu_list)
    menu_list = sub.Sub.get_all_subs()
    return render_template('menu.html', menu = menu_list)

@app.route('/about')
def about():
    if "user_id" in session:
        user_info = user.User.get_user_by_id({'id' : session['user_id']})
        return render_template('about.html', user = user_info)
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
    if "user_id" in session and session['user_id'] == 1:
        user_info = user.User.get_user_by_id({'id' : session['user_id']})
        return render_template('create_sub.html', user = user_info)
    # Change line 59 to redirect
    return render_template('create_sub.html')

@app.route('/edit_sub/<int:id>')
def edit_sub(id):
    if "user_id" in session and session['user_id'] == 1:
        user_info = user.User.get_user_by_id({'id' : session['user_id']})
        sub_info = sub.Sub.get_sub_by_id({'id' : id})
        return render_template('edit_sub.html', user = user_info, sub = sub_info)
    # change line 70 to redirect
    return render_template('edit_sub.html')
