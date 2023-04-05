from . import authors
from app.services.scraper import Scrapper
from flask import request
from app.repositories.author_repo import AuthorRepository as authorRepo
from app.utils import AuthUtils
from app.processes.decorators.require_auth import require_authentication 
from app.processes.decorators.suspected_author import suspected_author 

@authors.route("/confirm-its-me", methods=["GET", "POST"])
@require_authentication
@suspected_author
def confirmItsMe(suspected):
    currentuser = request.environ["currentuser"]
    userId = currentuser["id"]

    existed = authorRepo.getAuthor(id=suspected.id)
    if existed is not None and existed.isAssociatedToUser():
        if existed.userId != userId:
            raise Exception("already confirmed")
        else:
            raise Exception("author already associated to a different user")
    
    suspected.userId = userId
    saved = authorRepo.create(suspected)
    return AuthUtils.userSignInRes(saved.user.dto(currentuser["isAdmin"]))
    
