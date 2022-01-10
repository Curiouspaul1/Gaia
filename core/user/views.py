from . import user
from flask import request
from core.extensions import db

@user.post('/')
def register():
    data = request.get_json(force=True)
    # db

@user.get('/')
def fetch_details():
    pass

@user.post('/donate')
def donate_callback():
    pass