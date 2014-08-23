# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from apps import app, db

from apps.models import *

@app.route('/detail/<int:quest_id>', methods=['GET', 'POST'])
@app.route('/detail/<int:quest_id>/', methods=['GET', 'POST'])
@app.route('/detail/<int:quest_id>/<int:user_id>', methods=['GET', 'POST'])
def detail(quest_id, user_id = None):

    return render_template('detail.html')

