from functools import wraps
from flask import request
from app.services.scraper import Scrapper

def suspected_author(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        author_id = request.args.get("id")
        searched_name = request.args.get("name")
        found_in_page = request.args.get("pg")

        suspected = Scrapper.getAuthorById(searched_name, author_id, found_in_page)

        if suspected is None:
            raise Exception("unexpected error occurred searching for the author")

        return f(suspected, *args, **kwargs)
    return decorator