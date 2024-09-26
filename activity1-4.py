from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError, Email
from typing import Any, TypeVar, overload

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

# class ValidateUofTEmail:
#     def __init__(self, message=None):
#         self.message = message
        

#     def __call__(self, form, field):
#         if '@' not in field.data:
#             message = field.gettext(f"Please include an '@' in the email address. {field.data} is missing an '@'.")
#             raise ValidationError(message)


# Form definition
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email address?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')

        # Save name and email to session
        session['name'] = form.name.data
        session['email'] = form.email.data

        return redirect(url_for('index'))

    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))

