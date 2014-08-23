# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from apps import app, db

from apps.models import *

@app.route('/group', methods=['GET', 'POST'])
@app.route('/group/', methods=['GET', 'POST'])
@app.route('/group/<int:group_id>', methods=['GET', 'POST'])
def group(group_id = 0):

    return render_template('group.html')

