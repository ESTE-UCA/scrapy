from werkzeug.wrappers import Request
import jwt
from app.configs import Config

class CurrentUser:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ=environ)
        userToken = req.cookies.get(Config.USER_TOKEN_KEY)
        try:
            payload = jwt.decode(jwt=userToken,key=Config.JWT_KEY, algorithms=["HS256"])
            environ["currentuser"] = payload
        except:
            environ["currentuser"] = None

        return self.app(environ, start_response)


        