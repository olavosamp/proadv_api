from api.models import Publication, SearchTerm

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Search publications for search terms. If found, each term is added to the publication."

    def handle(self, *args, **options):
        print(f"\nSearching search terms in publications.")

        num_search_terms = SearchTerm.objects.count()
        print(f"\nFound {num_search_terms} search terms.")
        if num_search_terms < 1:
            raise ValueError("No search terms found.")

        num_publications = Publication.objects.count()
        print(f"\nFound {num_publications} publications.")
        if num_publications < 1:
            raise ValueError("No publications found.")

        for search_term in SearchTerm.objects.all():
            print("\nTerm: ", search_term.term)

            publications_qs = Publication.objects.filter(data__Conteudo__regex=search_term.term)
            print(f"Found {len(publications_qs)} matches")

            if publications_qs.count() > 0:
                print("Adding search term to publications.")
                search_term.publications.add(*publications_qs)
