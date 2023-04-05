from sqlalchemy import TypeDecorator, JSON, String
import json

class PaperLink:
    def __init__(self, url: str, type: str): 
        self.url = url
        self.type = type;

    def fromOriginJson(json: dict[str, any]):
        return PaperLink(url=json["url"], type=json["linkType"]);

    def serialize(self) -> dict:
        return {
            "url": self.url,
            "type": self.type
        }
    def __repr__(self):
        return f'<PaperLink url={self.url} type={self.type}>'
    
class PaperLinkField(TypeDecorator):
    impl = JSON

    def __repr__(self):
        return self.impl.__repr__()
    
    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(JSON)

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        else:
            if isinstance(value, PaperLink):
                return value.serialize()

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return PaperLink.fromOriginJson(value)
        
class PaperLinksField(TypeDecorator):
    impl = JSON

    def __repr__(self):
        return self.impl.__repr__()
    
    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(JSON)

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        else:
            if isinstance(value, list[PaperLink]):
                return [p.serialize() for p in value].__str__()

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            rawLinks = json.loads(value)
            return [PaperLink.fromOriginJson(link) for link in rawLinks]