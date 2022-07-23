from flask import Blueprint, render_template, request, flash, redirect, url_for
from .. import db
from flask_login import login_user, login_required, logout_user, current_user


req_dashboard = Blueprint('req_dashboard', __name__)


@req_dashboard.route('/reqdashboard', methods=['GET', 'POST'])
@login_required
def reqdashboard():
    return render_template('activitics_dashboard/req_dashboard.html')
