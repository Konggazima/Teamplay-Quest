# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from apps import app, db

from apps.models import *

@app.route('/manage/<int:quest_id>', methods=['GET', 'POST'])
def manage(quest_id):

    return render_template('manage.html')
