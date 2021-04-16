from .defines import SEARCH_TERM_KEY_DICT


def check_valid_keys(new, reference):
    return set(reference).issubset(set(new))


def get_search_term(json_data):
    keys = SEARCH_TERM_KEY_DICT

    new_term = json_data[keys["term"]]
    new_classification = json_data[keys["classification"]]

    return {"term": new_term, "classification": new_classification}
