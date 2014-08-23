import os
from apps import app
from flask import request, redirect, url_for, session, g
from utils import get_user_id_from_database, get_user_id

# @app.url_value_preprocessor
# def pull_lang_code(endpoint, values):
#     g.lang_code = values.pop('lang_code', None)
#     print g.lang_code

@app.before_request
def before_request():
    if os.environ.get('SERVER_NAME') == 'localhost':
        data = {
            'name' : 'somebody',
            'fb_id' : '00000000000',
            'email' : 'someone@some.one',
            'img_url' : ''
            'timezone_offset': '-540'
        }
        user_id = get_user_id_from_database(data)
        session.update(data)

    if get_user_id():
        if request.endpoint in ('index', 'login'):
            return redirect(url_for('list'))
    else :
        if request.endpoint in ('index', 'login'):
            pass
        else:
            return redirect(url_for('index'))
