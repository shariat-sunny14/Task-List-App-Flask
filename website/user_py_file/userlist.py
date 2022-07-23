from flask_bcrypt import generate_password_hash
from flask import current_app
import os
from flask_wtf.file import FileField
import uuid as uuid
from werkzeug.utils import secure_filename
from io import BytesIO
from cgitb import reset
from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file, Response
from ..models_py_file.models import User
from .. import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from flask_bcrypt import Bcrypt
from wtforms import StringField, IntegerField, PasswordField, SubmitField, Form, TextAreaField, SubmitField, validators
from wtforms.validators import InputRequired, Length, ValidationError
bcrypt = Bcrypt()


userlist = Blueprint('userlist', __name__)


class RegisterForm(FlaskForm):
    users_id = StringField(validators=[InputRequired()], render_kw={
                           "placeholder": "Enter Your User ID"})
    first_name = StringField(validators=[InputRequired()], render_kw={
                             "placeholder": "Enter Your First Name"})
    last_name = StringField(validators=[InputRequired()], render_kw={
                            "placeholder": "Enter Your Last Name"})
    username = StringField(validators=[InputRequired()], render_kw={
                           "placeholder": "Enter Your Username"})
    dept = StringField(render_kw={"placeholder": "Enter Your Dept."})
    email = StringField(validators=[InputRequired(), Length(
        min=8, max=40)], render_kw={"placeholder": "Enter Your Email"})
    address = StringField(render_kw={"placeholder": "Enter Your Address"})
    mobile_number = StringField(
        render_kw={"placeholder": "Enter Your Mobile Number"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={"placeholder": "Enter Your Password"})
    user_img = FileField()

    submit = SubmitField('Save')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


@userlist.route('/user_register', methods=['GET', 'POST'])
def user_register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)

        image = request.files['user_img']
        img_filename = secure_filename(image.filename)
        img = str(uuid.uuid1()) + "_" + img_filename

        saver = request.files['user_img']
        saver.save(os.path.join(current_app.root_path,
                   'static/user_image/', img))

        new_user = User(users_id=form.users_id.data, first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data,
                        dept=form.dept.data, email=form.email.data, address=form.address.data, mobile_number=form.mobile_number.data, password=hashed_password, user_img=img)

        db.session.add(new_user)
        db.session.commit()
        flash("User add has been successfully done!")
        return redirect(url_for('userlist.user'))

# update user
@userlist.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = User.query.get(request.form.get('id'))

        my_data.users_id = request.form['users_id']
        my_data.first_name = request.form['first_name']
        my_data.last_name = request.form['last_name']
        my_data.username = request.form['username']
        my_data.dept = request.form['dept']
        my_data.email = request.form['email']
        my_data.address = request.form['address']
        my_data.mobile_number = request.form['mobile_number']

        db.session.commit()
        flash("Data update has been successfully done!")
        return redirect(url_for('userlist.user'))


@userlist.route('/update/password', methods=['POST'])
def update_password():
    if request.method == 'POST':
        passw = User.query.get(request.form.get('id'))

        passw.password = generate_password_hash(request.form['password'])

        db.session.commit()
        flash("Password update has been successfully done!")
        return redirect(url_for('userlist.user'))

# delete User List
@userlist.route('/delete/<id>/')
def delete(id):
    my_data = User.query.get_or_404(id)
    try:
        os.unlink(os.path.join(current_app.root_path,
                  'static/user_image/' + my_data.user_img))
        db.session.delete(my_data)
    except:
        db.session.delete(my_data)
    db.session.commit()
    flash("User delete has been successfully done!")
    return redirect(url_for('userlist.user'))

# main host
@userlist.route('/user', methods=['GET', 'POST'])
# @login_required
def user():
    users_data = User.query.all()
    form = RegisterForm()
    return render_template('user_acc/user_list.html', users=users_data, form=form)
