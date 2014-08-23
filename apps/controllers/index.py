# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, session, jsonify, g
from sqlalchemy import desc
from apps import app
from apps.kstime import kstime
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

from apps.models import *


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    name = request.args.get('name')
    fb_id = request.args.get('fb_id')
    email = request.args.get('email')
    img_url = request.args.get('img_url')

    try:
        user_id = db.session.query(User.id).filter(User.fb_id == fb_id).one()
    except NoResultFound:
        user = User(
            name=name,
            email=email,
            fb_id=fb_id,
            img_url=img_url,
            date_created=kstime(9)
        )

        db.session.add(user)
        db.session.commit()
        user_id = db.session.query(User.id).filter(User.fb_id==fb_id).one()

    session.permanent = True
    session['user_id'] = user_id

    return jsonify(id=None)