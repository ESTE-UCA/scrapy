from flask import Blueprint

authors = Blueprint("authors", __name__, url_prefix="/api/authors")

from .confirm_its_me import confirmItsMe
from .suspected import suspectedAuthors
from .add_laboratory_author import addLaboratoryAuthor