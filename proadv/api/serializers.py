from rest_framework import serializers

from .models import Publication, SearchTerm

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = ['terms', 'data']

class SearchTermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SearchTerm
        fields = ['classification', 'term']
