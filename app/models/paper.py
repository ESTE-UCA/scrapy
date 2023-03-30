from typing import Optional
from .author import Author
from datetime import datetime 
from .paperLink import PaperLink
from .citationStats import CitationStats
from app.db import db

class Paper:
    # id = db.Column(db.String(), primary_key=True)
    # corpusId = db.Column(db.String(), primary_key=True)
    # slug = db.Column(db.String(), unique=True)
    # title = db.Column(db.String())
    # description = db.Column(db.String())
    

    def __init__(self, id: str, corpusId: str, slug: str, title: str, description: str, authors: list[Author], fieldsOfStudy: list[str], primaryPaperLink: Optional[PaperLink] = None, alternatePaperLinks: Optional[list[PaperLink]] = None, citationStats: Optional[CitationStats] = None, publishedAt: Optional[datetime] = None):
        self.id = id
        self.corpusId = corpusId
        self.slug = slug
        self.title = title
        self.description = description
        self.authors = authors
        self.fieldsOfStudy = fieldsOfStudy
        self.publishedAt = publishedAt
        self.primaryPaperLink = primaryPaperLink
        self.alternatePaperLinks = alternatePaperLinks
        self.citationStats = citationStats;
    
    def getAuthorById(self, authorId: str) -> Author | None:
        for author in self.authors:
            if author.id == authorId:
                return author
        return None
    
    def isAuthoredBy(self, suspected: Author) -> bool :
        return self.authors.__contains__(suspected); 

    def fromOriginJson(json: dict[str, any]):
        return Paper(
                id=json["id"], 
                corpusId=json["corpusId"], 
                slug=json["slug"],
                title= json["title"]["text"],
                description=json["paperAbstract"]["text"],
                authors=[
                    Author.fromOriginJson(rawAuthor)
                    for rawAuthor in json["authors"]
                ],
                fieldsOfStudy=json["fieldsOfStudy"],
                publishedAt=datetime.strptime(json["pubDate"], '%Y-%m-%d') if "pubDate" in json else None,
                primaryPaperLink=PaperLink.fromOriginJson(json["primaryPaperLink"]) if "primaryPaperLink" in json else None,
                alternatePaperLinks=[PaperLink.fromOriginJson(rawPaperLink) for rawPaperLink in json["alternatePaperLinks"]] if "alternatePaperLinks" in json else None,
                citationStats=CitationStats.fromOriginJson(json["citationStats"]) if "citationStats" in json else None,
                );

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "corpus_id": self.corpusId,
            "slug": self.slug,
            "title": self.title,
            "desc": self.description,
            "authors": [author.serialize() for author in self.authors],
            "fields_of_study": self.fieldsOfStudy,
            "pub_date": self.publishedAt,
            "links": {
                "primary": self.primaryPaperLink.serialize() if self.primaryPaperLink is not None else None,
                "alternates": [
                    link.serialize()
                    for link in self.alternatePaperLinks
                ] or None
            }
        }

    def __repr__(self):
        return f'Paper id={self.id} corpusId={self.corpusId} slug={self.slug} title={self.title} description={self.description} authors={self.authors} fieldsOfStudy={self.fieldsOfStudy} publishedAt={self.publishedAt} primaryPaperLink={self.primaryPaperLink} alternatePaperLinks={self.alternatePaperLinks} citationStats={self.citationStats}>'
               
