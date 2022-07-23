from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..models_py_file.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from flask_bcrypt import Bcrypt
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
bcrypt = Bcrypt()

auth = Blueprint('auth', __name__)

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Your Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Enter Your Password", "class": "password"})

    submit = SubmitField('Sign In')


@auth.route('/')
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist.', category='error')
    return render_template('logger/singin_form.html', form=form, user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successfully!', category='success')
    return redirect(url_for('auth.login'))






