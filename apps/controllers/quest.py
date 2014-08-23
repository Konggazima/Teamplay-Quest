# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, g, session
from sqlalchemy import desc
from apps import app, db
from apps.kstime import kstime

from apps.models import *

from apps.forms import QuestForm
from utils import get_user_id


@app.route('/quest/create', methods=['GET', 'POST'])
@app.route('/quest/create/', methods=['GET', 'POST'])
def create_quest():
    form = QuestForm(group_id=4)
    if request.method == 'GET':
        return render_template('quest/create.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            quest = Quest(
                title = form.title.data,
                category = form.category.data,
                description = form.description.data,
                group_id = form.group_id.data,
                date_created = kstime(0),
                date_expired = kstime(int(form.expired_date.data))
            )

            db.session.add(quest)
            db.session.commit()

            return redirect(url_for('list'))
        else:
            return render_template('quest/create.html', form=form)

@app.route('/quest/detail/<int:quest_id>', methods=['GET'])
def detail_quest(quest_id):
    quest = Quest.query.get(quest_id)

    users = db.session.query(User).join(Groupmember).filter(Groupmember.group_id == quest.group_id).all()

    return render_template('quest/detail.html', quest=quest, users=users)