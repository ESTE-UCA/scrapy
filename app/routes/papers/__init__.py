from flask import Blueprint


papers = Blueprint("papers", __name__, url_prefix="/api/papers")

from .search import search
from .suspected_authors import suspectedAuthors