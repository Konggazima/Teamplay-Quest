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
    form = GroupForm()
    if request.method == 'GET':
        return render_template('group/create.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            group = Group(
                name = form.name.data,
                description = form.description.data,
                owner_id = g.user_id,
                date_created = kstime(0)
            )

            db.session.add(group)
            db.session.commit()

            return redirect(url_for('list'))
        else:
            return render_template('group/create.html', form=form)

