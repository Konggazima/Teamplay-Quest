# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, session, jsonify, g
from sqlalchemy import desc
from apps import app
from apps.kstime import kstime
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

from apps.models import *
from utils import get_user_id, get_user_id_from_database


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    user_id = get_user_id_from_database(request.args)
    return jsonify(id=None)
