
from models.author import Author
from datetime import datetime 
from models.paperLink import PaperLink
from models.citationStats import CitationStats

class Paper:
    def __init__(self, id: str, corpusId: str, slug: str, title: str, description: str, authors: list[Author], fieldsOfStudy: list[str], publishedAt: datetime, primaryPaperLink: PaperLink, alternatePaperLinks: list[PaperLink], citationStats: CitationStats):
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
                publishedAt=datetime.strptime(json["pubDate"], '%Y-%m-%d'),
                primaryPaperLink=PaperLink.fromOriginJson(json["primaryPaperLink"]),
                alternatePaperLinks=[PaperLink.fromOriginJson(rawPaperLink) for rawPaperLink in json["alternatePaperLinks"]],
                citationStats=CitationStats.fromOriginJson(json["citationStats"]),
                );

    def __repr__(self):
        return f'''
            Paper(
                id: {self.id},
                corpusId: {self.corpusId},
                slug: {self.slug},
                title: {self.title},
                description: {self.description},
                authors: {self.authors},
                fieldsOfStudy: {self.fieldsOfStudy},
                publishedAt: {self.publishedAt},
                primaryPaperLink: {self.primaryPaperLink},
                alternatePaperLinks {self.alternatePaperLinks},
                citationStats: {self.citationStats},
            )
        ''';
               
