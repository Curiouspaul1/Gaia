from . import project
from flask import request, current_app
from core.extensions import db

@project.get('/')
def fetch_projects():
    page_no = request.args.get('page', 1, type=int)
    projects_ = list(db.projects.find({}))
    per_page = current_app.config['PROJECTS_PER_PAGE']
    return {
        'status': 'success',
        'data': projects_[(per_page*page_no)-per_page:(per_page*page_no)]
    }, 200


