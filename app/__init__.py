from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .db import db
from .configs import Config
from app.processes.hooks.error_handler import handleExceptions 
from app.processes.middlewares.current_user import CurrentUser 
from .routes.auth import auth
from .routes.papers import papers
from .routes.authors import authors

app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}},supports_credentials=True)

# setting up routes and blueprints
from .routes.index import index 
app.register_blueprint(auth)
app.register_blueprint(authors)
app.register_blueprint(papers)

# handling errors 
# app.register_error_handler(Exception, handleExceptions)

# setting global middlewares
app.wsgi_app = CurrentUser(app.wsgi_app)

# setting up db and migration
db.init_app(app=app)
migrate = Migrate(app, db)
