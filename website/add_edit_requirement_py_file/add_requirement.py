from flask import Blueprint, render_template, request, flash, redirect, url_for
from .. import db
from flask_login import login_required
from ..models_py_file.models import Registration_table, Prescription_table
from flask_wtf import FlaskForm
from flask_bcrypt import Bcrypt
from wtforms import StringField, IntegerField, PasswordField, SubmitField, Form, TextAreaField, RadioField, SelectField, TimeField, SelectMultipleField, DateField, BooleanField, validators
from wtforms.validators import InputRequired, Length, ValidationError

add_requirement = Blueprint('add_requirement', __name__)


class RequirementsData(FlaskForm):
    work_des = TextAreaField(validators=[InputRequired()], render_kw={
                             "class": "work_des-textarea", "placeholder": "Enter Your Work Description Here"})
    req_by = StringField(validators=[Length(max=30)], render_kw={
                         "placeholder": "Enter Your First Name"})
    req_type = SelectField(u'status', validators=[InputRequired()], choices=[
                           ('New Req.', 'New Req.'), ('Bugs', 'Bugs')])
    status = SelectField(u'status', choices=[('Pending', 'Pending'), (
        'Done', 'Done'), ('Not Done', 'Not Done'), ('Half Done', 'Half Done')])
    priority = SelectField(u'priority', choices=[('Very High', 'Very High'), (
        'High', 'High'), ('Medium', 'Medium'), ('Low', 'Low'), ('Very Low', 'Half Done')])
    dev_status = SelectField(u'dev_status', choices=[('Pending', 'Pending'), (
        'Done', 'Done'), ('Not Done', 'Not Done'), ('Half Done', 'Half Done')])
    qa_status = SelectField(u'qa_status', choices=[('Pending', 'Pending'), (
        'Done', 'Done'), ('Not Done', 'Not Done'), ('Half Done', 'Half Done')])
    assigned_to = StringField(validators=[Length(max=30)], render_kw={
                              "placeholder": "Enter Your Address"})
    hours = StringField(render_kw={"placeholder": "Enter Your Password"})
    req_date = DateField(format('d-m-Y'))
    start_date = StringField()
    end_date = StringField()
    comments = TextAreaField(validators=[Length(max=500)], render_kw={
        "class": "comments-textarea", "placeholder": "Confirm Your Password"})
    referance = TextAreaField(validators=[Length(max=50)], render_kw={
        "class": "referance-textarea", "placeholder": "Confirm Your Password"})
    submit = SubmitField('Save')

# ======================  registration ==================
# registration start
@add_requirement.route('/add/registration/data', methods=['GET', 'POST'])
def add_registration_data():
    form = RequirementsData()
    if form.validate_on_submit():
        new_add = Registration_table(work_des=form.work_des.data, req_by=form.req_by.data, req_type=form.req_type.data, status=form.status.data, priority=form.priority.data,
                                     dev_status=form.dev_status.data, qa_status=form.qa_status.data, assigned_to=form.assigned_to.data, hours=form.hours.data,
                                     start_date=form.start_date.data, end_date=form.end_date.data, comments=form.comments.data, referance=form.referance.data)
        db.session.add(new_add)
        db.session.commit()
        flash("Successfully Requirement Added")
        return redirect(url_for('add_requirement.requirement'))

# edit id data
@add_requirement.route('/update/id/registration/data', methods=['GET', 'POST'])
def update_id_registration_data():
    if request.method == 'POST':
        id_data = Registration_table.query.get(request.form.get('id'))
        id_data.id = request.form['id']
        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit work_des data
@add_requirement.route('/update/work_des/registration/data', methods=['GET', 'POST'])
def update_work_des_registration_data():
    if request.method == 'POST':
        data = Registration_table.query.get(request.form.get('id'))
        data.work_des = request.form['work_des']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit req. by data
@add_requirement.route('/update/req_by/registration/data', methods=['GET', 'POST'])
def update_req_by_registration_data():
    if request.method == 'POST':
        req_by_data = Registration_table.query.get(request.form.get('id'))
        req_by_data.req_by = request.form['req_by']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit req_type data
@add_requirement.route('/update/req_type/registration/data', methods=['GET', 'POST'])
def update_req_type_registration_data():
    if request.method == 'POST':
        req_type_data = Registration_table.query.get(request.form.get('id'))
        req_type_data.req_type = request.form['req_type']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit status data
@add_requirement.route('/update/status/registration/data', methods=['GET', 'POST'])
def update_status_registration_data():
    if request.method == 'POST':
        status_data = Registration_table.query.get(request.form.get('id'))
        status_data.status = request.form['status']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit priority data
