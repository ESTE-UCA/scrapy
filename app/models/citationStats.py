

class YearlyIncreasedBy:
    def __init__(self, fromYear: str, toYear: str, increasedBy: int):
        self.fromYear = fromYear
        self.toYear = toYear
        self.increasedBy = increasedBy;

    def fromOriginJson(json: dict[str, any]):
        return YearlyIncreasedBy(
            fromYear=json["startKey"],
            toYear=json["endKey"],
            increasedBy=json["count"]
        );

    def __repr__(self):
        return f'''
            YearlyIncreasedBy(
                fromYear: {self.fromYear},
                toYear: {self.toYear},
                increasedBy: {self.increasedBy}
            )
        '''

        
class CitationStats:
    def __init__(self, allCitationsCount: int, keyCitationsCount: int, incrementStats: list[YearlyIncreasedBy]):
        self.allCitationsCount = allCitationsCount
        self.keyCitationsCount = keyCitationsCount
        self.incrementStats = incrementStats;
        
    def fromOriginJson(json: dict[str, any]):
        return CitationStats(
            allCitationsCount=json["numCitations"], 
            keyCitationsCount=json["numKeyCitations"],
            incrementStats=[
                YearlyIncreasedBy.fromOriginJson(rawIncreasedBy) 
                for rawIncreasedBy in json["citedByBuckets"]
            ]
        );

    def __repr__(self):
        return f'''
            CitationStats(
                allCitationsCount: {self.allCitationsCount},
                keyCitationCount: {self.keyCitationsCount},
                incrementStats: {self.incrementStats},
            )
        ''';