
from typing import Optional
from app.db import db
from sqlalchemy.exc import NoResultFound
from app.models import Author

class AuthorRepository:
    def exists(id: str | None, slug: str | None) -> bool:
        return AuthorRepository.getAuthor(id, slug) is not None
    

    def getAuthor(id: Optional[int] = None, slug: Optional[str] = None) -> Author | None:
        assert(id is not None or slug is not None)
        try:
            filters = (Author.id == id) & (Author.slug == slug) if id is not None and slug is not None  \
                else (Author.id == id) if id is not None \
                else (Author.slug == slug)
            return db.session.execute(db.select(Author).filter(filters)).scalar_one()
        except Exception as e:
            if isinstance(e, NoResultFound):
                return None
            else:
                print(e)

    def getAuthorById(id: int) -> Author | None:
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
    
    def save() -> Author:
        db.session.commit()
    
    def create(author: Author) -> Author:
        try:
            db.session.add(author) 
            db.session.commit()
            return author
        except Exception as e:
            db.session.rollback()
            print('exception occurred on create: ', e)
    