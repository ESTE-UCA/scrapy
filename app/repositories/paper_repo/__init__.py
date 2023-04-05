from app.models import Paper, Author
from typing import Optional

class PaperRepository:
    def exists(id: Optional[str], slug: Optional[str], corpusId: Optional[str]) -> bool:
        pass
    
    def getPapersWrittenBy(author: Author | str) -> Optional[Paper]:
        pass

    def getPaperById(id: str) -> Optional[Paper]:
        pass

    def getPaperBySlug(slug: str) -> Optional[Paper]:
        pass

    def getPaperByCorpusId(corpusId: int) -> Optional[Paper]:
        pass

    def save(paper: Paper | list[Paper]):
        pass
