from . import papers
from app.services.scraper import Scrapper
from app.models import Paper
from flask import request
from app.constants.sort_by_filter import SortByFilter

@papers.route("/search", methods=["GET", "POST"])
def search():
    q = request.args.get("q")
    sortBy = request.args.get("sort")
    pg = request.args.get("pg")

    papers = Scrapper.fetchPapers(q,pg,sort_by=SortByFilter(sortBy.lower()))
    serialized = [paper.serialize() for paper in papers] if papers is not None else []

    return {
        "count": len(serialized),
        "papers": serialized
    }
    # return serializedResult