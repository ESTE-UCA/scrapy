from . import authors
from app.services.scraper import Scrapper
from flask import request

@authors.route("/confirm-its-me")
def confirmItsMe():
    author_id = request.args.get["id"]
    searched_name = request.args.get["sname"]
    found_in_page = request.args.get("pg")

    author = Scrapper.getAuthorById(searched_name, author_id, found_in_page)

    