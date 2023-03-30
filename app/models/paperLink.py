


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