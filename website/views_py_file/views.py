from flask import Flask, Blueprint, render_template, request, app, redirect, url_for, g, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import json
from ..models_py_file.models import User
from flask import Response
from flask_cors import CORS

views = Blueprint('views', __name__)

@views.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('main_dashboard/main_dashboard.html')
