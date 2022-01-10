from flask import Flask
from dotenv import load_dotenv
import os

from flask.json import load

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('app-secret')
    app.config['PROJECTS_PER_PAGE'] = 10

    from .user import user
    from .projects import project
    app.register_blueprint(user)
    app.register_blueprint(project)

    return app
