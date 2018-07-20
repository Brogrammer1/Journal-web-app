from flask_wtf import Form

from wtforms import StringField, PasswordField, TextAreaField,BooleanField,IntegerField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)
import models

class EntryForm(Form):


    title = StringField(
        'title',
        validators=[
            DataRequired(),
        ])
    time_spent = IntegerField('time spend in minutes',validators=[
            DataRequired(),
        ])
    what_i_learned = TextAreaField('what you learned',validators=[
            DataRequired(),
        ])
    resources = TextAreaField('any Resources found out',validators=[
            DataRequired(),
        ])


class EditForm(Form):
    title = StringField(
        'title',
        validators=[
            DataRequired(),
        ])
    time_spent = IntegerField('time spend in minutes', validators=[
        DataRequired(),
    ])
    what_i_learned = TextAreaField('what you learned', validators=[
        DataRequired(),
    ])
    resources = TextAreaField('any Resources found out', validators=[
        DataRequired(),
    ])













