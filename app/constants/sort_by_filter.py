from enum import StrEnum


class SortByFilter(StrEnum):
    RELEVANCE = "relevance"
    CITATION_COUNT = "total-citations"
    INFLUENCE = "influence"
    RECENCY = "pub-date"