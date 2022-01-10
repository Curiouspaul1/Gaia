from flask import Blueprint

project = Blueprint(__name__, 'project', url_prefix='/project')

from . import views
