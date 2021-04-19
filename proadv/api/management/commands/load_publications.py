import json

from api.models import Publication
from api.utils import check_valid_keys
from api.defines import PUBLICATION_KEYS

from django.core.management import BaseCommand

def make_publication(json_data):
    return Publication(
        date=json_data["Data"],
        content=json_data["Conteudo"],
        observation=json_data["Observacao"],
        code=json_data["DiarioCodigo"]
    )

class Command(BaseCommand):
    help = "Imports publication data from a JSON file with format: [{key:value}, ...]. "+\
        "Must contain the following keys: {}.".format(PUBLICATION_KEYS)

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        path = options['file_path'][0]
        print(f"\nLoading publications from \n{path}")

        with open(path) as file_handle:
            string_data = file_handle.read()

        object_list = []
        for json_data in json.loads(string_data):
            if not check_valid_keys(json_data.keys(), PUBLICATION_KEYS):
                print(f"\nInvalid data format: missing any of {PUBLICATION_KEYS}\nFile not loaded.")
                return

            new_entry = make_publication(json_data)

            object_list.append(new_entry)

        print(f"\nFound {len(object_list)} publication objects.")
        Publication.objects.bulk_create(object_list)

        print(f"Import finished.")
