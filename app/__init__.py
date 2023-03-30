from flask import Flask
from flask_migrate import Migrate
from .db import db
from .configs import Config
from .processes.middlewares.error_handler import handleExceptions 
from .processes.middlewares.current_user import CurrentUser 
from .routes.auth import auth
from .routes.papers import papers

app = Flask(__name__)
app.config.from_object(Config)

# setting up routes and blueprints
from .routes.index import index 
app.register_blueprint(auth)
app.register_blueprint(papers)

# handling errors 
app.register_error_handler(Exception, handleExceptions)

# setting global middlewares
app.wsgi_app = CurrentUser(app.wsgi_app)

# setting up db and migration
db.init_app(app=app)
migrate = Migrate(app, db)
