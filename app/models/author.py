from __future__ import annotations;

class Author:
    def __init__(self, id: str, slug: str, name: str):
        self.id = id
        self.slug = slug
        self.name = name;

    def fromOriginJson(json: dict[str, any]):
        return Author(id=json[0]["ids"][0], slug=json[0]["slug"], name=json[0]["name"]);

    def __eq__(self, other: Author) -> bool:
        if(other != self): return False
        if(self.id == other.id and self.slug == other.slug): return True
        return False;
        
    def __repr__(self):
        return f'''
            Author(
                id: {self.id},
                slug: {self.slug},
                name: {self.name},
            )
        ''';