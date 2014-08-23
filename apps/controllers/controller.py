# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from apps import app, db

from apps.models import *

@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():

    return render_template('create.html')

@app.route('/detail/<int:quest_id>', methods=['GET', 'POST'])
@app.route('/detail/<int:quest_id>/', methods=['GET', 'POST'])
@app.route('/detail/<int:quest_id>/<int:user_id>', methods=['GET', 'POST'])
def detail(quest_id, user_id = None):

    return render_template('detail.html')

@app.route('/list', methods=['GET'])
@app.route('/list/', methods=['GET'])
@app.route('/list/<mode>', methods=['GET'])
@app.route('/list/<mode>/', methods=['GET'])
@app.route('/list/<mode>/<int:page>', methods=['GET'])
def list(mode = 'joined', page = 0):
    assert(mode in ('joined', 'created'))
    return render_template('list.html')

@app.route('/manage/<int:quest_id>', methods=['GET', 'POST'])
def manage(quest_id):

    return render_template('manage.html')

@app.route('/user', methods=['GET'])
@app.route('/user/', methods=['GET'])
@app.route('/user/<int:user_id>', methods=['GET'])
def user(user_id = None):
    if not user_id:
        # get user_id from session
        pass

    return render_template('user.html')
