from __future__ import annotations
from sqlalchemy_utils import UUIDType
from datetime import datetime
from app.utils import PasswordHasher
from typing import Optional
from app import db
from sqlalchemy.sql import func
from app.processes.decorators.validate_form import UserCredential
import uuid

class User(db.Model):
    id = db.Column(UUIDType, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(120), index=True, unique=True)
    username =db.Column(db.String(120))
    password = db.Column(db.String(128), index=True, unique=True)
    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), server_default=func.now())
    author = db.relationship('Author', back_populates='user', uselist=False)
    
    def __init__(self, email: str, password: str, username: str, id: Optional[str] = None, createdAt: Optional[datetime] = None, updatedAt: Optional[datetime] = None):
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    @classmethod
    def create(self, credential: UserCredential) -> User:
        password = credential.password.value if credential.password.isHashed else PasswordHasher.toHash(credential.password.value)
        return User(email=credential.email.value, password=password, username=credential.username.value)
        
    def isPersisted(self) -> bool:
        return self.id != None

    def isPasswordMatched(self, password: str) -> bool:
        return PasswordHasher.compare(self.password, password)
    
    def payload(self) -> dict[str, any]:
        return {
            'id': self.id.__str__(),
            'email': self.email,
            'username': self.username,
        }
    
    def serialize(self) -> dict[str, any]:
        s = {
            **self.payload(),
            'createdAt': self.createdAt.__str__(),
            'updatedAt': self.updatedAt.__str__(),
            'isConfirmed': False,
        }
        if self.author is not None:
            arS = self.author.serialize()
            arS.pop("userId")
            s.update({**arS, "isConfirmed": True})
        return s
    
    def dto(self, isAdmin: bool = False) -> dict[str, any]:
        ser = {
            **self.serialize(),
            'isAdmin': isAdmin
        }
        ser.pop("updatedAt")
        return ser
    
    def __repr__(self) -> str:
        return f'<User id={self.id.__str__()} email={self.email} password={self.password} username={self.username} createdAt={self.createdAt} updatedAt={self.updatedAt}>'