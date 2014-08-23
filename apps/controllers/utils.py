# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, session, jsonify, g
from sqlalchemy import desc
from apps import app
from apps.kstime import kstime
from sqlalchemy.orm.exc import NoResultFound

from apps.models import *

from datetime import datetime

def get_user_id_from_database(data):
    name = data['name']
    fb_id = data['fb_id']
    email = data['email']
    img_url= data['img_url']
    timezone_offset = data['timezone_offset']
    try:
        user_id = db.session.query(User.id).filter(User.fb_id == fb_id).one()
    except NoResultFound:
        user = User(
            name=name,
            email=email,
            fb_id=fb_id,
            img_url=img_url,
            timezone_offset=timezone_offset,
            date_created=datetime.utcnow()
        )

        db.session.add(user)
        db.session.commit()
        user_id = user.id

    session.permanent = True
    session['user_id'] = user_id
    return user_id

def get_user_id():
    return session.get('user_id')

def get_tz_offset():
    user_id = get_user_id()
    try:
        offset, = db.session.query(User.timezone_offset).filter(
            User.id == user_id).one()
    except NoResultFound:
        offset = -540
    return offset
