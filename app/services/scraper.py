import requests
from app.models import Paper
from app.constants import SSConst
from app.models import Author
from typing import Optional
class Scrapper:
    def fetchPapers(searchInput: str, page: int = 1):
        papers: list[Paper] = []
        result = requests.request("POST", SSConst.URL, headers=SSConst.HEADERS, json={
                "queryString": str(searchInput),
                "page": page,
                **SSConst.BODY,
            })
        data: dict[str, any] = result.json()
        if('error' in data):
            print(data['error'])
            return None
        elif('results' in data and data['results'] == None or len(data['results']) == 0):
            print('No Result Was Found!')
            return None
        else:
            for raw in data["results"]:
                currentPaper = Paper.fromOriginJson(raw)
                papers.append(currentPaper)
            return papers
        
    def lookupForAuthorInPapers(authorId: str, papers: list[Paper]) -> Author | None:
        for paper in papers:
                author = paper.getAuthorById(authorId)
                if author is not None: 
                    return author

    def getAuthorById(searchInput: str, authorId: str, targetPage: Optional[int] = None) -> Author | None:
        if targetPage is not None:
            papers = Scrapper.fetchPapers(searchInput, targetPage)
            if papers is None: return papers
            Scrapper.lookupForAuthorInPapers(authorId, papers)
                
        found: Optional[Author] = None
        currPage = 1
        maxPagesInter = 5
        while found is not None and currPage <= maxPagesInter:
            papers = Scrapper.fetchPapers(searchInput, currPage)
            if papers is None: return papers
            found = Scrapper.lookupForAuthorInPapers(authorId, papers)
            currPage += 1

        return found

    def getSuspectedAuthors(searchedName: str, notFoundCounter: Optional[int] = 1) -> list[Author] | None:
        papers = Scrapper.fetchPapers(searchedName, notFoundCounter)
        if papers is None: return None 
        authorsAcc: list[Author] = []
        for paper in papers:
            authorsAcc.extend(author for author in paper.authors if author not in authorsAcc)
        return authorsAcc

    def getPapersOfAuthor(author: Author):
        return "this function is for retrieving papers of a particular author"




            
