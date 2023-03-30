from flask import Blueprint

authors = Blueprint("authors", __name__, url_prefix="/api/authors")

