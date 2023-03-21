import requests
from app.models import Paper


class Scrapper:
    def getSuspectedAuthors(name: str):
        return "this function is for retrieving a list of authors that the user might be one of them"
    def getPapersByAuthor(author):
        return "this function is for retrieving papers of a particular author"


search= input("what are you searching for : ")
url = "https://www.semanticscholar.org/api/1/search"
headers = {
            "authority": "www.semanticscholar.org",
            "accept": "*/*",
            "accept-language": "en-US,en-AS;q=0.9,en-ZA;q=0.8,en-GB;q=0.7,en;q=0.6,fr;q=0.5",
            "cache-control": "no-cache,no-store,must-revalidate,max-age=-1",
            "content-type": "application/json",
            "origin": "https://www.semanticscholar.org",
            "pragma": "no-cache",
            "referer": "https://www.semanticscholar.org/search",
            "sec-ch-ua": """Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110""",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": """macOS""",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "x-s2-client": "webapp-browser",
            "x-s2-ui-version": "d4ba3d82e4d31ab6f9dec97f346ea1a0a82584a3"
        }

postPageLimit= 10
payloadConstAttrs={
            "pageSize": postPageLimit,
            "sort": "relevance",
            "authors": [],
            "coAuthors": [],
            "venues": [],
            "yearFilter": None,
            "requireViewablePdf": True,
            "fieldsOfStudy": [],
            "useFallbackRankerService": False,
            "useFallbackSearchCluster": False,
            "hydrateWithDdb": True,
            "includeTldrs": False,
            "performTitleMatch": True,
            "includeBadges": False,
            "tldrModelVersion": "v2.0.0",
            "getQuerySuggestions": False,
            "useS2FosFields": False
}
papers: list[Paper] = []


for x in range(1,2):
        result = requests.request("POST", url, headers=headers, json={
            "queryString": str(search),
            "page": x,
            **payloadConstAttrs,
        })
        data: dict[str, any] = result.json()
        print(data)
        if('error' in data):
             print(data['error'])
        elif('results' in data and data['results'] == None or len(data['results']) == 0):
            print('No Result Was Found!')
        else:
            for raw in data["results"]:
                currentPaper = Paper.fromOriginJson(raw)
                papers.append(currentPaper)
            print(papers[0]);
            
