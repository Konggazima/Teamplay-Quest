import os
from apps import app
from flask import request, redirect, url_for, session, g

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
        }
        session.update(data)

    g.user_id = None

    if 'user_id' in session:
        g.user_id = session['user_id']
    else :
        if request.endpoint != 'index' and request.endpoint != 'login':
            return redirect(url_for('index'))

    # if 'user_id' in session:
    #     g.user_id =
    #
    # if g.user_id == None :
