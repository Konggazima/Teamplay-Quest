# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from apps import app, db

from apps.models import *

@app.route('/user', methods=['GET'])
@app.route('/user/', methods=['GET'])
@app.route('/user/<int:user_id>', methods=['GET'])
def user(user_id = None):
    if not user_id:
        # get user_id from session
        pass

    return render_template('user.html')
