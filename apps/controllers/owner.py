# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, g, session, jsonify
from sqlalchemy import desc
from apps import app, db
from apps.kstime import kstime

from apps.models import *

from utils import get_user_id, get_tz_offset
from datetime import datetime, timedelta


@app.route('/owner/checkin', methods=['GET','POST'])
def checkin():
    quest_id = request.args.get('quest_id')

    quest = Quest.query.get(quest_id)
    quest.success = 1

    db.session.commit()

    return jsonify(suceess=200)
