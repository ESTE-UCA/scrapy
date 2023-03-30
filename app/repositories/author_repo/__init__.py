
from app.db import db
from sqlalchemy.exc import NoResultFound
from app.models import Author

class AuthorRepository:
    def exists(id: str | None, slug: str | None) -> bool:
        return AuthorRepository.getAuthorById(id) is not None if id is not None \
            else AuthorRepository.getAuthorBySlug(slug) is not None if slug is not None \
            else False
    
    def getAuthorById(id: str) -> Author | None:
        try:
            author = db.session.execute(db.select(Author).filter_by(id=id)).scalar_one()
            return author
        except Exception as e:
            if isinstance(e, NoResultFound):
                return None
            else:
                print(e)
                
    
    def getAuthorBySlug(slug: str) -> Author | None:
        try:
            author = db.session.execute(db.select(Author).filter_by(slug=slug)).scalar_one()
            return author
        except Exception as e:
            if isinstance(e, NoResultFound):
                return None
            else:
                print(e)
    
    
    
    def create(author: Author) -> Author:
        try:
            db.session.add(author)
            db.session.commit()
            return author
        except Exception as e:
            db.session.rollback()
            print(e)
    