from app.db import db
from app.models.user import User
from datetime import datetime
from sqlalchemy.exc import NoResultFound

 
class UserRepository:
    def exists(email: str | None = None, id: str | None = None) -> bool:
        return UserRepository.getUserByEmail(email=email) != None if email != None \
            else UserRepository.getUserById(id) != None if id != None \
            else False
    
    def getUserById(id: str) -> User | None:
        try:
            user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
            return user
        except Exception as e:
            if(isinstance(e, NoResultFound)):
                return None
    
    def getUserByEmail(email: str, test: bool = False) -> User | None:
        if(test):
            return User("5f37e1f8-56cb-41b7-b87a-aa0892e749ef","makouar@gmail.com", "hard_to_guess", datetime.now())
        try:
            user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
            return user
        except Exception as e:
            if(isinstance(e, NoResultFound)):
                return None


    def save(user: User) -> User:
        try:
            if not user.isPersisted():
                db.session.add(user)

            db.session.commit()
            return user
        except Exception as e:
            print("error on save", e)
            db.session.rollback()
        
