# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from apps import app, db

from apps.models import *

@app.route('/create', methods=['GET', 'POST'])
def create():

    return render_template('create.html')

