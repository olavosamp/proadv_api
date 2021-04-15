import json

from api.models import SearchTerm
from api.utils import get_search_term
from api.defines import SEARCH_TERM_KEYS

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Imports search term data from a JSON file with format: {classificacao: str, termo: str}"

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        path = options['file_path'][0]
        keys = SEARCH_TERM_KEYS.values()

        with open(path) as file_handle:
            string_data = file_handle.read()

        object_list = []
        for json_data in json.loads(string_data):
            if not set(keys).issubset(json_data.keys()):
                print(f"\nUnknown data format: missing any of {list(keys)}\nFile not loaded.")

            term_dict = get_search_term(json_data)
            new_term = SearchTerm(**term_dict)

            object_list.append(new_term)

        SearchTerm.objects.bulk_create(object_list)
