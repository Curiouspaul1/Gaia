from flask import Flask
from dotenv import load_dotenv
import os

from flask.json import load
from .extensions import cors

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('app-secret')
    app.config['PROJECTS_PER_PAGE'] = 20

    cors.init_app(app)

    from core.user import user
    from core.projects import project
    app.register_blueprint(user)
    app.register_blueprint(project)

    return app
