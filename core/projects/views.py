from . import project
from flask import request, current_app
from core.extensions import db
import uuid
import datetime

@project.get('/')
def fetch_projects():
    page_no = request.args.get('page', 1, type=int)
    projects_ = list(db.projects.find({}))
    per_page = current_app.config['PROJECTS_PER_PAGE']
    return {
        'status': 'success',
        'data': projects_[(per_page*page_no)-per_page:(per_page*page_no)]
    }, 200


@project.get('/')
def fetch_project():
    id_ = request.args.get('pid', type=str)
    # find document
    try:
        doc_ = db.project.find_one(id_)
        return {
            'status': 'success',
            'data': doc_
        }, 200
    except Exception as e:
        print(e)
        return {
            'status': 'failed',
            'msg': 'some error occurred'
        }, 500


@project.post('/')
def register():
    data = request.get_json(force=True)
    # add id
    data['_id'] = str(uuid.uuid4())
    data['signup-date'] = datetime.datetime.utcnow()
    try:
        db.project.insert_one(data)
        return {
            'status': 'success',
            'data': data
        }, 201
    except Exception as e:
        print(e)
        return {
            'status': 'failed',
            'msg': 'Some error occurred while trying to add the new'
        }
