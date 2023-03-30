from __future__ import annotations;
from sqlalchemy_utils import UUIDType
from typing import Optional
from app.db import db 
from .fullName import FullName
   
class Author(db.Model):
    id = db.Column(db.String(), primary_key=True)
    slug = db.Column(db.String(), index= True, unique= True)
    name = db.Column(db.String())
    fullName = db.Column(db.JSON)
    userId = db.Column(db.ForeignKey("user.id"))
    user = db.relationship('User', back_populates='author')


    def __init__(self, id: str, slug: str, name: str, fullName: FullName | dict, userId: Optional[str] = None):
        self.id = id
        self.userId = userId
        self.slug = slug
        self.name = name
        self.fullName = fullName if type(fullName) is not dict else FullName.fromOriginJson(fullName)
    
    def isAssociatedToUser(self) -> bool:
        return self.userId is not None

    def fromOriginJson(json: dict[str, any]) -> Author:
        return Author(id=json[0]["ids"][0], slug=json[0]["slug"], name=json[0]["name"], fullName=FullName.fromOriginJson(json[0]["structuredName"]))

    def __eq__(self, other: Author) -> bool:
        if(self.id == other.id): return True
        return False;

    def serialize(self) -> dict:
        return {
            "authorId": self.id,
            "slug": self.slug,
            "name": self.name,
            "fullName": self.fullName.serialize(),
            "userId": self.userId,
        }
        
    def __repr__(self):
        return f'<Author id={self.id} userId={self.userId} slug={self.slug} name={self.name} fullName={self.fullName}>'