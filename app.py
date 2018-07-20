from flask import (Flask, render_template,redirect, url_for)


import forms
import models
import datetime

app = Flask(__name__)
app.secret_key = 'auoesh.bouoastuh.43,uoausoehuosth3ououea.auoub!'



@app.route('/')
def index():
    todays_date = datetime.date.today().strftime('%d-%m-%Y')
    return render_template('index.html', date=todays_date)


@app.route('/entries')
def list():
    entries = models.Entry.select()
    return render_template('index.html', entries=entries)


@app.route('/entries/delete/<int:entry_id>/entry')
def delete(entry_id):
    entry = models.Entry.get(
        models.Entry.id == entry_id

    )
    entry.delete_instance()
    return redirect(url_for('list'))


@app.route('/detail/<int:entry_id>')
def detail(entry_id):
    entry = models.Entry.get(
        models.Entry.id == entry_id

    )
    return render_template('detail.html', entry=entry)


@app.route('/entry', methods=('GET', 'POST'))
@app.route('/entry<int:entry_id>', methods=('GET', 'POST'))
def add_edit_entry(entry_id=None):
    if entry_id:
        entry = models.Entry.get(
            models.Entry.id == entry_id)
        form = forms.EditForm()
        if form.validate_on_submit():
            query = (models.Entry
                 .update({models.Entry.title: form.title.data.strip(),
                          models.Entry.time_spent: form.time_spent.data,
                          models.Entry.date: form.date.data,
                          models.Entry.what_i_learned:form.what_i_learned.
                         data.strip(),
                          models.Entry.resources: form.resources.data.strip()})
                 .where(models.Entry.id == entry_id))
            query.execute()

            return redirect(url_for('detail', entry_id=entry_id))
        return render_template('edit.html', form=form, entry=entry)
    else:
        form = forms.EntryForm()
        if form.validate_on_submit():
            models.Entry.create(title=form.title.data.strip(),
                                date=form.date.data,
                                time_spent=form.time_spent.data,
                                what_i_learned=form.what_i_learned.
                                data.strip(),
                                resources=form.resources.data.strip()
                                )
            return redirect(url_for('index'))
        return render_template('new.html', form=form)


if __name__ == '__main__':
    models.initialize()
    app.run()
