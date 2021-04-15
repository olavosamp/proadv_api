from .defines import SEARCH_TERM_KEYS

def get_search_term(json_data):
    keys = SEARCH_TERM_KEYS

    new_term = json_data[keys["term"]]
    new_classification = json_data[keys["classification"]]

    return {"term": new_term, "classification": new_classification}
