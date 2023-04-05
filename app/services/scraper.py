import requests
from app.models import Paper
from app.constants import SSConst
from app.models import Author
from app.types.fullname import FullName
from typing import Optional
from app.constants.sort_by_filter import SortByFilter
class Scrapper:
    def fetchPapers(searchInput: str, page: Optional[int], authors_names: Optional[str]=[], sort_by: Optional[SortByFilter] = SortByFilter.RELEVANCE) -> list[Paper] | None:
        papers: list[Paper] = []
        result = requests.request("POST", SSConst.URL, headers={
                **SSConst.HEADERS,
                "referer": "https://www.semanticscholar.org/search?q=" + searchInput + "&sort=" + sort_by.__str__(),
                }, json={
                **SSConst.BODY,
                "queryString": str(searchInput),
                "page": page if page is not None else 1,
                "authors": authors_names,
                "sort": sort_by.__str__()
            })

        data: dict[str, any] = result.json()
        print("raw data : ", data)
        if('error' in data):
            raise Exception(data['error'])
        elif('results' in data and data['results'] == None or len(data['results']) == 0):
            return None
        else:
            for raw in data["results"]:
                currentPaper = Paper.fromOriginJson(raw)
                papers.append(currentPaper)

            print("processed data : ", papers)
            return papers
    
    def getAuthorById(searchInput: str, authorId: int | str, targetPage: Optional[int] = None) -> Author | None:
        if type(authorId) == str:
            authorId = int(authorId)

        if targetPage is not None:
            papers = Scrapper.fetchPapers(searchInput, targetPage)
            if papers is None: return papers
            for paper in papers:
                author = paper.getAuthorById(authorId)
                if author is not None: 
                    return author
            # Scrapper.lookupForAuthorInPapers(authorId, papers)
                
        found: Optional[Author] = None
        maxPagesIter = 5
        for currPage in range(1, maxPagesIter):
            papers = Scrapper.fetchPapers(searchInput, currPage)
            if papers is None: return papers
            for paper in papers:
                author = paper.getAuthorById(authorId)
                if author is not None:
                    found = author
                    break

        return found

    def getSuspectedAuthors(searchedName: str, notFoundCounter: Optional[int | str] = None) -> list[Author] | None:
        nfc = int(notFoundCounter) if (notFoundCounter is not None and int(notFoundCounter) >= 1) else 1
        papers = Scrapper.fetchPapers(searchedName, nfc)
        if papers is None: return None 
        authorsAcc: list[Author] = []
        for paper in papers:
            authorsAcc.extend(author for author in paper.authors if author not in authorsAcc)
        return authorsAcc

    def getPapersOfAuthor(author: Author | FullName,smc: Optional[int]):
        authorName = author.fullName.inline() if isinstance(author, Author) else author.inline()
        return Scrapper.fetchPapers(searchInput=authorName, authors_names=[authorName], page=smc)




            
