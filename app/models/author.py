from __future__ import annotations
from sqlalchemy.sql import func
from typing import Optional
from app import db
from ..types.fullname import FullName, FullNameField
import random 
from .paper_author import paper_author
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(), index= True, unique= True)
    name = db.Column(db.String())
    fullName = db.Column(FullNameField)
    isPublic = db.Column(db.BOOLEAN, default=False)
    associationDate = db.Column(db.DateTime(timezone=True), server_default= func.now())
    userId = db.Column(db.ForeignKey("user.id"))
    user = db.relationship('User', back_populates='author')
    papers = db.relationship('Paper', secondary=paper_author, back_populates='authors')

    def __init__(self, id: str, slug: str, name: str, fullName: FullName | dict, isPublic: bool = False, userId: Optional[str] = None, isIdentifiable: bool = True):
        self.id = int(id)
        self.userId = userId
        self.slug = slug
        self.name = name
        self.fullName = fullName if type(fullName) is not dict else FullName.fromOriginJson(fullName)
        self.isPublic = isPublic
        self.isIdentifiable = isIdentifiable

    def fromOriginJson(json: dict[str, any]) -> Author:
        raw = json[0]
        isIdentifiable = len(raw["ids"]) > 0
        authorId = int(raw["ids"][0]) if isIdentifiable else random.randint(100000, 99999999999)
        return Author(id=authorId, slug=raw["slug"], name=raw["name"], fullName=FullName.fromOriginJson(raw["structuredName"]), isIdentifiable=isIdentifiable)

    def isAssociatedToUser(self) -> bool:
        return self.userId is not None

    def __eq__(self, other: Author) -> bool:
        if(self.id == other.id): return True
        return False;

    def serialize(self) -> dict:
        return {
            "authorId": self.id,
            "slug": self.slug,
            "name": self.name,
            "fullName": self.fullName.serialize(),
            "userId": self.userId.__str__(),
            "isAssociated": self.isAssociatedToUser(),
            "associatedTo": self.userId.__str__(),
            "associationDate": self.associationDate.__str__()
        }

        
    def __repr__(self):
        return f'<Author {self.name} id={self.id} userId={self.userId.__str__()} slug={self.slug} name={self.name} fullName={self.fullName}>'