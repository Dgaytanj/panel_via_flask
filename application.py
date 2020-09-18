#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import panel as pn
from flask import Flask

flask_app = Flask(__name__)

@flask_app.route('/app')
def hello_world():
    return 'Hello, World!'
def panel_app():
    return pn.Column("# This Panel app runs alongside flask, access the flask app at [here](./flask/app)",pn.widgets.Select(options=['Africa', 'Asia', 'Europe'],value='Asia'))
pn.serve({'/flask': flask_app,'/app': panel_app}, port=5001)

