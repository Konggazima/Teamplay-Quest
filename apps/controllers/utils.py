# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, session, jsonify, g
from sqlalchemy import desc
from apps import app
from apps.kstime import kstime
from sqlalchemy.orm.exc import NoResultFound

from apps.models import *

def get_user_id_from_database(data):
    name = data['name']
    fb_id = data['fb_id']
    email = data['email']
    img_url= data['img_url']
    try:
        user_id = db.session.query(User.id).filter(User.fb_id == fb_id).one()
    except NoResultFound:
        user = User(
            name=name,
            email=email,
            fb_id=fb_id,
            img_url=img_url,
            date_created=kstime(0)
        )

        db.session.add(user)
        db.session.commit()
        user_id = user.id

    session.permanent = True
    session['user_id'] = user_id
    return user_id

def get_user_id():
    return session.get('user_id')