@add_requirement.route('/update/priority/registration/data', methods=['GET', 'POST'])
def update_priority_registration_data():
    if request.method == 'POST':
        priority_data = Registration_table.query.get(request.form.get('id'))
        priority_data.priority = request.form['priority']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit dev_status data
@add_requirement.route('/update/dev_status/registration/data', methods=['GET', 'POST'])
def update_dev_status_registration_data():
    if request.method == 'POST':
        dev_status_data = Registration_table.query.get(request.form.get('id'))
        dev_status_data.dev_status = request.form['dev_status']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit qa_status data
@add_requirement.route('/update/qa_status/registration/data', methods=['GET', 'POST'])
def update_qa_status_registration_data():
    if request.method == 'POST':
        qa_status_data = Registration_table.query.get(request.form.get('id'))
        qa_status_data.qa_status = request.form['qa_status']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit assigned_to data
@add_requirement.route('/update/assigned_to/registration/data', methods=['GET', 'POST'])
def update_assigned_to_registration_data():
    if request.method == 'POST':
        assigned_to_data = Registration_table.query.get(request.form.get('id'))
        assigned_to_data.assigned_to = request.form['assigned_to']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit hours data
@add_requirement.route('/update/hours/registration/data', methods=['GET', 'POST'])
def update_hours_registration_data():
    if request.method == 'POST':
        hours_data = Registration_table.query.get(request.form.get('id'))
        hours_data.hours = request.form['hours']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit start_date data
@add_requirement.route('/update/start_date/registration/data', methods=['GET', 'POST'])
def update_start_date_registration_data():
    if request.method == 'POST':
        start_date_data = Registration_table.query.get(request.form.get('id'))
        start_date_data.start_date = request.form['start_date']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit end_date data
@add_requirement.route('/update/end_date/registration/data', methods=['GET', 'POST'])
def update_end_date_registration_data():
    if request.method == 'POST':
        end_date_data = Registration_table.query.get(request.form.get('id'))
        end_date_data.end_date = request.form['end_date']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit comments data
@add_requirement.route('/update/comments/registration/data', methods=['GET', 'POST'])
def update_comments_registration_data():
    if request.method == 'POST':
        comments_data = Registration_table.query.get(request.form.get('id'))
        comments_data.comments = request.form['comments']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))

# edit referance data
@add_requirement.route('/update/referance/registration/data', methods=['GET', 'POST'])
def update_referance_registration_data():
    if request.method == 'POST':
        referance_data = Registration_table.query.get(request.form.get('id'))
        referance_data.referance = request.form['referance']

        db.session.commit()
        flash("User Data Updated Successfully")
        return redirect(url_for('add_requirement.requirement'))


# registration data delete
@add_requirement.route('/registration/delete/<id>/', methods=['GET', 'POST'])
def registration_data_delete(id):
    del_reg_data = Registration_table.query.get(id)
    db.session.delete(del_reg_data)
    db.session.commit()
    flash("Requirement Deleted Successfully")
    return redirect(url_for('add_requirement.requirement'))
# registration end


# ======================  prescription ==================
# prescription start
@add_requirement.route('/add/prescription/data', methods=['GET', 'POST'])
def add_prescription_data():
    form = RequirementsData()
    if form.validate_on_submit():
        new_add = Prescription_table(work_des=form.work_des.data, req_by=form.req_by.data, req_type=form.req_type.data, status=form.status.data, priority=form.priority.data,
                                     dev_status=form.dev_status.data, qa_status=form.qa_status.data, assigned_to=form.assigned_to.data, hours=form.hours.data,
                                     start_date=form.start_date.data, end_date=form.end_date.data, comments=form.comments.data, referance=form.referance.data)
        db.session.add(new_add)
        db.session.commit()
        flash("Requirement Added Successfully")
        return redirect(url_for('add_requirement.requirement'))

# prescription data delete
@add_requirement.route('/prescription/delete/<id>/', methods=['GET', 'POST'])
def prescription_data_delete(id):
    del_pres_data = Prescription_table.query.get(id)
    db.session.delete(del_pres_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('add_requirement.requirement'))
# prescription end


# =====================  Main route =====================
@add_requirement.route('/requirement', methods=['GET', 'POST'])
@login_required
def requirement():
    form = RequirementsData()
    registration_data = Registration_table.query.all()
    prescription_data = Prescription_table.query.all()
    return render_template('requirements_list/add_requirement.html', registration=registration_data, prescription=prescription_data, form=form)
