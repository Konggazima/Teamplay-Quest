# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from apps import app, db

from apps.models import (
    Article,
    Comment
)

@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')
