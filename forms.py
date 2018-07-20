from flask_wtf import Form

from wtforms import StringField, TextAreaField,  \
    IntegerField, DateField
from wtforms.validators import (DataRequired)


class EntryForm(Form):
    title = StringField(
        'title',
        validators=[
            DataRequired(),
        ])
    date = DateField('date in dd/mm/yyyy format', format='%d/%m/%Y')

    time_spent = IntegerField('time spend in minutes', validators=[
        DataRequired(),
    ])
    what_i_learned = TextAreaField('what you learned', validators=[
        DataRequired(),
    ])
    resources = TextAreaField('Any Resources found out')


class EditForm(Form):
    title = StringField(
        'title',
        validators=[
            DataRequired(),
        ])
    date = DateField('date in dd/mm/yyyy format', format='%d/%m/%Y'
                     )
    time_spent = IntegerField('time spend in minutes', validators=[
        DataRequired(),
    ])
    what_i_learned = TextAreaField('what you learned', validators=[
        DataRequired(),
    ])
    resources = TextAreaField('Any Resources learned')
