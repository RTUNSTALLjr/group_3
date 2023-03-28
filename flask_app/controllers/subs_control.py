from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import user, order, sub
from flask_app.controllers import users_control, orders_control

# CLOUDINARAY
from dotenv import load_dotenv
load_dotenv()
import cloudinary
import cloudinary.uploader
import cloudinary.api

config = cloudinary.config(secure = True)


@app.route('/')
def dashboard():
    if "user_id" in session:
        user_info = user.User.get_user_by_id({'id' : session['user_id']})
        return render_template('dashboard.html', user = user_info)
    return render_template('dashboard.html')

@app.route('/menu')
def menu():
    menu_list = sub.Sub.get_all_subs()
    return render_template('menu.html', menu = menu_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/insert_sub', methods=['POST'])
def insert_sub():
    if sub.Sub.validate_sub(request.form):
        uploaded_img = request.files['image']

        name = request.form["name"]
        sub_data = {
            "name": name.replace(" ",""),
            "price": request.form["price"],
            "brief_description": request.form["brief_description"],
            "full_description": request.form["full_description"],
            "bread": request.form["bread"],
            "protein": request.form["protein"],
            "cheese": request.form["cheese"],
            "vegetables": request.form["vegetables"],
            "sauce": request.form["sauce"]
        }

        cloudinary.uploader.upload(uploaded_img, public_id=sub_data["name"], unique_filename=False, overwrite=True)
        srcURL = cloudinary.CloudinaryImage(sub_data["name"]).build_url()

        sub_data["img_url"] = srcURL

        print(sub_data)
        sub.Sub.save_sub(sub_data)

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
    if "user_id" in session and session['user_id'] == 1:
        return render_template('create_sub.html')
    return redirect('/')

@app.route('/edit_sub/<int:id>')
def edit_sub(id):
    if "user_id" in session and session['user_id'] == 1:
        sub_info = sub.Sub.get_sub_by_id({'id' : id})
        return render_template('edit_sub.html', sub = sub_info)
    return redirect("/")

@app.route('/update_sub/<int:id>', methods=["POST"])
def update_sub(id):
    if sub.Sub.validate_sub(request.form):
        uploaded_img = request.files['image']
        name = request.form["name"]
        sub_data = {
            "id": id,
            "name": name.replace(" ",""),
            "price": request.form["price"],
            "brief_description": request.form["brief_description"],
            "full_description": request.form["full_description"],
            "bread": request.form["bread"],
            "protein": request.form["protein"],
            "cheese": request.form["cheese"],
            "vegetables": request.form["vegetables"],
            "sauce": request.form["sauce"]
        }

        cloudinary.uploader.upload(uploaded_img, public_id=sub_data["name"], unique_filename=False, overwrite=True)
        srcURL = cloudinary.CloudinaryImage(sub_data["name"]).build_url()

        sub_data["img_url"] = srcURL
        sub.Sub.update_sub(sub_data)

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
        return redirect(f'/edit_sub/{id}')
    
@app.route("/delete_sub/<int:id>")
def delete_sub(id):
    if "user_id" in session and session['user_id'] == 1:
        sub.Sub.delete_sub({"id": id})
        return redirect("/menu")
    return redirect("/")