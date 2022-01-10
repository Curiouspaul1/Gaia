from . import project
from flask import request, current_app
from core.extensions import db
from core import projects

@project.get('/')
def fetch_projects():
    page_no = request.args.get('page', 1, type=int)
    projects_ = db.projects.find({})
    per_page = current_app['PROJECTS_PER_PAGE']
    return projects[(per_page*page_no)-per_page:(per_page*page_no)]
    
