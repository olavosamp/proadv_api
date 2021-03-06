import json

from api.models import SearchTerm
from api.utils import get_search_term, check_valid_keys
from api.defines import SEARCH_TERM_KEY_DICT

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Imports search term data from a JSON file with format: [{classificacao: str, termo: str}, ...]"

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        path = options['file_path'][0]
        reference_keys = SEARCH_TERM_KEY_DICT.values()

        print(f"\nLoading search terms from \n{path}")

        with open(path) as file_handle:
            string_data = file_handle.read()
        object_list = []
        for json_data in json.loads(string_data):
            if not check_valid_keys(json_data.keys(), reference_keys):
                print(f"\nInvalid data format: missing any of {list(reference_keys)}\nFile not loaded.")
                continue

            entry_dict = get_search_term(json_data)
            new_entry = SearchTerm(**entry_dict)

            object_list.append(new_entry)

        print(f"\nFound {len(object_list)} search term objects.")
        SearchTerm.objects.bulk_create(object_list)

        print(f"Import finished.")
