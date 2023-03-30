



class SSConst:
    URL = "https://www.semanticscholar.org/api/1/search"
    HEADERS = {
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
    BODY = {
        "sort": "relevance",
        "authors": [],
        "coAuthors": [],
        "venues": [],
        "pageSize": 10,
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