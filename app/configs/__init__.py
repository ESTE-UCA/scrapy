import os

basedir = os.path.abspath(os.path.dirname(__file__))
database_dir = os.path.normpath(os.path.join(basedir, os.pardir, 'db', 'app.db'))

class Config(object):
    SECRET_KEY= os.environ.get("SECRET_KEY") or "SUPPOSED_TO_BE_TOP_SECRET"
    USER_TOKEN_KEY = os.environ.get('USER_TOKEN_KEY') or "user_token"
    SALT_PREFIX = os.environ.get('SALT_PREFIX') or "PaSsSaLT:"
    JWT_KEY = os.environ.get('JWT_KEY') or "SUPPOSED_TO_BE_SECRET"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + database_dir
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS_PAYLOADS = os.environ.get("ADMINS_PAYLOADS") or [{"email": "admin@test.com", "id": "7e462ca4-4d6a-444e-b2ea-ab124a7d6f06"}].__str__()

