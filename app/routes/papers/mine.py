from app.processes.decorators.require_author_confirmation import require_author_confirmation
from app.processes.decorators.require_auth import require_authentication
from flask import request,jsonify
from app.repositories.author_repo import AuthorRepository as AuthorRepo
from app.services.scraper import Scrapper
from . import papers
from app.types.fullname import FullName

@papers.route('/mine', methods=["GET"])
@require_authentication
@require_author_confirmation
def myPapers():
    currentuser = request.environ["currentuser"]
    # show more counter
    smc=request.args.get("smc")


    if smc is not None:
        smc = int(smc)
    # author = AuthorRepo.getAuthorById(currentuser["authorId"])
    authorName = FullName.fromOriginJson(currentuser["fullName"])
    
    papers = Scrapper.getPapersOfAuthor(authorName, smc)
    serPapers = [paper.serialize() for paper in papers] if papers is not None else []

    return {
        "count": serPapers.__len__(),
        "papers": serPapers
    }