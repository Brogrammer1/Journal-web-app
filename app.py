from flask import (Flask, g, render_template, flash, redirect, url_for,
                  abort)
from flask_bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, logout_user,
                             login_required, current_user)

import forms
import models


app = Flask(__name__)
app.secret_key = 'auoesh.bouoastuh.43,uoausoehuosth3ououea.auoub!'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.route('/')
def index():
    entries = models.Entry.select()
    return render_template('index.html',entries= entries)

@app.route('/detail/<int:entry_id>')
def detail(entry_id):
    # Do something with page_id
    entry = models.Entry.get(
        models.Entry.id == entry_id

    )
    return render_template('detail.html', entry= entry)

@app.route('/entry', methods=('GET', 'POST'))
@app.route('/entry<int:entry_id>', methods=('GET', 'POST'))
def new_entry(entry_id = None):
    if entry_id:
        entry = models.Entry.get(
            models.Entry.id == entry_id)
        form = forms.EditForm()
        if form.validate_on_submit():
            q = (models.Entry
                 .update({models.Entry.title:form.title.data.strip(),
                          models.Entry.time_spent: form.time_spent.data,
                          models.Entry.what_i_learned: form.what_i_learned.data.strip(),
                          models.Entry.resources: form.resources.data.strip()})
                 .where(models.Entry.id == entry_id))
            q.execute()  # Execute the query, returning number of rows updated.

            return redirect(url_for('detail', entry_id = entry_id))
        return render_template('edit.html', form=form, entry = entry)
    else:
        form = forms.EntryForm()
        if form.validate_on_submit():
            models.Entry.create(title=form.title.data.strip(),
                               time_spent=form.time_spent.data,
                               what_i_learned=form.what_i_learned.data.strip(),
                               resources=form.resources.data.strip()
                              )
            return redirect(url_for('index'))
        return render_template('new.html', form=form)



if __name__ == '__main__':
    models.initialize()
    app.run()