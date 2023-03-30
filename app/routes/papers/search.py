from . import papers
from app.services.scraper import Scrapper
from app.models import Paper
from flask import jsonify

@papers.route("/search", methods=["GET", "POST"])
def search():
    result = Scrapper.fetchPapers("development")
    serializedResult = []
    for paper in result:
        if isinstance(paper, Paper):
            serializedResult.append(paper.serialize())

    return {
        "count": len(serializedResult),
        "papers": serializedResult
    }
    # return serializedResult