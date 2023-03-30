from . import papers
from app.services.scraper import Scrapper 
from flask import request

@papers.route("/confirm-its-me")
def confirmItsMe():
    id = request.json["author_id"]
    target_name = request.json["target_name"]
    found_in_page = request.json["found_in_page"]

    author = Scrapper.getAuthorById(target_name, id, found_in_page)
    
    if author is None: raise Exception("Could not confirm it is you")

    
    pass;


