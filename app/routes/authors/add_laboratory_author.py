from . import authors
from app.processes.decorators.require_auth import require_authentication
from app.processes.decorators.require_admin_privilege import require_admin_privilege
from app.processes.decorators.suspected_author import suspected_author
from app.repositories.author_repo import AuthorRepository as authorRepo 

@authors.route('/add-labo-author',methods=["GET", "POST"])
@require_authentication
@require_admin_privilege
@suspected_author
def addLaboratoryAuthor(suspected):
    existing = authorRepo.getAuthor(id=suspected.id)
    if existing is None:
        existing = suspected

    existing.isPublic = True
    authorRepo.save()
    return {
        "addedAuthor": existing.serialize()
    }
    