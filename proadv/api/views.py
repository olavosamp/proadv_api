from rest_framework import viewsets

from .serializers import PublicationSerializer, SearchTermSerializer
from .models import Publication, SearchTerm

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class SearchTermViewSet(viewsets.ModelViewSet):
    queryset = SearchTerm.objects.all()
    serializer_class = SearchTermSerializer
