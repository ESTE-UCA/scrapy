from app.services.scraper import Scrapper
from . import papers

@papers.route("suspected-authors", methods=["GET", "POST"])
def suspectedAuthors():
    result = Scrapper.getSuspectedAuthors("elmahdi erraji")
    if result is None:
        return {
            "message": "no result was found"
        }

    serAuthors = []
    for author in result:
        serAuthors.append(author.serialize())

    return {
        "suspected_authors": serAuthors
    }