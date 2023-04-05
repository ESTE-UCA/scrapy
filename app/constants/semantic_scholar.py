



class SSConst:
    URL = "https://www.semanticscholar.org/api/1/search"

    # HEADERS = {
    #     "authority": "www.semanticscholar.org",
    #     "accept": "/",
    #     "accept-language": "en-US,en-AS;q=0.9,en-ZA;q=0.8,en-GB;q=0.7,en;q=0.6,fr;q=0.5",
    #     "cache-control": "no-cache,no-store,must-revalidate,max-age=-1",
    #     "content-type": "application/json",
    #     "origin": "https://www.semanticscholar.org",
    #     "pragma": "no-cache",
    #     "sec-ch-ua": """Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111""",
    #     "sec-ch-ua-mobile": "?0",
    #     "sec-ch-ua-platform": """macOS""",
    #     "sec-fetch-dest": "empty",
    #     "sec-fetch-mode": "cors",
    #     "sec-fetch-site": "same-origin",
    #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    #     "x-s2-client": "webapp-browser",
    #     "x-s2-ui-version": "7e97edaafd1422c18139b206b1a373068a6da3dc"
    # }

    HEADERS = {
            "authority": "www.semanticscholar.org",
            "accept": "*/*",
            "accept-language": "en-US,en-AS;q=0.9,en-ZA;q=0.8,en-GB;q=0.7,en;q=0.6,fr;q=0.5",
            "cache-control": "no-cache,no-store,must-revalidate,max-age=-1",
            "content-type": "application/json",
            "cookie": """tid=rBIABmP2AVhneQAKCfEdAg==; _gcl_au=1.1.1386602317.1677066585; hubspotutk=ace1c7f4f89adfdac6a4093440b3b66c; pv2more=1677066592; pv2more10s=1677066696; s2_copyright_dismissed=1; _ga=GA1.1.238110995.1677066586; __hssrc=1; s2Exp=create_library_ftue_modal%3D-control%26abstract_highlighter_v2%3D-highlighted_abstract_default_toggle_off%26new_ab_framework_aa%3Dtest%26alerts_two_types_relevance_v2%3Drelevance_author%26paper_row_v2_font_only%3D-paper_row_v2_font_only%26new_ab_framework_mock_ab%3Dcontrol%26author_recs_content%3Dcontrol%26reader_note_taking%3D-enable_note_taking; g_state={"i_p":1682899315505,"i_l":4}; __hstc=132950225.ace1c7f4f89adfdac6a4093440b3b66c.1677066585852.1680478001984.1680480149444.19; sid=ebd3cfbb-2f68-4104-b5b3-f78847d03a8c; aws-waf-token=54087d3d-f6fd-416b-9d2b-0ad52e2b4d04:DAoAkuNcV+YAAAAA:kGlITcysem+OlD23cFL1jKn69v3kVKxiX1c5GlpL8LG9/ko7C9/JIhOZnucJq5b/pXI64qG5IffM3gWPGF86FNLu532pxiukodBBLPSnSDoGgzBFF2va6XY9wIjwFY7NH3NzPaUAkz0MpGt66YgPONPi0kcjSRAkN24lwXuff31Pvw+CRJ/ZhLVwPrbB; s2Hist=2023-04-05T00%3A00%3A00.000Z%7C1011110000100010000000000000000100000011111; _ga_H7P4ZT52H5=GS1.1.1680700422.29.0.1680700424.0.0.0; _hp2_props.2424575119=%7B%22feature%3Apdf_note_taking%22%3Atrue%2C%22feature%3Aweb_app_capable_meta_tag%22%3Afalse%2C%22feature%3Asearch_spellcheck_suggestions%22%3Afalse%2C%22experiment%3Anew_ab_framework_aa%22%3A%22test%22%2C%22feature%3Arelated_papers_search_cluster%22%3Afalse%2C%22feature%3Ahomepage_ads%22%3Afalse%2C%22feature%3Ause_fallback_search_cluster%22%3Afalse%2C%22feature%3Aahp_pronouns%22%3Atrue%2C%22experiment%3Aalerts_two_types_relevance_v2%22%3A%22relevance_author%22%2C%22feature%3Alog_heap_landmarks%22%3Afalse%2C%22feature%3Areader_skimming%22%3Atrue%2C%22feature%3Asatisfaction_survey%22%3Afalse%2C%22feature%3Aresearch_homepage_survey%22%3Atrue%2C%22feature%3Ahomepage_ad_semantic_reader%22%3Atrue%2C%22feature%3Acite_see%22%3Afalse%2C%22feature%3Asearch_citations_perf%22%3Afalse%2C%22feature%3Aall_papers_folders%22%3Atrue%2C%22feature%3Aauthor_claim_on_pdp%22%3Atrue%2C%22feature%3Aauthor_stats_gql%22%3Atrue%2C%22feature%3Ahomepage_ad_public_api%22%3Atrue%2C%22feature%3Ahydrate_search_from_ddb%22%3Atrue%2C%22feature%3Alogin_demographics_modal%22%3Atrue%2C%22feature%3Ahighly_influential_citations_scorecard%22%3Atrue%2C%22feature%3Aauth_google_one_tap%22%3Atrue%2C%22feature%3Ause_fallback_search_reranker_service%22%3Afalse%2C%22feature%3Aminify_js%22%3Atrue%2C%22feature%3Awith_entitlements%22%3Atrue%2C%22feature%3Ahomepage_ad_browser_ext%22%3Afalse%2C%22feature%3Asimilar_papers_pdp%22%3Atrue%2C%22feature%3Apdp_citation_suggestions%22%3Atrue%2C%22feature%3Ahubspot_newsletter_form%22%3Atrue%2C%22tid%22%3A%22rBIABmP2AVhneQAKCfEdAg%3D%3D%22%2C%22Is%20Signed%20In%22%3Afalse%2C%22experiment%3Anew_ab_framework_mock_ab%22%3A%22control%22%2C%22feature%3Aauthor_recs_exp%22%3Atrue%2C%22experiment%3Aauthor_recs_content%22%3A%22control%22%7D; _hp2_id.2424575119=%7B%22userId%22%3A%221143414285409631%22%2C%22pageviewId%22%3A%228529518733798634%22%2C%22sessionId%22%3A%22551383558797867%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.2424575119=%7B%22r%22%3A%22https%3A%2F%2Fwww.semanticscholar.org%2F%22%2C%22ts%22%3A1680700422653%2C%22d%22%3A%22www.semanticscholar.org%22%2C%22h%22%3A%22%2Fsearch%22%2C%22q%22%3A%22%3Fq%3DBenkirane%2522%26sort%3Drelevance%22%7D""",
            "origin": "https://www.semanticscholar.org",
            "pragma": "no-cache",
            # "referer": "https://www.semanticscholar.org/search",
            "sec-ch-ua": """Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111""",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": """macOS""",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "x-s2-client": "webapp-browser",
            "x-s2-ui-version": "7e97edaafd1422c18139b206b1a373068a6da3dc"
        }
    BODY = {
        "coAuthors": [],
        "venues": [],
        "fieldsOfStudy": [],
        "getQuerySuggestions": False,
        "hydrateWithDdb": True,
        "includeBadges": True,
        "includeTldrs": True,
        "pageSize": 10,
        "performTitleMatch": True,
        "requireViewablePdf": False,
        "sort": "relevance",
        "tldrModelVersion": "v2.0.0",
        "useFallbackRankerService": False,
        "useFallbackSearchCluster": False,
        "yearFilter": None,
        # "useS2FosFields": False
    }