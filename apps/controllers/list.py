# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from apps import app, db

from apps.models import *

@app.route('/list', methods=['GET'])
@app.route('/list/', methods=['GET'])
# @app.route('/list/<mode>', methods=['GET'])
# @app.route('/list/<mode>/', methods=['GET'])
# @app.route('/list/<mode>/<int:page>', methods=['GET'])
# def list(mode = 'joined', page = 0):
def list():
    # assert(mode in ('joined', 'created'))

    quests = Quest.query.all()

    return render_template('list.html', quests=quests)
