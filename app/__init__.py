from flask import Flask

app = Flask(__name__)

from routes import *
app.register_blueprint(routes)


if __name__ == "__main__":
    app.run(host="localhost", port="5000", debug=True)