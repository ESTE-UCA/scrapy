from app.services.scraper import Scrapper
from flask import request
from . import authors
from app.processes.decorators.require_auth import require_authentication
from app.types.fullname import FullName

@authors.route("/suspected", methods=["GET", "POST"])
@require_authentication
def suspectedAuthors():
    currentuser = request.environ["currentuser"]
    searchedName = request.args.get("name")
    notFountCounter = request.args.get("nfc") 

    if searchedName is None:
        if currentuser["isConfirmed"]:
            searchedName = FullName.fromOriginJson(currentuser["fullName"]).inline()
        else:
            searchedName = currentuser["username"]
        notFountCounter = 1
        
    
    print("searched for user with name :", searchedName)
    suspectedAuthors = Scrapper.getSuspectedAuthors(searchedName, notFountCounter)
    if suspectedAuthors is None:
        return {
            "message": "no result was found"
        }
    
    print(suspectedAuthors)
    
    serAuthors = [author.serialize() for author in suspectedAuthors]

    return {
        "count": serAuthors.__len__(),
        "suspected_authors": serAuthors
    }