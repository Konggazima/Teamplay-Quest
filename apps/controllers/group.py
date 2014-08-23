# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, g, session
from sqlalchemy import desc
from apps import app, db
from apps.kstime import kstime

from apps.models import *

from apps.forms import GroupForm

@app.route('/group', methods=['GET', 'POST'])
@app.route('/group/', methods=['GET', 'POST'])
@app.route('/group/<int:group_id>', methods=['GET', 'POST'])
def group(group_id = 0):

    return render_template('group.html')



@app.route('/group/create', methods=['GET', 'POST'])
def create_group():
    form = GroupForm()
    if request.method == 'GET':
        users = User.query.filter(User.id != g.user_id)

        return render_template('group/create.html', form=form, users=users)
    elif request.method == 'POST':
        if form.validate_on_submit():
            group = Group(
                name = form.name.data,
                owner_id = g.user_id,
                date_created = kstime(0)
            )

            db.session.add(group)
            db.session.commit()

            return redirect(url_for('list'))
        else:
            return render_template('group/create.html', form=form)


