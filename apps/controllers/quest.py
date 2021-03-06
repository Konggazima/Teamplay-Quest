# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, g, session
from sqlalchemy import desc
from apps import app, db
from apps.kstime import kstime

from apps.models import *

from apps.forms import QuestForm
from utils import get_user_id, get_tz_offset
from datetime import datetime, timedelta


# @app.route('/quest', methods=['GET'])
@app.route('/quest/<int:group_id>', methods=['GET'])
def quest(group_id):
    quests = Quest.query.filter(Quest.group_id == group_id)

    return render_template('quest/list.html', quests=quests)


@app.route('/quest/create', methods=['GET', 'POST'])
@app.route('/quest/create/', methods=['GET', 'POST'])
def create_quest():
    form = QuestForm(group_id=4)
    if request.method == 'GET':
        members = db.session.query(User).join(Groupmember).filter(Groupmember.group_id == 4)

        return render_template('quest/create.html', form=form, members=members)
    elif request.method == 'POST':
        if form.validate_on_submit():
            now = datetime.utcnow()
            date_str = map(int, request.form['date_expired'].split('/'))
            expired = datetime(*date_str) + timedelta(minutes = get_tz_offset())
            quest = Quest(
                title = form.title.data,
                category = form.category.data,
                description = form.description.data,
                group_id = form.group_id.data,
                date_created = now,
                date_expired = expired)

            db.session.add(quest)
            db.session.commit()

            return redirect(url_for('detail_quest', quest_id = quest.id))
        else:
            members = db.session.query(User).join(Groupmember).filter(Groupmember.group_id == 4)

            return render_template('quest/create.html', form=form, members=members)


@app.route('/quest/detail/<int:quest_id>', methods=['GET'])
def detail_quest(quest_id):
    quest = Quest.query.get(quest_id)

    user_id = get_user_id()[0]
    group = Group.query.get(quest.group_id)
    owner_id = group.owner_id

    users = db.session.query(User).join(Questmember).filter(Questmember.quest_id == quest.id)
    d = quest.date_expired - timedelta(minutes = get_tz_offset())
    date_expired = '%d/%d/%d %d:%d'%(d.year, d.month, d.day, d.hour, d.minute)

    return render_template('quest/detail.html', quest=quest, users=users, user_id=user_id, owner_id=owner_id, date_expired = date_expired)