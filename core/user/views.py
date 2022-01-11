from datetime import datetime
from . import user
from flask import request
from core.extensions import db
import uuid

@user.post('/')
def register():
    data = request.get_json(force=True)
    data['_id'] = str(uuid.uuid4())
    try:
        db.users.insert_one(data)
        return {
            'status': 'success',
            'data': data
        }, 200
    except Exception as e:
        print(e)
        return {
            'status': 'failed',
            'msg': 'Some error occurred'
        }, 500
    

@user.get('/<string:user_id>')
def fetch_details(user_id):
    try:
        user_ = db.users.find_one(filter={'_id': user_id})
        return {
            'status': 'success',
            'data': user_
        }
    except Exception as e:
        print(e)
        return {
            'status': 'failed',
            'msg': 'An error occurred'
        }, 500

@user.post('/donate')
def donate_callback():
    data = request.get_json(force=True)
    data['_id'] = str(uuid.uuid4())
    data['date_donated'] = datetime.utcnow()
    try:
        db.donations.insert_one(data)
        return {
            'status': 'success',
            'data': data
        }, 201
    except Exception as e:
        print(e)
        return {
            'status': 'failed',
            'msg': 'An error occurred'
        }, 500

@user.get('/donations')
def donations():
    user_id = request.args.get('user_id', type=str)
    print(user_id)
    try:
        donations_ = db.donations.find({"user_id":user_id})
        return {
            'status': 'success',
            'data': list(donations_)
        }, 200
    except Exception as e:
        print(e)
        return {
            'status': 'failed',
            'msg': 'An error occurred'
        }, 500
