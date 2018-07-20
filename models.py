import datetime

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('Journal.db')



class Entry(Model):
    title = CharField()
    date = DateTimeField(default = datetime.datetime.now)
    time_spent = IntegerField()
    what_i_learned = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-date',)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()