# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import desc
from apps import app, db

from apps.models import *

@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@app.route('/create', methods=['GET'])
def create():

    return render_template('create.html')

@app.route('/detail', methods=['GET'])
def detail():

    return render_template('detail.html')

@app.route('/list', methods=['GET'])
def list():

    return render_template('list.html')

@app.route('/manage', methods=['GET'])
def manage():

    return render_template('manage.html')

@app.route('/review', methods=['GET'])
def review():

    return render_template('review.html')

@app.route('/user', methods=['GET'])
def user():

    return render_template('user.html')
